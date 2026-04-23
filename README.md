# CatsE 🐱

[![GitHub Stars](https://img.shields.io/github/stars/xjly1/CatsE?style=social)]()
[![GitHub Forks](https://img.shields.io/github/forks/xjly1/CatsE?style=social)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![WebGL](https://img.shields.io/badge/WebGL-Visuals-orange)]()

---

<img src="https://github.com/xjly1/CatsE/blob/main/assets/cat-disgust.jpeg" width="300">

## 🎯 Overview

**CatsE** is a real-time computer vision project built with **OpenCV + MediaPipe** that detects facial expressions through a webcam and maps them to fun TikTok-style cat reactions (Rigby, Larry, etc).

It tracks facial landmarks and uses lightweight geometric rules to detect:

- 😮 Shock (eye widening)
- 👅 Tongue (mouth opening)
- 😑 Glare (eye squinting)

Each detected expression triggers a corresponding cat reaction in real time.

---

## 🎬 Demo

![CatsE Demo](https://media.giphy.com/media/your-demo-link-here/giphy.gif)

> Replace this link with your real demo GIF (GitHub, Giphy, or Imgur)

---

## ⚙️ How it works

1. Webcam feed is captured using OpenCV  
2. MediaPipe Face Mesh extracts 468 facial landmarks  
3. Facial movements are analyzed using simple heuristics  
4. Expression state is detected in real time  
5. A matching cat reaction image is displayed instantly  

---

## 😺 Expression Mapping

| Expression | Trigger Condition |
|------------|------------------|
| Shock | Wide eye opening |
| Tongue | Mouth opening |
| Glare | Eye squinting |

---

## ✨ Features

- Real-time face tracking  
- 468 facial landmarks detection  
- Lightweight expression detection logic  
- Fun cat reaction system  
- Webcam-based interaction  

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/xjly1/CatsE.git
cd CatsE

```
### 2. Intall libraries
- Termial - New Terminal: pip install opencv-python mediapipe numpy Pillow