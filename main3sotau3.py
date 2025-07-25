import cv2
import numpy as np
import pytesseract

# Cấu hình pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_text_regions(image):
    # Resize ảnh (EAST yêu cầu chiều phải chia hết cho 32)
    orig = image.copy()
    (H, W) = image.shape[:2]
    newW, newH = (320, 320)
    rW, rH = W / float(newW), H / float(newH)

    image = cv2.resize(image, (newW, newH))
    blob = cv2.dnn.blobFromImage(image, 1.0, (newW, newH),
                                 (123.68, 116.78, 103.94), swapRB=True, crop=False)

    # Load EAST model
    net = cv2.dnn.readNet("frozen_east_text_detection.pb")  # cần tải về model này

    net.setInput(blob)
    (scores, geometry) = net.forward(["feature_fusion/Conv_7/Sigmoid",
                                      "feature_fusion/concat_3"])

    # Phân tích đầu ra để lấy bounding boxes
    (rects, confidences) = decode_predictions(scores, geometry, min_confidence=0.5)

    boxes = cv2.dnn.NMSBoxes(rects, confidences, 0.5, 0.4)

    results = []
    if len(boxes) > 0:
        for i in boxes.flatten():
            (startX, startY, endX, endY) = rects[i]
            # Scale về ảnh gốc
            startX = int(startX * rW)
            startY = int(startY * rH)
            endX = int(endX * rW)
            endY = int(endY * rH)

            # Cắt vùng nghi ngờ chứa chữ
            roi = orig[startY:endY, startX:endX]

            # OCR vùng này
            config = "--psm 7"  # 1 dòng chữ đơn
            text = pytesseract.image_to_string(roi, config=config).strip()

            if text:
                results.append((text, (startX, startY, endX, endY)))

    return results


def decode_predictions(scores, geometry, min_confidence):
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidences = []

    for y in range(0, numRows):
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]

        for x in range(0, numCols):
            if scoresData[x] < min_confidence:
                continue

            offsetX = x * 4.0
            offsetY = y * 4.0

            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)

            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]

            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)

            rects.append([startX, startY, endX, endY])
            confidences.append(float(scoresData[x]))

    return (rects, confidences)
