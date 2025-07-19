
# 🖱️ Virtual Mouse with Voice Assistant and Gesture Recognition

This project enables users to control a computer mouse using **hand gestures** and perform various system actions through **voice commands**. Built using Python, OpenCV, and speech recognition libraries, this tool enhances accessibility and enables hands-free interaction with your system.

---

## 🔧 Features

- 👋 **Gesture Recognition**  
  - Move cursor using hand tracking  
  - Perform left-click, right-click, double-click  
  - Scroll and screen positioning

- 🎙️ **Voice Assistant Integration**  
  - Open apps (Notepad, browser, etc.)  
  - Tell jokes, show weather, give news updates  
  - System control via speech commands

- 🧠 **Computer Vision + NLP combo**  
  - Real-time webcam feed analysis  
  - Voice command recognition using Google API

---

## 🧠 Technologies Used

- Python 3.7+
- OpenCV
- NumPy
- PyAutoGUI
- SpeechRecognition
- pyttsx3
- Google Speech API
- Windows OS

---

## 📁 Project Structure

```
├──src
  ├── Gesture_Controller.py       # Hand tracking & virtual mouse control
  ├── Voice_Assistant.py          # Voice-based command executor
  ├── app.py                      # ChatBot script/UI interaction
  ├── calib_images/               # Camera calibration files (checkerboard)
  ├── requirements.txt            # Required Python packages
└── README.md                   # This file
```

---

## 🧪 Setup Instructions (Windows)

### 1. Clone the Repository
```bash
git clone https://github.com/hrushireddy/virtual-mouse-voice
cd virtual-mouse-voice
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:
```bash
pip install opencv-python pyttsx3 SpeechRecognition pyautogui numpy
```

### 3. Run the Application
```bash
python Voice_Assistant.py
```

Make sure your **webcam and microphone** are enabled and functional.

> To exit the webcam stream, press `q` in the OpenCV window.

---

## 🎯 Use Cases

- Accessibility for users with limited mobility
- Hands-free interaction for hygienic environments
- Smart automation demo for academic projects

---

## 🔮 Future Improvements

- Add more complex gesture patterns
- Improve gesture stability with MediaPipe
- Build GUI for feedback and status display
- Add multi-language voice support
- Enable browser automation and email features

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and share it with attribution.

---

## 👨‍💻 Author

**Mareddi Hrushikesh Reddy**  
B.Tech CSE Student | Python & AI Enthusiast | Open Source Explorer  
🔗 GitHub: [@hrushireddy](https://github.com/hrushireddy)  
🔗 LinkedIn: [Hrushikesh Mareddi](https://www.linkedin.com/in/hrushikesh-mareddi-095952281/)

---

> If you like this project, feel free to ⭐ the repo or fork it!
