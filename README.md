# Metadata Extractor

이 프로젝트는 주어진 URL 목록에서 메타데이터(title, description, keywords)를 추출하여 엑셀 파일로 저장하는 Python 스크립트입니다.

## 설정 방법 (macOS)

1. 저장소 클론:
    ```sh
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. 가상 환경 생성 및 활성화:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. 필요한 라이브러리 설치:
    ```sh
    pip install -r requirements.txt
    ```

4. 실행 파일 생성:
    ```sh
    pyinstaller --onefile --windowed main.py
    ```

5. 생성된 실행 파일은 `dist/main`에 위치합니다.
