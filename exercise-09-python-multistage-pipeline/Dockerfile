FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir flake8

COPY app.py test_app.py ./

EXPOSE 5000

CMD ["python", "app.py"]
