FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy individual files from app/
COPY app/main.py .
COPY app/utils.py .
COPY app/classify_headings.py .

# Copy model folder
COPY app/model ./model
