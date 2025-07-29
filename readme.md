# 🚀 Hướng Dẫn Cài Docker, OpenCV-Python và YOLOv5

## 🐳 1. Cài Đặt Docker Phiên Bản Cũ

### macOS  
Tải Docker Desktop phiên bản 4.25.2 cho Mac (amd64):  
[🔗 Tải tại đây](https://desktop.docker.com/mac/main/amd64/129061/Docker.dmg)

### Windows  
Cài đặt Docker Desktop 4.25.0 qua Chocolatey:

```bash
choco install docker-desktop --version=4.25.0
```

Hoặc tham khảo link:  
[https://community.chocolatey.org/packages/docker-desktop/4.25.0](https://community.chocolatey.org/packages/docker-desktop/4.25.0)

---

## 🐍 2. Tạo Docker Image có sẵn OpenCV-Python

Bạn có thể dùng các Docker image như:

- `jupyter/scipy-notebook`
- `python:3.10` rồi cài thêm `opencv-python`

### 📌 Ví dụ Dockerfile

```Dockerfile
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
```

### 🛠️ Build image

```bash
docker build -t my-opencv-image .
```

### ▶️ Chạy container

```bash
docker run -it --rm -v $(pwd):/app my-opencv-image bash
```

---

## ✅ 3. Kiểm Tra OpenCV Trong Container

```bash
python
```

Trong Python shell:

```python
import cv2
print(cv2.__version__)
```

Kết quả ví dụ:

```
4.8.1
```

### 🖼️ Tạo ảnh kiểm tra

```python
import numpy as np
img = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.imwrite("test.png", img)
```

Sau đó gõ:

```bash
ls
```

Kết quả: bạn sẽ thấy file `test.png` được tạo → chứng minh `cv2` hoạt động.

---

## ⚙️ 4. Dùng Docker Interpreter Trong PyCharm

1. Mở **Settings → Project: ... → Python Interpreter**
2. Bấm biểu tượng `⚙` → `Add...`
3. Chọn `Docker` → `New...`
4. Nếu dùng Docker Desktop: chọn Unix socket
5. Chọn đúng image (ví dụ: `my-opencv-image`)
6. Nhấn `OK`

---

## ➕ 5. Cài Thêm Thư Viện Trong Container

Ví dụ container có tên là `opencv-container`:

```bash
docker exec -it opencv-container pip install scikit-learn pandas
```

Hoặc thêm vào `Dockerfile` để giữ nguyên trạng thái.

---

## 📦 6. Các Cách Cài OpenCV-Python

### Cách 1: Qua pip

```bash
pip install opencv-python
```

### Cách 2: Cài thủ công từ GitHub

```bash
git clone https://github.com/opencv/opencv-python.git
cd opencv-python

python -m venv venv
source venv/bin/activate  # Windows dùng .\venv\Scripts\activate

pip install -r requirements.txt
python setup.py bdist_wheel
pip install dist/*.whl
```

---

# 🎯 Cài Đặt YOLOv5

## 1. Qua Terminal

```bash
pip install torch torchvision torchaudio
pip install opencv-python matplotlib

git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

---

## 2. Qua Giao Diện PyCharm

- **Bước 1:** Mở `Settings` hoặc `Preferences`
- **Bước 2:** Vào `Project → Python Interpreter`
- **Bước 3:** Bấm `+` → tìm và cài các thư viện như `torch`, `opencv-python`

---

## 3. Clone và Cài Đặt YOLOv5 Repo

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

**Lưu ý:** Nên chạy PyCharm bằng quyền **Administrator** trên Windows.

---

## 4. Cài YOLOv5 Vào Virtual Environment (venv)

- Tải ZIP từ [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
- Giải nén vào thư mục, ví dụ: `C:\Users\PC\Downloads\yolov5-main`

Sau đó trong PyCharm terminal:

```bash
cd "C:\Users\PC\Downloads\yolov5-main"
pip install -r requirements.txt
```

---

## 5. Tải Model EAST (Text Detection)

- [Tải `frozen_east_text_detection.pb`](https://github.com/opencv/opencv_extra/blob/master/testdata/dnn/download_models.py)
- Hoặc thêm link Google Drive tùy ý

---
