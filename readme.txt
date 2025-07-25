pip install torch torchvision torchaudio
pip install opencv-python matplotlib
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt

Cài đặt thư viện bằng giao diện PyCharm (GUI)
🔹 Bước 1: Mở Settings (Windows) hoặc Preferences (macOS)
Vào menu:
File → Settings (Windows/Linux)
hoặc
PyCharm → Preferences (macOS)

🔹 Bước 2: Chọn Python Interpreter
Trong cửa sổ Settings/Preferences:

Vào Project: [Tên dự án của bạn] → Python Interpreter

Nhấn vào nút + ở góc trên bên phải

🔹 Bước 3: Tìm và cài thư viện
Tìm tên thư viện cần cài (ví dụ: opencv-python, torch, matplotlib)

Nhấn Install Package

# Clone YOLOv5 repo
git clone https://github.com/ultralytics/yolov5
cd yolov5

# Cài các thư viện cần thiết từ requirements.txt
pip install -r requirements.txt

Chạy PyCharm bằng quyền Administrator

Cách cài YOLOv5 thủ công vào venv của project PyCharm
🔹 Bước 1: Tải và giải nén YOLOv5
Vào GitHub: https://github.com/ultralytics/yolov5

Nhấn nút Code → Download ZIP

Giải nén, ví dụ vào thư mục: C:\Users\PC\Downloads\yolov5-main

🔹 Bước 2: Mở lại PyCharm và đảm bảo bạn đang dùng đúng môi trường ảo
Vào File → Settings → Project: [Tên project] → Python Interpreter

Đảm bảo Python interpreter là .venv\Scripts\python.exe của dự án bạn đang làm

🔹 Bước 3: Cài các thư viện mà YOLOv5 cần, vào đúng venv đó
✅ Cách 1: Dùng Terminal trong PyCharm
bash
Copy
Edit
cd đường_dẫn_đến_yolov5_main
pip install -r requirements.txt
Ví dụ:

bash
Copy
Edit
cd "C:\Users\PC\Downloads\yolov5-main"
pip install -r requirements.txt
💡 Câu lệnh trên sẽ cài các thư viện (như torch, opencv, matplotlib...) vào đúng venv của PyCharm nếu bạn chạy trong Terminal của PyCharm.

📥 Tải model EAST:
Tải frozen_east_text_detection.pb tại:
🔗 https://github.com/opencv/opencv_extra/blob/master/testdata/dnn/download_models.py
hoặc trực tiếp:

📥 Download link (Google Drive)