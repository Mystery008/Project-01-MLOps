# 🚗 Vehicle Insurance Cross-Sell Prediction – End-to-End MLOps Project

## 📌 Overview

This project implements a complete **MLOps pipeline** for predicting whether existing vehicle insurance customers are interested in purchasing a health insurance policy.

The solution follows industry-standard MLOps practices including **data ingestion from MongoDB Atlas, automated training pipelines, model evaluation, AWS S3 model registry, FastAPI deployment, Docker containerization, and CI/CD automation using GitHub Actions and AWS services.**

---

## 🎯 Business Problem

Insurance companies often target existing customers with additional insurance products. This project predicts whether a customer is likely to respond positively to a health insurance offer based on demographic and vehicle-related information.

---

## 🚀 Key Features

* End-to-End Training Pipeline
* MongoDB Atlas Data Ingestion
* Schema-Based Data Validation
* Data Transformation & Feature Engineering
* Class Imbalance Handling using SMOTEENN
* Random Forest Model Training
* Model Evaluation Against Production Model
* AWS S3 Model Registry
* FastAPI Prediction Application
* Docker Containerization
* GitHub Actions CI/CD Pipeline
* AWS ECR & EC2 Deployment
* Structured Logging & Exception Handling

---

## 🏗️ Architecture

```text
MongoDB Atlas
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
AWS S3 Model Registry
      │
      ▼
Prediction Pipeline
      │
      ▼
FastAPI Application
      │
      ▼
Docker
      │
      ▼
AWS ECR
      │
      ▼
AWS EC2
```

---

## 🛠️ Tech Stack

| Category         | Technologies                   |
| ---------------- | ------------------------------ |
| Programming      | Python 3.10                    |
| Machine Learning | Scikit-Learn, Imbalanced-Learn |
| Data Processing  | Pandas, NumPy                  |
| Database         | MongoDB Atlas                  |
| Backend          | FastAPI, Jinja2                |
| Cloud            | AWS S3, EC2, ECR, IAM          |
| DevOps           | Docker, GitHub Actions         |
| Utilities        | Boto3, Dill, PyYAML            |

---

## 📂 Project Workflow

### 1️⃣ Data Ingestion

* Connects to MongoDB Atlas
* Extracts insurance data
* Creates train/test datasets

### 2️⃣ Data Validation

* Schema validation
* Missing column checks
* Data consistency verification

### 3️⃣ Data Transformation

* Feature encoding
* Feature scaling
* SMOTEENN balancing
* Preprocessing pipeline creation

### 4️⃣ Model Training

* Random Forest Classifier
* Performance evaluation
* Model serialization

### 5️⃣ Model Evaluation

* Compare with production model
* F1-score based acceptance criteria

### 6️⃣ Model Deployment

* Upload best model to AWS S3
* Serve predictions through FastAPI

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Project-01-MLOps.git
cd Project-01-MLOps
```

### Create Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
MONGODB_URL=your_mongodb_connection_string

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
```

---

## 🚀 Run Application

### Start FastAPI Server

```bash
python app.py
```

Application URL:

```text
http://localhost:5000
```

---

## 🐳 Docker

### Build Image

```bash
docker build -t vehicle-insurance-mlops .
```

### Run Container

```bash
docker run -p 5000:5000 vehicle-insurance-mlops
```

---

## 🔄 CI/CD Pipeline

Implemented using **GitHub Actions**.

### Continuous Integration

* Checkout Source Code
* Build Docker Image
* Push Image to AWS ECR

### Continuous Deployment

* Pull Latest Image on EC2
* Run Docker Container
* Deploy Updated Application

---

## ☁️ AWS Services Used

* **AWS S3** – Model Registry
* **AWS ECR** – Docker Image Repository
* **AWS EC2** – Application Hosting
* **AWS IAM** – Access Management

---

## 📊 Dataset Features

* Gender
* Age
* Driving License
* Region Code
* Previously Insured
* Vehicle Age
* Vehicle Damage
* Annual Premium
* Policy Sales Channel
* Vintage

**Target Variable:** `Response`

---

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

* MLOps Pipeline Development
* Machine Learning Model Lifecycle
* MongoDB Integration
* AWS Cloud Services
* Docker Containerization
* CI/CD Automation
* FastAPI Deployment
* Production-Ready ML Systems
