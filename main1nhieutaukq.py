import torch
import cv2
import numpy as np

def center_pad_thumbnail(image, size=200):
    h, w = image.shape[:2]
    scale = min(size / w, size / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized = cv2.resize(image, (new_w, new_h))
    canvas = np.zeros((size, size, 3), dtype=np.uint8)
    top = (size - new_h) // 2
    left = (size - new_w) // 2
    canvas[top:top+new_h, left:left+new_w] = resized
    return canvas

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Đọc video từ ổ E
cap = cv2.VideoCapture('E:/haiquanvn.mp4')  # hoặc 0 nếu là webcam

if not cap.isOpened():
    print("Không thể mở video")
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
        if label == 'boat':
            x1, y1, x2, y2 = map(int, xyxy)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            ship_crop = frame[y1:y2, x1:x2].copy()
            thumb = center_pad_thumbnail(ship_crop, size=200)
            thumbnails.append(thumb)

    # Hiển thị video chính
    cv2.imshow("YOLOv5 Ship Detection", frame)

    # Hiển thị tàu đã cắt trong các ô 200x200
    if thumbnails:
        combined = cv2.vconcat(thumbnails)
        cv2.imshow("Detected Ships", combined)
    else:
        blank = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.putText(blank, "No ship", (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow("Detected Ships", blank)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
