# 🔐 Face Recognition Security System

An intelligent security system using facial recognition that detects unknown faces and sends instant email alerts with a photo and video. Built with Python, OpenCV, and SMTP for real-time protection.

---

## 🎯 Purpose

This project helps automate surveillance and improve safety in:

- Homes  
- Offices  
- Labs  
- Classrooms  

It uses machine learning to recognize faces and alert when unfamiliar ones appear.

---

## 🚀 Key Features

- ✅ Real-time face detection and recognition  
- 📸 Captures intruder photo (`thief.jpg`) and video (`outpy.avi`)  
- 📧 Sends email alerts with attachments  
- 🔁 Easy to train with your face samples  
- 🖥️ Command-line interface (GUI optional)

---

## 🧠 How It Works

1. **Capture faces** using `face_dataset.py`  
2. **Train the system** with `training.py`  
3. **Run detection** using `face reco.py`  
4. If an unrecognized face appears, the system:
   - Captures the image and video  
   - Sends them via email to the configured address

---

## 🛠️ Technologies Used

- Python  
- OpenCV  
- LBPH Algorithm  
- Haar Cascades  
- SMTP (for Email Alerts)  
- (Optional) Tkinter GUI

---

## 📂 Project Files Overview

| File / Folder                   | Purpose                                 |
|--------------------------------|-----------------------------------------|
| `face_dataset.py`              | Capture face samples from webcam        |
| `training.py`                  | Train the recognition model             |
| `face reco.py`                 | Real-time detection and email alerts    |
| `cam_test.py`                  | Test if webcam works                    |
| `graw.py`                      | Extra feature: Yawn/blink detection     |
| `dataset/`                     | Stores captured face images             |
| `trainer.yml`                  | Trained LBPH face recognizer            |
| `haarcascade_frontalface_default.xml` | Face detection model              |

---

## 📧 Email Alert System

- Detects unknown faces  
- Captures `thief.jpg` and `outpy.avi`  
- Emails the attachments using your SMTP config  
- Works with Gmail, Outlook, etc.

---

## 🧪 Step-by-Step Usage

1. Run: `python face_dataset.py`  
2. Run: `python training.py`  
3. Run: `python face reco.py`  
4. Check output files and email inbox

---

## 🔭 Future Improvements

- GUI with Tkinter or PyQt  
- OTP security before alerts  
- Arduino siren integration  
- Raspberry Pi deployment

---

## 👨‍💻 Developer

**Ravichandra Pathi**  
🎓 B.Tech CSE, Universal College of Engineering  
🌐 [Portfolio Website](https://ravichandra-5859.github.io/portfolio/)  
📩 projectyear444@gmail.com  

---

## 🤝 Contributions Welcome

Feel free to fork this repo, suggest improvements, or raise issues!
