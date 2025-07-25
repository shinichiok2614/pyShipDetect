import torch
import cv2

# Load YOLOv5 pre-trained model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Mở webcam
cap = cv2.VideoCapture(0)  # 0 là webcam mặc định

if not cap.isOpened():
    print("Không thể mở webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Chuyển đổi BGR -> RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Nhận diện với mô hình
    results = model(img_rgb)

    # Vẽ kết quả lên ảnh
    annotated_frame = results.render()[0]

    # Hiển thị
    cv2.imshow('YOLOv5 Ship Detection (Webcam)', annotated_frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dọn dẹp
cap.release()
cv2.destroyAllWindows()
