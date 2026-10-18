
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Install CPU-only PyTorch
RUN pip install --no-cache-dir --timeout 300 --retries 10 \
    --index-url https://download.pytorch.org/whl/cpu \
    torch==2.8.0+cpu

# Install the remaining dependencies
RUN pip install --no-cache-dir --timeout 300 --retries 10 \
    -r requirements.txt

COPY app.py .
COPY course_model ./course_model

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
