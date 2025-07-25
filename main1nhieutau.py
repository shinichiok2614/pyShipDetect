import torch
import cv2
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Khởi động webcam
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('E:/haiquanvn.mp4')


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

    thumbnails = []

    for *xyxy, conf, cls in boxes:
        label = results.names[int(cls)]
        if label == 'boat':  # hoặc 'ship' nếu bạn huấn luyện mô hình riêng
            x1, y1, x2, y2 = map(int, xyxy)

            # Vẽ khung và nhãn lên ảnh gốc
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{label}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Cắt ảnh tàu
            ship_crop = frame[y1:y2, x1:x2].copy()

            # Resize thumbnail
            # thumb = cv2.resize(ship_crop, (200, 200))
            # Resize thumbnail giữ nguyên tỉ lệ theo chiều cao = 200px
            max_height = 200
            h, w = ship_crop.shape[:2]
            new_w = int(w * (max_height / h))
            thumb = cv2.resize(ship_crop, (new_w, max_height))

            thumbnails.append(thumb)

    # Hiển thị webcam chính
    cv2.imshow("YOLOv5 Ship Detection", frame)

    # Ghép các ảnh cắt thành một hàng ngang
    if thumbnails:
        # Nếu có nhiều ảnh -> ghép lại
        combined = cv2.hconcat(thumbnails)
        cv2.imshow("Detected Ships", combined)
    else:
        # Không có tàu nào
        blank = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.putText(blank, "No ship detected", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow("Detected Ships", blank)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dọn dẹp
cap.release()
cv2.destroyAllWindows()
