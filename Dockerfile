FROM python:3.10-slim

# Cài các công cụ cần thiết
RUN apt-get update && apt-get install -y \
    build-essential cmake git wget unzip libgtk2.0-dev libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Cài Python packages
RUN pip install --no-cache-dir opencv-python numpy matplotlib

# (Tuỳ chọn) copy code vào container
WORKDIR /app
COPY . /app
