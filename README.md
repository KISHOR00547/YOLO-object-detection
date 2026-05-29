
# Real-Time Object Detection on Raspberry Pi 5 using YOLOv8

## Overview

This project implements a real-time object detection system on a Raspberry Pi 5 using the YOLOv8 deep learning model. The system captures live video from a Raspberry Pi Camera Module 2 and performs object detection on each frame, displaying bounding boxes and class labels in real time.

The project demonstrates the deployment of AI-based computer vision applications on resource-constrained edge devices.

---

## Features

* Real-time object detection using YOLOv8n
* Live video capture using Raspberry Pi Camera Module 2
* CPU-based inference on Raspberry Pi 5
* Bounding box and class label visualization
* Optimized image processing pipeline
* Lightweight deployment suitable for edge AI applications

---

## Hardware Used

* Raspberry Pi 5
* Raspberry Pi Camera Module 2
* MicroSD Card (Raspberry Pi OS)
* Power Supply

---

## Software & Libraries

* Python 3
* OpenCV
* PyTorch
* Ultralytics YOLOv8
* Picamera2
* NumPy

---

## Project Architecture

```text
Raspberry Pi Camera
          │
          ▼
     Picamera2
          │
          ▼
   Frame Acquisition
          │
          ▼
 Image Preprocessing
          │
          ▼
      YOLOv8n
   Object Detection
          │
          ▼
 Bounding Boxes &
    Class Labels
          │
          ▼
   Live Display Window
```

---


The camera feed will open in a live window displaying:

* Detected object labels
* Confidence scores
* Bounding boxes

---

## Challenges Faced

* Python package dependency conflicts
* Virtual environment configuration
* Raspberry Pi camera integration issues
* Image format conversion (RGBA → RGB)
* YOLO model compatibility and setup
* Network interruptions during remote development

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Computer Vision
* Deep Learning Inference
* Embedded Linux Development
* Edge AI Deployment
* Raspberry Pi Development
* Python Environment Management
* Real-Time Debugging and Problem Solving

---

## Future Improvements

* Custom YOLOv8 model training
* Object counting system
* Person detection and tracking
* Edge AI optimization using TensorRT/OpenVINO
* Smart surveillance applications
* Industrial monitoring solutions




⭐ If you found this project useful, consider giving it a star on GitHub.


