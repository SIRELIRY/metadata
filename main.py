import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def extract_metadata(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find('title').text if soup.find('title') else 'N/A'
        
        description = 'N/A'
        keywords = 'N/A'
        
        for meta in soup.find_all('meta'):
            if 'name' in meta.attrs:
                if meta.attrs['name'].lower() == 'description':
                    description = meta.attrs['content']
                elif meta.attrs['name'].lower() == 'keywords':
                    keywords = meta.attrs['content']
        
        return {'URL': url, 'Title': title, 'Description': description, 'Keywords': keywords}
    except Exception as e:
        return {'URL': url, 'Title': 'Error', 'Description': str(e), 'Keywords': 'N/A'}

def save_to_excel(metadata_list, output_file):
    df = pd.DataFrame(metadata_list)
    df.to_excel(output_file, index=False)
    messagebox.showinfo("성공", f"메타데이터가 {output_file}에 저장되었습니다")

def on_extract():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("입력 오류", "URL을 입력하세요")
        return
    
    metadata = extract_metadata(url)
    metadata_list.append(metadata)
    update_treeview(metadata)

def update_treeview(metadata):
    tree.insert("", tk.END, values=(metadata['URL'], metadata['Title'], metadata['Description'], metadata['Keywords']))

def on_save():
    output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if output_file:
        save_to_excel(metadata_list, output_file)

def copy_to_clipboard(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item['values']
        column = tree.identify_column(event.x)
        column_index = int(column.replace('#', '')) - 1
        app.clipboard_clear()
        app.clipboard_append(values[column_index])
        messagebox.showinfo("복사됨", "선택한 셀의 내용이 복사되었습니다")

app = tk.Tk()
app.title("메타데이터 추출기")
app.geometry("800x600")
app.configure(bg="#F5F5F5")

metadata_list = []

font_style = ("Pretendard", 12)

frame = tk.Frame(app, bg="#F5F5F5")
frame.pack(fill="both", expand=True, padx=10, pady=10)

url_label = tk.Label(frame, text="URL 입력:", font=font_style, bg="#F5F5F5")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

url_entry = tk.Entry(frame, width=50, font=font_style)
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

extract_button = tk.Button(frame, text="메타데이터 추출", font=font_style, command=on_extract, relief="flat", bg="#0078D4", fg="white", bd=0, padx=20, pady=10)
extract_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

tree_frame = tk.Frame(frame)
tree_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

columns = ("URL", "제목", "설명", "키워드")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
tree.heading("URL", text="URL")
tree.heading("제목", text="제목")
tree.heading("설명", text="설명")
tree.heading("키워드", text="키워드")

tree.pack(side="left", fill="both", expand=True)

scrollbar_y = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar_y.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar_y.set)

scrollbar_x = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
scrollbar_x.grid(row=2, column=0, columnspan=3, sticky="ew")
tree.configure(xscrollcommand=scrollbar_x.set)

save_button = tk.Button(frame, text="엑셀 파일로 저장", font=font_style, command=on_save, relief="flat", bg="#0078D4", fg="white", bd=0, padx=20, pady=10)
save_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

for col in columns:
    tree.column(col, width=200)

tree.bind("<Double-1>", copy_to_clipboard)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

def style_button(button):
    button.config(
        relief="flat",
        bg="#0078D4",
        fg="white",
        activebackground="#005BB5",
        activeforeground="white",
        bd=0,
        padx=20,
        pady=10
    )

style_button(extract_button)
style_button(save_button)

app.mainloop()

