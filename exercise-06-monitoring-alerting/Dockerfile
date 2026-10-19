FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY delivery_metrics.py .

USER 10001:10001

EXPOSE 8000

CMD ["python", "-u", "delivery_metrics.py"]
