import os
from pydantic_settings import BaseSettings

# Calculate project root dynamically
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "NoticeSense Phase 1 OCR"
    PROJECT_VERSION: str = "0.1.0"
    
    # Path configurations (adjust these as per system installation on Windows)
    TESSERACT_CMD: str = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    POPPLER_PATH: str = os.path.join(PROJECT_ROOT, ".poppler", "poppler-24.08.0", "Library", "bin")

    # Storage Settings
    UPLOAD_DIR: str = "data/uploads"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instance to be used across the application
settings = Settings()

# Ensure required directories exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
