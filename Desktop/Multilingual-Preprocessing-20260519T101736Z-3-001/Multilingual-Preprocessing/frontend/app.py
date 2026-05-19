import streamlit as st
import requests

API_URL = "http://localhost:8000/process"

st.set_page_config(
    page_title="Multilingual Text Preprocessor",
    page_icon="🌐",
    layout="wide",
)

st.markdown(
    """
    <style>
    .css-1rs6os.edgvbvh3 {padding-top: 2rem;}
    .stButton>button {background-color: #0057b7; color: white;}
    .stButton>button:hover {background-color: #003f8a;}
    .block-container {padding: 2rem 3rem 3rem 3rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Multilingual Text Preprocessor")
st.write("A modern interface for English and Arabic text cleaning.")

with st.sidebar:
    st.header("Pipeline Settings")
    language = st.selectbox("Language", ["en", "ar"])
    remove_stopwords = st.checkbox("Remove stopwords", True)
    remove_punctuation = st.checkbox("Remove punctuation", True)
    normalize = st.checkbox("Normalize text", True)
    stemming = st.checkbox("Apply stemming", False)
    lemmatize = st.checkbox("Apply lemmatization", False)
    st.markdown("---")
    st.markdown(
        "This project preprocesses English and Arabic text using a shared API backend and a clean GUI. "
        "Use the settings to control stopwords, normalization, punctuation removal, stemming, and lemmatization."
    )

col1, col2 = st.columns([3, 2])
with col1:
    text = st.text_area("Enter text to preprocess", height=260)
    if st.button("Process"):
        if not text.strip():
            st.warning("Please enter some text before processing.")
        else:
            with st.spinner("Processing text..."):
                response = requests.post(
                    API_URL,
                    json={
                        "text": text,
                        "language": language,
                        "remove_stopwords": remove_stopwords,
                        "remove_punctuation": remove_punctuation,
                        "stemming": stemming,
                        "lemmatize": lemmatize,
                        "normalize": normalize,
                    },
                )

            if response.ok:
                data = response.json()
                st.success("Text processed successfully.")
                st.markdown("---")
                st.subheader("Original")
                st.write(data["original"])
                st.subheader("Processed")
                st.write(data["processed"])
            else:
                st.error(f"Processing failed: {response.text}")

with col2:
    st.subheader("How to use")
    st.write("1. Choose the correct language for your input.")
    st.write("2. Enter the text in the left box.")
    st.write("3. Enable the preprocessing steps you want.")
    st.write("4. Click Process to see the cleaned output.")
    st.markdown("---")
    st.subheader("Notes")
    st.write("• English validation checks for Latin letters.")
    st.write("• Arabic validation checks for Arabic script.")
    st.write("• Stemming and lemmatization are designed for English text.")
    st.write("• Normalization handles letter forms and punctuation removal.")
