# Dockerfile

FROM python:3.12-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Çalışma dizini
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY celery_signal_test ./celery_signal_test
COPY send_signal.sh .
RUN chmod +x send_signal.sh

# Worker başlatma komutu
CMD ["celery", "-A", "celery_signal_test", "worker", "--loglevel=INFO"]
