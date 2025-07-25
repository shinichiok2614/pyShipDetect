import cv2
import numpy as np
import pytesseract
import torch

# Đường dẫn đến tesseract.exe (sửa nếu bạn cài ở chỗ khác)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Tải mô hình YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Đọc video từ ổ E (đổi nếu cần)
cap = cv2.VideoCapture("E:/haiquanvn.mp4")

# Hàm tạo thumbnail căn giữa trong khung vuông 200x200
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

if not cap.isOpened():
    print("Không thể mở video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)
    boxes = results.xyxy[0].cpu().numpy()

    thumbnails = []

    for i, (*xyxy, conf, cls) in enumerate(boxes, start=1):
        label = results.names[int(cls)]
        if label == 'boat':
            x1, y1, x2, y2 = map(int, xyxy)

            # Vẽ khung và nhãn
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Vẽ "boat" (xanh) và số thứ tự (vàng) trên cùng 1 dòng
            base_label = "boat "
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.9
            thickness = 2
            org = (x1, y1 - 10)

            # Boat label màu xanh
            cv2.putText(frame, base_label, org, font, font_scale, (0, 255, 0), thickness)

            # Tính độ rộng của 'boat ' để đặt số ngay sau
            (text_width, _), _ = cv2.getTextSize(base_label, font, font_scale, thickness)
            number_org = (x1 + text_width, y1 - 10)
            cv2.putText(frame, f"#{i}", number_org, font, font_scale, (0, 255, 255), thickness)

            # Cắt ảnh tàu
            ship_crop = frame[y1:y2, x1:x2].copy()

            # OCR chữ/số trên thân tàu
            gray_crop = cv2.cvtColor(ship_crop, cv2.COLOR_BGR2GRAY)
            ocr_text = pytesseract.image_to_string(gray_crop, config='--psm 6').strip()

            if ocr_text:
                # Ghi OCR dưới khung tàu (màu vàng nhạt)
                cv2.putText(frame, ocr_text, (x1, y2 + 25),
                            font, 0.7, (255, 255, 0), 2, cv2.LINE_AA)

            # Tạo thumbnail 200x200, thêm số thứ tự (màu vàng)
            thumb = center_pad_thumbnail(ship_crop)
            cv2.putText(thumb, str(i), (10, 30), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

            thumbnails.append(thumb)

    # Hiển thị khung chính
    cv2.imshow("YOLOv5 Ship Detection", frame)

    # Hiển thị thumbnail
    if thumbnails:
        combined = cv2.vconcat(thumbnails)
    else:
        combined = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.putText(combined, "No ship", (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Detected Ships", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
