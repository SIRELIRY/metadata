# Metadata Extractor

이 프로젝트는 주어진 URL 목록에서 메타데이터(title, description, keywords)를 추출하여 엑셀 파일로 저장하는 Python 스크립트입니다.

## 설정 방법

1. 가상 환경 생성 및 활성화:
    ```sh
    python -m venv venv
    .\venv\Scripts\Activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

2. 필요한 라이브러리 설치:
    ```sh
    pip install -r requirements.txt
    ```

3. `main.py` 실행:
    ```sh
    python .\main.py
    ```

## 파일 구조

metadata_extractor/
│
├── data/
│ └── metadata.xlsx # 추출된 메타데이터를 저장할 엑셀 파일
│
├── venv/ # 가상 환경 폴더
│ └── ... # 가상 환경 관련 파일
│
├── main.py # 메인 스크립트 파일
├── requirements.txt # 필요한 라이브러리 목록 파일
└── README.md # 프로젝트 설명 파일