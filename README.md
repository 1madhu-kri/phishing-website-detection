HEAD
# Phishing Website Detection System

## Overview

The **Phishing Website Detection System** is a Machine Learning-based web application that predicts whether a website is **phishing** or **legitimate** based on various website security features.

The project is developed using **Python**, **Scikit-learn**, and **Streamlit**, providing real-time phishing detection through an interactive user interface.

The system was trained and evaluated using multiple machine learning algorithms:

- Random Forest
- Logistic Regression
- Decision Tree

Among these models, **Random Forest** achieved the highest accuracy and was selected for deployment.

---

## Features

- Detect phishing websites using Machine Learning
- Interactive web application built with Streamlit
- Real-time prediction
- Confidence score display
- Feature-based website analysis
- User-friendly interface

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## Project Structure

```bash
ML-PROJECT/
│
├── Models/
│   ├── app_url.py
│   ├── random_forest.joblib
│   ├── requirements.txt
│   ├── README.md
│   └── email.csv
│
├── notebook/
│   ├── data.ipynb
│   ├── model_training.ipynb
│   └── saved_models.ipynb
│
└── dataset1.csv
```

---

## Dataset

The dataset contains several website-related features used to identify phishing websites, including:

- Having IP Address
- URL Length
- Shortening Service
- Having @ Symbol
- SSL Final State
- Prefix Suffix
- Domain Registration Length
- HTTPS Token

### Target Variable

| Value | Meaning            |
| ----- | ------------------ |
| 1     | Legitimate Website |
| -1    | Phishing Website   |

---

## Model Performance

| Model               | Performance       |
| ------------------- | ----------------- |
| Random Forest       | Best Accuracy     |
| Logistic Regression | Good Accuracy     |
| Decision Tree       | Moderate Accuracy |

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/phishing-website-detection.git
cd phishing-website-detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app_url.py
```

---
[🚀 Live Demo](https://phishing-website-detection-my.streamlit.app/)
## Screenshots

Add screenshots of:

- Home Page
- Prediction Result
- Accuracy Comparison Graph
- Feature Importance Graph

---

## Future Improvements

- Automatic URL feature extraction
- Real-time website scanning
- Cloud deployment
- Enhanced UI/UX
- Deep Learning integration
- Browser extension support

---

## Authors

**Madhu Kumari**
**Yuthika**

---

## License

This project is developed for educational and research purposes.
=======
# phishing-website-detection
A Streamlit web application that detects phishing websites using Machine Learning models such as Random Forest, Logistic Regression, and Decision Tree.
9e4e1a446414518f1f30ec165d2a0b9b8d4c004c
