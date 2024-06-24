# Metadata Extractor

이 프로젝트는 주어진 URL 목록에서 메타데이터(title, description, keywords)를 추출하여 엑셀 파일로 저장하는 Python 스크립트입니다.

## 프로젝트 구조

metadata_extractor/
│
├── data/ # 데이터 파일 저장 폴더
│ └── metadata.xlsx # 추출된 메타데이터를 저장할 엑셀 파일
│
├── venv/ # 가상 환경 폴더
│ └── ... # 가상 환경 관련 파일
│
├── main.py # 메인 스크립트 파일
├── requirements.txt # 필요한 라이브러리 목록 파일
├── README.md # 프로젝트 설명 파일
└── .gitignore # Git에 포함되지 않을 파일 목록


## 설정 방법 (Windows & macOS)

### 공통

1. 저장소 클론:
    ```sh
    git clone https://github.com/SIRELIRY/metadata.git
    cd metadata
    ```

2. 가상 환경 생성 및 활성화:
    - **Windows**
      ```sh
      python -m venv venv
      .\venv\Scripts\Activate
      ```
    - **macOS**
      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```

3. 필요한 라이브러리 설치:
    ```sh
    pip install -r requirements.txt
    ```

### Windows

4. 실행 파일 생성:
    ```sh
    pyinstaller --onefile --windowed main.py
    ```

5. 생성된 실행 파일은 `dist/main.exe`에 위치합니다.

### macOS

4. 실행 파일 생성:
    ```sh
    pyinstaller --onefile --windowed main.py
    ```

5. 생성된 실행 파일은 `dist/main`에 위치합니다.

## 실행 방법

1. 가상 환경 활성화:
    - **Windows**
      ```sh
      .\venv\Scripts\Activate
      ```
    - **macOS**
      ```sh
      source venv/bin/activate
      ```

2. 스크립트 실행:
    ```sh
    python main.py
    ```

## 필요 라이브러리

프로젝트를 실행하기 위해 다음 라이브러리가 필요합니다:

- requests
- beautifulsoup4
- pandas
- openpyxl
- pyinstaller

이 라이브러리는 `requirements.txt` 파일에 정의되어 있으며, 다음 명령을 통해 설치할 수 있습니다:

```sh
pip install -r requirements.txt

기여를 원하시면, 이 저장소를 포크하고 새로운 기능을 추가하거나 버그를 수정한 후 풀 리퀘스트를 보내주세요. 기여해주셔서 감사합니다!
