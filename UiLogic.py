import streamlit as st
from DataExtraction import ExtractTextFromPDF

st.title("Ask Your Docs")

uploadedFile = st.file_uploader("Upload PDF Document", type = "pdf")

if uploadedFile:
    with open("dummy.pdf","wb") as f:
        f.write(uploadedFile.getbuffer())
    text = ExtractTextFromPDF("dummy.pdf")
    st.text_area("PDF Text", text, height = 300)