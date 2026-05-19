# 🌐 Multilingual Text Preprocessor

> *A modular FastAPI + Streamlit text preprocessing system for English and Arabic – containerized as a single Docker image running both API and GUI seamlessly.*

---

## 📌 Overview

Cleaning and normalizing text for natural language processing (NLP) is essential, especially when working with multiple languages like **English** and **Arabic**. This project provides a **ready‑to‑use, containerized solution** that:

- Accepts raw text via a clean **Streamlit web interface**
- Sends it to a **FastAPI backend** for preprocessing
- Returns normalized, cleaned text with language detection and mismatch warnings

All components run inside a **single Docker image** – no complex orchestration required.

---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🔤 **Bilingual support** | Handles English and Arabic text with language‑specific preprocessing rules. |
| 🧹 **Text cleaning** | Removes diacritics (Arabic), extra spaces, punctuation, digits, and lowercases. |
| ⚠️ **Language mismatch detection** | The GUI validates expected vs. detected language and reports mismatches. |
| 🐳 **Single‑image deployment** | Both FastAPI (port `8000`) and Streamlit (port `8501`) run inside one container. |
| 📦 **NLTK preloaded** | The Docker image includes required NLTK models – starts ready to use. |

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend API** | FastAPI (Uvicorn) |
| **Frontend GUI** | Streamlit |
| **Containerization** | Docker |
| **NLP Libraries** | NLTK, regex, custom Arabic normalizer |
| **Language** | Python 3.9+ |

---

## 📂 Repository Structure

```
multilingual-preprocessing/
├── src/
│   └── main.py               # FastAPI backend (endpoint: /process)
├── frontend/
│   └── app.py                # Streamlit frontend
├── requirements.txt          # Python dependencies
├── Dockerfile                # Multi‑service container definition
└── README.md                 # This file
```

---

## 🚀 Local Setup (without Docker)

### 1. Clone & Navigate
```bash
git clone https://github.com/yourusername/multilingual-preprocessing.git
cd multilingual-preprocessing
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

- **Windows**: `venv\Scripts\Activate.ps1` (or `activate.bat`)
- **macOS/Linux**: `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Backend (FastAPI)
```bash
venv\Scripts\python.exe -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Start Frontend (Streamlit) – in a separate terminal
```bash
venv\Scripts\python.exe -m streamlit run frontend\app.py --server.port 8501 --server.address 0.0.0.0
```

### 6. Open the Web UI
- Navigate to: **`http://localhost:8501`**

> ℹ️ The backend API will be available at `http://localhost:8000/process` for direct calls.

---

## 🐳 Docker Setup (Recommended)

### Build the Image
```bash
docker build -t text-preprocessor .
```

### Run the Container
```bash
docker run -p 8000:8000 -p 8501:8501 text-preprocessor
```

### Access the Application
- **Streamlit GUI**: `http://localhost:8501`
- **FastAPI API**: `http://localhost:8000/process` (POST)

The container runs both services simultaneously – no additional steps needed.

---

## 🔌 API Usage (Direct)

**Endpoint**: `POST /process`

**Request Body** (JSON):
```json
{
  "text": "Your input text here...",
  "expected_language": "english"   // or "arabic"
}
```

**Response** (JSON):
```json
{
  "original_text": "...",
  "cleaned_text": "...",
  "detected_language": "english",
  "mismatch": false
}
```

You can test with `curl` or any HTTP client.


---

## 👥 Acknowledgments

- Built with FastAPI, Streamlit, and NLTK.
- Inspired by real‑world multilingual NLP preprocessing needs.

---


## 🙏 Thank You

For questions, issues, or contributions, please feel free to contact me.





