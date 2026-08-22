# Face Recognition Attendance System

An AI-based face recognition system designed to automate student attendance and reduce the time and effort required for manual attendance marking.

## 📌 Overview

Manual attendance can be time-consuming, especially in classrooms with a large number of students. It can also lead to human errors and make attendance records difficult to maintain.

This project explores the use of facial recognition to provide a faster and more efficient approach to attendance marking.

## 🎯 Problem Statement

School authorities spend considerable time marking attendance manually. The process can be tedious, time-consuming, and prone to errors.

The goal of this project was to develop a system that could identify students using facial recognition and use the identification result to assist with attendance marking.

## 💡 Solution

The system uses a webcam to capture faces and compares them with previously collected training data.

### How it works

1. The user faces the webcam.
2. The system captures and detects the face.
3. The detected face is compared with the trained faces.
4. The system identifies the person.
5. The identification result can then be used to record attendance.

## 🛠️ Technologies Used

* OpenCV
* dlib
* Visual Studio

## 🧪 Testing

The prototype was tested with selected Class XII students.

During testing, approximately **80% recognition success** was observed. The system was able to recognize students' faces, although changes such as different hairstyles and clothing could affect recognition.

### Testing Observations

**What worked:**

* The system could recognize a person's face when they stood in front of the camera.
* The identified person's name could be displayed.

**Limitations identified:**

* Face detection could be faster.
* Recognition could be affected by variations in appearance.

### Possible Improvements

* Use a larger and higher-quality training dataset.
* Improve face detection speed.
* Use more advanced recognition techniques.
* Periodically update the dataset.

## 🎥 Project Demo

A demonstration of the project is available below:

[View the project demo](./face-recognition-demo.mp4)

## 👩‍💻 My Contribution

I was primarily involved in the **technical development of the project**. I worked mostly on the face recognition code, helped develop and test the prototype, and contributed to improving the system based on testing observations.

I also handled the **video production and editing** for the final project presentation.

### Key Contributions

* Worked primarily on the face recognition implementation.
* Helped develop and test the prototype.
* Worked on the face detection and recognition workflow.
* Helped identify limitations during testing.
* Contributed to improving the prototype based on observations.
* Filmed and edited the final project demonstration.
* Collaborated with the team on project documentation and presentation.

## 🚀 Future Improvements

Future versions of the system could focus on:

* Improving recognition accuracy.
* Increasing face detection speed.
* Expanding and improving the training dataset.
* Handling greater variations in appearance and environmental conditions.
* Exploring more advanced face recognition techniques.

## 📚 Project Context

This project was developed as a **Class XII Artificial Intelligence project** focused on applying AI to a real-world school attendance problem.

The project involved problem identification, user research, brainstorming, solution design, data collection, prototyping, testing, and reflection.
