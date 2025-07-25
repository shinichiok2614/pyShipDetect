import torch
import cv2
import numpy as np

# Load YOLOv5 model (pre-trained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Khởi động webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)
    boxes = results.xyxy[0].cpu().numpy()

    # Duyệt qua tất cả các object đã nhận diện
    ship_crop = None
    for *xyxy, conf, cls in boxes:
        label = results.names[int(cls)]
        if label == 'boat':  # hoặc 'ship' nếu bạn huấn luyện mô hình riêng
            x1, y1, x2, y2 = map(int, xyxy)
            ship_crop = frame[y1:y2, x1:x2].copy()
            # Vẽ khung bao quanh tàu
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            break  # chỉ lấy 1 tàu đầu tiên

    # Hiển thị ảnh webcam chính
    cv2.imshow("YOLOv5 Ship Detection", frame)

    # Nếu có tàu, hiển thị vùng cắt riêng ở cửa sổ bên cạnh
    if ship_crop is not None:
        ship_crop_resized = cv2.resize(ship_crop, (300, 300))
        cv2.imshow("Cropped Ship", ship_crop_resized)
    else:
        # Nếu không phát hiện tàu, tạo hình trống
        blank = np.zeros((300, 300, 3), dtype=np.uint8)
        cv2.putText(blank, "No ship detected", (30, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow("Cropped Ship", blank)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
