import sys
import os
from pathlib import Path

# Add project root to python path to allow importing backend modules
project_root = str(Path(__file__).parent.parent.absolute())
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
from backend.utils.file_utils import save_upload_file, clean_upload_dir
from backend.services.ocr_service import process_document
from backend.services.parsing_service import process_and_structure_document
import json

st.set_page_config(
    page_title="NoticeSense MVP",
    page_icon="📄",
    layout="wide"
)

def main():
    st.title("NoticeSense - OCR Pipeline (Phase 1 MVP)")
    st.markdown("""
    Welcome to the **NoticeSense** text extraction system. 
    Upload a Notice Document (PDF or Image) to extract its text content using Agentic AI workflows and Tesseract OCR.
    """)
    
    # Optional styling
    st.markdown("""
        <style>
        .stTextArea textarea {
            font-family: monospace;
            font-size: 14px;
        }
        </style>
    """, unsafe_allow_html=True)

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a notice document", 
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        st.info(f"File '{uploaded_file.name}' selected. Processing...")
        
        # Save file temporarily
        try:
            saved_path = save_upload_file(uploaded_file)
            
            # Action button
            if st.button("Extract & Structure Text", type="primary"):
                with st.spinner("Running OCR extraction & Parsing..."):
                    # Extract text using OCR service
                    extracted_text = process_document(saved_path)
                    
                    if extracted_text.startswith("Error"):
                        st.error(extracted_text)
                    else:
                        st.success("Extraction & Parsing Complete!")
                        
                        # Process and structure the document
                        structured_data, cleaned_text = process_and_structure_document(extracted_text)
                        
                        # Get document type
                        doc_type = structured_data.get("document_type", "Unknown Document Type")
                        st.subheader(f"Extracted Entities ({doc_type})")
                        
                        # Create tabs for structured views
                        tab1, tab2, tab3 = st.tabs(["📝 Structured JSON", "📄 Cleaned Text", "🔍 Raw Output"])
                        
                        with tab1:
                            st.json(structured_data, expanded=True)
                            
                        with tab2:
                            st.text_area(
                                "Cleaned OCR Text",
                                value=cleaned_text,
                                height=400,
                                disabled=True
                            )
                            
                        with tab3:
                            st.text_area(
                                "Raw Output", 
                                value=extracted_text, 
                                height=400,
                                disabled=True
                            )
        except Exception as e:
            st.error(f"Failed to process file: {str(e)}")
        finally:
            pass
            
    # Cleanup button on sidebar
    if st.sidebar.button("Clean Temporary Files"):
        clean_upload_dir()
        st.sidebar.success("Cleaned up upload directory.")

if __name__ == "__main__":
    main()
