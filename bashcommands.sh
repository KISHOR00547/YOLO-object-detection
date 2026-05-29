

### setup.sh

Use this once to install dependencies:

```bash
#!/bin/bash

python3 -m venv yolo_env
source yolo_env/bin/activate

pip install --upgrade pip
pip install ultralytics
pip install torch torchvision
pip install opencv-python
pip install picamera2

echo "Setup Complete!"
```

Make it executable:

```bash
chmod +x setup.sh
```

Run:

```bash
./setup.sh
```

---

### run.sh

Use this to start your project:

```bash
#!/bin/bash

source yolo_env/bin/activate
python3 object_detection.py
```

Make it executable:

```bash
chmod +x run.sh
```

Run:

```bash
./run.sh
```
