# 🌸 Flower Species Classification (Iris Dataset)

A Machine Learning web application that predicts the species of a flower using the famous **Iris dataset**.
The model takes sepal and petal measurements as input and classifies the flower into one of three categories: **Setosa, Versicolor, or Virginica**.

---

# 🔗 **Live Demo:** [https://flower-species-classification.onrender.com/](https://flower-species-classification.onrender.com/)

> ⚠️ Note: The app may take some time to open on first visit because the hosting service automatically downloads required model files in the background (cold start).

---

## 📖 Overview

This project demonstrates an end‑to‑end Machine Learning workflow:

* Data preprocessing
* Model training
* Model serialization
* Backend API creation
* Web interface integration
* Cloud deployment

The goal is to provide a simple yet practical example of how a trained ML model can be served to users through a web application.

---

## ✨ Features

* Predicts flower species from user input measurements
* Clean and simple web UI
* Fast prediction using trained ML model
* Deployed online using cloud hosting
* Beginner‑friendly project structure
* Demonstrates real ML model deployment pipeline

---

## 🧠 Machine Learning Details

### Dataset

The project uses the **Iris Dataset**, one of the most popular datasets in machine learning.

It contains 150 samples with 4 features:

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

Target Classes:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

### Model Workflow

1. Load dataset
2. Preprocess features
3. Train classification model
4. Evaluate performance
5. Save model using serialization
6. Serve predictions through API

---

## 🛠 Tech Stack

**Machine Learning**

* Python
* Scikit‑learn
* NumPy
* Pandas

**Backend**

* FastAPI / Flask (depending on implementation)
* Uvicorn server

**Frontend**

* HTML
* CSS
* JavaScript

**Deployment**

* Render Cloud Platform

---

## 📂 Project Structure

```
Flower-Species-Classification/
│
├── model/                # Saved trained model
├── static/               # CSS & frontend assets
├── templates/            # HTML pages
├── main.py / app.py      # Backend server
├── train_model.py        # Model training script
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🚀 Installation & Setup (Local Run)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Anukul-Chandra/Flower-Species-Classification.git
cd Flower-Species-Classification
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
uvicorn main:app --reload
```

Now open:

```
http://127.0.0.1:8000
```

---

## 🧪 How Prediction Works

1. User enters flower measurements
2. Data is sent to backend API
3. Model processes input
4. Predicted species returned
5. Result displayed on webpage

---

## 🌍 Deployment

The project is deployed on **Render**.

Steps followed:

1. Push code to GitHub
2. Connect GitHub repository to Render
3. Install dependencies automatically
4. Start backend server
5. Host public prediction service

---

## 📊 Example Input

| Feature      | Value |
| ------------ | ----- |
| Sepal Length | 5.1   |
| Sepal Width  | 3.5   |
| Petal Length | 1.4   |
| Petal Width  | 0.2   |

**Prediction → Iris Setosa**

---

## 🔮 Future Improvements

* Add probability confidence score
* Add dataset visualization graphs
* Add REST API endpoint documentation
* Improve UI design
* Support batch predictions
* Docker containerization

---

## 👨‍💻 Author

**Anukul Chandra**

---

## 📜 License

This project is open source and available under the MIT License.
