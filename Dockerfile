FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY data_ingestion_script.py .

CMD ["python", "data_ingestion_script.py"]
