# face-recognition-security-system
A real-time face recognition and alert system using Python, OpenCV, and SMTP
Face Recognition Security System
A smart security system that uses a webcam to detect and recognize human faces. It automatically sends an alert with a photo and video if an unknown person is detected — all in real time.
🎯 Purpose
This project helps automate basic surveillance using facial recognition. It can be used in:
- Offices
- Homes
- Labs
- Classrooms
It enhances security by combining AI-powered face detection with instant email alerts.
🚀 Key Features
✅ Detects known and unknown faces in real time
✅ Captures a photo (thief.jpg) and video (outpy.avi) of intruders
✅ Sends email alerts instantly with attachments
✅ Built with Python and OpenCV (works on any computer with a webcam)
✅ Easy to train the system with your own face
🧠 How It Works (In Simple Terms)
1. Collect faces: The system takes pictures of a person's face using a webcam
2. Train the system: It learns to recognize those faces
3. Run the system: If it sees an unknown face, it captures a photo & video
4. Send alerts: It emails those files to a configured address
🖥️ Technologies Used
• Python
• OpenCV
• LBPH
• SMTP
• (Optional) Tkinter for GUI
📂 Project Files
File Name	Description
face_dataset.py	Collect face samples from webcam
training.py	Train recognition model
face reco.py	Detect faces and send alerts
cam_test.py	Check if your camera works
graw.py	Yawn/Blink detection (extra)
haarcascade_frontalface_default.xml	Face detection model
trainer.yml	Trained model (auto-generated)
dataset/	Your face images
📸 Screenshots
Add images like:
- Webcam face capture
- Alert email screenshot
- Saved images folder
🧪 How To Use
1. Collect Face Data
   python face_dataset.py
2. Train the System
   python training.py
3. Start the System
   python face reco.py
📩 Email Alert Details
- Sent using Gmail (or any SMTP)
- You can configure sender and receiver emails in the script
- Attachments: thief.jpg and outpy.avi
🛠️ Future Improvements
• GUI interface
• OTP-based email alerts
• Arduino-based alarm
• Raspberry Pi deployment
👤 About the Developer
Ravichandra Pathi
B.Tech (CSE) – Universal College of Engineering
Passionate about ML, Security & Python Development
📧 projectyear444@gmail.com
🌐 https://ravichandra-5859.github.io/portfolio/
🤝 Contributions Welcome
If you're a developer, feel free to fork the project, improve it, or collaborate!
