# ✋ Hand Gesture Recognition

A real-time AI-powered Hand Gesture Recognition system that detects and classifies hand gestures using a webcam. Built with MediaPipe Hand Tracking and OpenCV, this project can recognize multiple gestures and perform actions based on finger positions.

---

## ✨ Features

* 🤖 Real-Time Hand Tracking
* ✋ Detects Single & Multiple Hands
* 👍 Thumbs Up Detection
* 👎 Thumbs Down Detection
* 😎 Swag Gesture Detection
* ✌️ Peace Sign Detection
* ☝️ Pointing Finger Detection
* 🖐️ Open Hand Detection
* 👌 OK Gesture Detection
* ✊ Fist Detection
* 🚪 Exit Using Both Hands Open (10 Fingers)
* 📷 Live Webcam Feed
* ⚡ Fast & Lightweight Processing

---

## 🎮 Supported Gestures

| Gesture            | Description               |
| ------------------ | ------------------------- |
| 👍 Thumbs Up       | Positive Gesture          |
| 👎 Thumbs Down     | Negative Gesture          |
| 😎 Swag            | Index + Pinky Finger      |
| ✊ Fist             | All Fingers Closed        |
| ✌️ Peace Sign      | Index + Middle Finger     |
| ☝️ Pointing Finger | Index Finger Only         |
| 🖐️ Open Hand      | All Fingers Open          |
| 👌 OK              | Thumb & Index Form Circle |
| ✋ Two Hands        | Both Hands Detected       |

---

## 📂 Project Structure

```text
Hand-Gesture-Recognition/
├── hand_gesture_recognition.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Tech Stack

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| Python          | Core Programming          |
| OpenCV          | Webcam & Image Processing |
| MediaPipe Hands | AI Hand Tracking          |
| Math Module     | Gesture Calculations      |

---

## 📦 Installation

### Clone Repository

```bash
https://github.com/codertheashish/Hand-Gesture-Recognition

```

### Install Dependencies

```bash
pip install opencv-python mediapipe
```

---

## ▶️ How to Run

```bash
python hand_gesture_recognition.py
```

A webcam window will open and start detecting gestures in real time.

---

## 🚪 Exit Control

Show **both hands fully open (10 fingers)** to automatically exit the application.

OR

Press:

```text
Q
```

to quit manually.

---

## 🧠 How It Works

1. MediaPipe detects hand landmarks (21 key points).
2. Finger positions are analyzed.
3. Landmark distances and angles are calculated.
4. Finger states (open/closed) are determined.
5. Gestures are classified based on finger combinations.
6. The detected gesture is displayed on the webcam feed.

---

## 🔮 Future Enhancements

* More Gesture Support
* Volume Control Using Gestures
* Brightness Control
* Virtual Mouse
* Gesture-Based Presentation Control
* Sign Language Recognition
* Custom Gesture Training

---

## 📸 Screenshot

```markdown
![Project Screenshot](screenshot.png)
```

---

## 📄 License

Released under the MIT License.

---

## 👨‍💻 Author

**Ashish Kumar Prajapati**

* GitHub: https://github.com/codertheashish
* Email: [codertheashish@gmail.com](mailto:codertheashish@gmail.com)

---

⭐ If you like this project, give it a star on GitHub.
