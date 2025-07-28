<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Hướng dẫn cài đặt YOLOv5 và các thư viện liên quan

## 1. Cài đặt thư viện qua Terminal

```bash
pip install torch torchvision torchaudio
pip install opencv-python matplotlib
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```


## 2. Cài đặt thư viện qua giao diện PyCharm (GUI)

**Bước 1:** Mở Settings (Windows) hoặc Preferences (macOS)

- Windows/Linux: `File → Settings`
- macOS: `PyCharm → Preferences`

**Bước 2:** Chọn Python Interpreter

- Vào `Project: [Tên dự án của bạn] → Python Interpreter`
- Nhấn vào nút `+` ở góc trên bên phải

**Bước 3:** Tìm và cài đặt thư viện

- Nhập tên thư viện cần cài (ví dụ: `opencv-python`, `torch`, `matplotlib`)
- Nhấn `Install Package`


## 3. Clone và cài đặt repo YOLOv5

```bash
# Clone YOLOv5 repo
git clone https://github.com/ultralytics/yolov5
cd yolov5

# Cài các thư viện cần thiết từ requirements.txt
pip install -r requirements.txt
```

**Lưu ý:**
Nên chạy PyCharm bằng quyền Administrator để tránh lỗi phân quyền khi cài các thư viện.

## 4. Cài YOLOv5 thủ công vào môi trường ảo (venv) của PyCharm Project

**Bước 1:** Tải và giải nén YOLOv5

- Vào [YOLOv5 GitHub](https://github.com/ultralytics/yolov5)
- Nhấn nút `Code` → `Download ZIP`
- Giải nén, ví dụ: `C:\Users\PC\Downloads\yolov5-main`

**Bước 2:** Mở lại PyCharm, đảm bảo dùng đúng môi trường ảo

- Vào `File → Settings → Project: [Tên project] → Python Interpreter`
- Đảm bảo Python interpreter là `.venv\Scripts\python.exe` của dự án

**Bước 3:** Cài các thư viện cần thiết vào đúng venv

- Dùng Terminal trong PyCharm:

```bash
cd đường_dẫn_đến_yolov5_main
pip install -r requirements.txt
```

**Ví dụ:**

```bash
cd "C:\Users\PC\Downloads\yolov5-main"
pip install -r requirements.txt
```

*Câu lệnh trên sẽ cài các thư viện (`torch`, `opencv`, `matplotlib`...) vào đúng venv nếu bạn chạy trong Terminal của PyCharm.*

## 5. Tải model EAST (Text Detection Model)

- **Tải file `frozen_east_text_detection.pb` tại:**
[Download script trên GitHub OpenCV](https://github.com/opencv/opencv_extra/blob/master/testdata/dnn/download_models.py)
- **Hoặc tải trực tiếp qua Google Drive**
*(Bạn có thể cung cấp thêm link Google Drive tại đây nếu có)*

> Hãy copy toàn bộ nội dung và dán lên README.md GitHub của bạn để hướng dẫn người dùng setup nhanh chóng, trực quan.

<div style="text-align: center">⁂</div>

[^1]: https://github.com/ultralytics/yolov5

