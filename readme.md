# Python Compilation Project

My personal Python learning codebase organized by topic. The goal is to build a clean collection of examples, notes, and small projects while learning Python, automation, computer vision, machine learning, augmented reality, and AI model integration.

## Learning Roadmap

1. Python basics
2. Automation
3. OpenCV camera basics
4. MediaPipe hand tracking
5. PyAutoGUI computer control
6. Machine learning basics
7. Augmented reality
8. AI model integration

## Current Folder Structure

```text
python github/
+-- Fundamentals/
+-- OOP/
+-- Automation/
+-- Libraries_and_Frameworks/
+-- OpenCV_Camera_Basics/
+-- MediaPipe_Hand_Tracking/
+-- PyAutoGUI_Computer_Control/
+-- Machine_Learning_Basics/
+-- Augmented_Reality/
+-- AI_Model_Integration/
+-- Playground/
+-- workflows/
+-- readme.md
```

## Topics

### Fundamentals

Basic Python learning files such as syntax, variables, conditionals, loops, functions, files, and beginner exercises.

### OOP

Object-oriented programming practice, including classes, objects, methods, inheritance, and simple OOP projects.

### Automation

Python scripts for automating tasks such as file creation, Excel work, repetitive actions, and workflow helpers.

### Libraries and Frameworks

Practice files for Python libraries and tools. Current example:

- Turtle

### OpenCV Camera Basics

Beginner computer vision lessons using `opencv-python`.

Current files:

```text
OpenCV_Camera_Basics/
+-- selfie_camera.py
+-- grayscale_camera.py
+-- draw_camera.py
+-- face_detection.py
```

Covered concepts:

- Opening the webcam with `cv2.VideoCapture(0)`
- Reading frames from the camera
- Flipping the camera view
- Showing the camera window with `cv2.imshow()`
- Detecting keyboard input with `cv2.waitKey()`
- Saving images with `cv2.imwrite()`
- Drawing rectangles, circles, lines, and text
- Basic face detection using Haar cascades

Install OpenCV:

```bash
pip install opencv-python
```

Run an OpenCV file:

```bash
python OpenCV_Camera_Basics/face_detection.py
```

### MediaPipe Hand Tracking

Future folder for hand tracking, hand landmarks, gesture detection, and camera-based controls.

### PyAutoGUI Computer Control

Future folder for controlling the mouse, keyboard, screenshots, and computer automation with Python.

### Machine Learning Basics

Future folder for NumPy, Pandas, Matplotlib, Scikit-learn, regression, classification, and model evaluation.

### Augmented Reality

Future folder for camera overlays, AR effects, markers, filters, and object placement on video frames.

### AI Model Integration

Future folder for connecting Python projects to AI models, APIs, chatbots, and local model experiments.

### Playground

Temporary experiments and quick test files. Useful code can be moved later into the correct topic folder.

## Suggested File Pattern

Each topic folder should use simple, clear filenames:

```text
topic_folder/
+-- notes.md
+-- example_01.py
+-- example_02.py
+-- mini_project.py
```

Each Python file should start with a short comment or docstring:

```python
"""
Topic: OpenCV Face Detection
Goal: Detect faces from the webcam and draw a box around each face.
Library: opencv-python
"""
```

## Common Commands

Run a Python file:

```bash
python path/to/file.py
```

Install a library:

```bash
pip install library-name
```

Check installed OpenCV version:

```bash
python -c "import cv2; print(cv2.__version__)"
```
