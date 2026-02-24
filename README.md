# NoticeSense - Phase 1 (MVP)

NoticeSense is an Agentic AI System for Understanding Official Notices. This repository contains **Phase 1 (MVP)**, which focuses on a working OCR-based notice text extraction system.

## Features
- **Upload Notices**: Accepts `.pdf`, `.png`, `.jpg`, and `.jpeg` formats.
- **OCR Text Extraction**: Uses Tesseract OCR to accurately extract text from documents.
- **PDF Conversion**: Uses `pdf2image` and Poppler to convert multi-page PDF notices to processable images.
- **Frontend UI**: A clean, modular Streamlit frontend for interacting with the OCR pipeline.

## Folder Structure
```text
NoticeSense/
├── backend/                  # Core backend logic
│   ├── core/
│   │   └── config.py         # Application settings & environment configurations
│   ├── services/
│   │   └── ocr_service.py    # Tesseract OCR extraction logic (PDF/Image)
│   └── utils/
│       └── file_utils.py     # File saving and upload directory cleanup utilities
├── data/
│   └── uploads/              # Temporary storage for uploaded user files
├── frontend/
│   └── app.py                # Streamlit UI for user interaction
├── .gitignore                # Ignored files (data/uploads, __pycache__, etc.)
├── requirements.txt          # Python dependencies
└── README.md                 # Project setup and documentation
```

## System Requirements & Prerequisites (Windows)

Before running the Python application, you **must** install the system-level dependencies for OCR.

1. **Install Tesseract OCR**:
   - Download the Windows installer from [UB-Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
   - Install it, usually to `C:\Program Files\Tesseract-OCR\`.
   - The path is configured in `backend/core/config.py`. Update the `TESSERACT_CMD` constant if you installed it elsewhere.

2. **Install Poppler** (Required for PDF processing):
   - Download the latest Poppler Windows binary from [Release poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases/).
   - Extract the `.zip` file to a folder like `C:\poppler\poppler-23.11.0\`.
   - Update `POPPLER_PATH` in `backend/core/config.py` to point to the `Library\bin` folder inside the extracted Poppler directory.

## Setup Instructions

1. **Create and Activate a Virtual Environment**
   Open your terminal (Command Prompt/PowerShell) in the `NoticeSense` folder and run:
   ```bash
   python -m venv venv
   
   # Activate on Windows:
   venv\Scripts\activate
   ```

2. **Install Python Dependencies**
   Run the following command to install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Configuration Paths**
   Open `backend/core/config.py` and ensure the paths matches your system installation:
   ```python
   TESSERACT_CMD: str = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   POPPLER_PATH: str = r"C:\poppler\poppler-xx.xx.x\Library\bin"
   ```

4. **Run the Streamlit Application**
   Start the frontend server from the project root:
   ```bash
   python -m streamlit run frontend/app.py
   ```
   
   The application will be accessible at `http://localhost:8501`.

## Modularity for NoticeSense Future Phases
This code is structured cleanly into `backend/services/` and `frontend/`. 
As Phase 2 starts, we can easily add new AI Agents (e.g., `llm_service.py`, `agent_workflow.py`) inside `services/` and expose them through FastAPI endpoints for deeper system integration without breaking the existing OCR pipeline.
