# Multilingual Text Preprocessor

A modular FastAPI + Streamlit text preprocessing system for English and Arabic.
The project is containerized as a single Docker image that runs both the API and the GUI together.

## Local setup

```bash
cd C:\Users\Admin\Desktop\multilingual-preprocessing
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start the backend API:

```bash
venv\Scripts\python.exe -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Start the Streamlit frontend:

```bash
venv\Scripts\python.exe -m streamlit run frontend\app.py --server.port 8501 --server.address 0.0.0.0
```

Open the web UI:

- `http://localhost:8501`

## Docker

Build the image:

```bash
docker build -t text-preprocessor .
```

Run the container:

```bash
docker run -p 8000:8000 -p 8501:8501 text-preprocessor
```

Once the container starts, the web app is available at:

- `http://localhost:8501`

## Notes

- The backend API is available at `http://localhost:8000/process`.
- The GUI validates English and Arabic input and reports mismatches.
- The Docker image includes NLTK model downloads, so it starts ready to use.

make this read me more attractive and professional in the same way
