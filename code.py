from ultralytics import YOLO
from picamera2 import Picamera2
import cv2
import time

model = YOLO("yolov8n.pt")

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (480, 360)}
)

picam2.configure(config)
picam2.start()

time.sleep(2)

cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLO", 900, 700)

while True:
    frame = picam2.capture_array()

    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

    results = model(
        frame,
        imgsz=320,
        verbose=False,
        device="cpu"
    )

    annotated = results[0].plot()

    cv2.imshow("YOLO", annotated)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
