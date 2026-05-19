FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt stopwords wordnet

EXPOSE 8000 8501

CMD ["bash", "entrypoint.sh"]