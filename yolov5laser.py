import serial
import time
import torch
import cv2

# Initialize serial communication with the Arduino
arduinoData = serial.Serial('com13', 9600)  # Change this based on your serial port

def send_coordinates_to_arduino(x, y, w, h):
    """Send the coordinates of the detected object to the Arduino."""
    coordinates = f"{x},{y}\r"
    arduinoData.write(coordinates.encode())
    print(f"Sent to Arduino: X{x} Y{y}")

# Load YOLOv5 model
model_yolov5 = torch.hub.load('yolov5', 'custom', path='yolov5s.pt', source='local')
model_yolov5.iou = 0.45  # Set IoU threshold
model_yolov5.conf = 0.5  # Set confidence threshold

# Initialize video capture with the appropriate camera index (0 for the internal laptop camera, 1 for an external webcam)
capture = cv2.VideoCapture(0)
try:
    while True:
        ret, frame = capture.read()

        if not ret:
            print("can not open camera")
            break
        time.sleep(0.1)
        # 使用YOLOv5
        results = model_yolov5(frame)

        #(COCO 0: 'person')
        for *xyxy, conf, cls in results.xyxy[0]:
            if int(cls) == 77:  # 只保留 'person'
                x1, y1, x2, y2 = map(int, xyxy)
                w, h = x2 - x1, y2 - y1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                send_coordinates_to_arduino(x1, y1, w, h)
                

       
        cv2.imshow('Video', frame)

        
        if cv2.waitKey(20) & 0xFF == ord('d'):
            break
finally:
    capture.release()
    cv2.destroyAllWindows()
    if arduinoData.is_open:
        arduinoData.close()
        print("串行通信端口已关闭")
