# 🚗 Vehicle Insurance Prediction MLOps Pipeline

An end-to-end Machine Learning Operations (MLOps) project for Vehicle Insurance Prediction, demonstrating the complete lifecycle of a production-ready ML system—from data ingestion and validation to model training, deployment, and CI/CD automation using AWS and Docker.

This project showcases industry-standard MLOps practices including MongoDB integration, modular pipeline architecture, model versioning, cloud deployment, and automated CI/CD workflows.

---

## 📌 Project Overview

The objective of this project is to build a scalable and production-ready machine learning pipeline that predicts whether a customer is likely to purchase vehicle insurance based on demographic and vehicle-related attributes.

The project follows a complete MLOps workflow:

```text
Data Ingestion
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Deployment
      ↓
Prediction API
      ↓
CI/CD Automation
```

---

## 🚀 Features

* End-to-End MLOps Pipeline
* MongoDB Atlas Integration
* Automated Data Validation
* Feature Engineering & Transformation
* Machine Learning Model Training
* Model Evaluation & Versioning
* AWS S3 Model Storage
* FastAPI Prediction Service
* Docker Containerization
* GitHub Actions CI/CD Pipeline
* AWS EC2 Deployment
* Modular and Scalable Architecture
* Logging and Exception Handling

---

## 🛠️ Tech Stack

### Programming

* Python 3.10

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Database

* MongoDB Atlas

### Backend

* FastAPI

### Cloud Services

* AWS S3
* AWS EC2
* AWS ECR
* IAM

### DevOps

* Docker
* GitHub Actions

### Utilities

* Logging
* YAML Configuration
* Custom Exception Handling

---

## 📂 Project Structure

```bash
Vehicle-Insurance-MLops/
│
├── notebook/
│   ├── EDA.ipynb
│   ├── Feature_Engineering.ipynb
│   └── mongoDB_demo.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   │
│   ├── configuration/
│   ├── entity/
│   ├── utils/
│   ├── aws_storage/
│   └── pipeline/
│
├── templates/
├── static/
├── logs/
├── app.py
├── requirements.txt
├── setup.py
├── pyproject.toml
├── Dockerfile
└── .github/workflows/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/vehicle-insurance-mlops.git

cd vehicle-insurance-mlops
```

### Create Virtual Environment

```bash
conda create -n vehicle python=3.10 -y

conda activate vehicle
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

## 🗄️ MongoDB Setup

### Create MongoDB Atlas Cluster

1. Create a MongoDB Atlas account
2. Create a new project
3. Create an M0 free cluster
4. Create database user credentials
5. Allow network access from:

```text
0.0.0.0/0
```

6. Copy the MongoDB connection string

Example:

```text
mongodb+srv://username:password@cluster.mongodb.net/
```

---

## 🔑 Environment Variables

### MongoDB

#### Linux/Mac

```bash
export MONGODB_URL="mongodb+srv://username:password@cluster.mongodb.net/"
```

#### Windows PowerShell

```powershell
$env:MONGODB_URL="mongodb+srv://username:password@cluster.mongodb.net/"
```

---

## 📊 Data Ingestion

The ingestion pipeline fetches data from MongoDB Atlas and stores it locally for further processing.

### Responsibilities

* Establish MongoDB Connection
* Extract Data
* Convert to DataFrame
* Store Raw Dataset
* Generate Ingestion Artifacts

---

## ✅ Data Validation

Validation checks include:

* Schema Validation
* Missing Values Detection
* Data Type Validation
* Column Consistency Verification
* Dataset Integrity Checks

Configuration is maintained in:

```text
config/schema.yaml
```

---

## 🔄 Data Transformation

Data preprocessing steps:

* Missing Value Handling
* Feature Encoding
* Scaling & Normalization
* Feature Engineering
* Pipeline Serialization

Artifacts generated:

```text
preprocessor.pkl
```

---

## 🤖 Model Training

Machine learning models are trained using transformed data.

### Training Workflow

* Data Splitting
* Model Training
* Hyperparameter Evaluation
* Performance Comparison
* Best Model Selection

Artifacts generated:

```text
model.pkl
```

---

## 📈 Model Evaluation

The trained model is compared with previously deployed models.

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1 Score

If performance improves:

✅ New model approved

Otherwise:

❌ Existing production model retained

---

## ☁️ AWS S3 Integration

Trained models are versioned and stored in AWS S3.

### Bucket Structure

```text
s3://vehicle-insurance-models/

├── model.pkl
├── preprocessor.pkl
└── metadata
```

---

## 🚀 Running the Application

Start the FastAPI server:

```bash
python app.py
```

or

```bash
uvicorn app:app --host 0.0.0.0 --port 5000
```

Open:

```text
http://localhost:5000
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t vehicle-insurance-app .
```

### Run Container

```bash
docker run -p 5000:5000 vehicle-insurance-app
```

---

## 🔄 CI/CD Pipeline

GitHub Actions automates:

* Code Build
* Docker Image Creation
* Push to AWS ECR
* Deploy to AWS EC2

### Required GitHub Secrets

```text
AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION

ECR_REPOSITORY
```

---

## ☁️ AWS Deployment Architecture

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
AWS ECR
   │
   ▼
AWS EC2
   │
   ▼
Docker Container
   │
   ▼
Prediction API
```

---

## 📚 Learning Outcomes

Through this project, the following MLOps concepts were implemented:

* Data Versioning
* Pipeline Architecture
* Model Lifecycle Management
* Cloud Storage
* CI/CD Automation
* Dockerization
* Production Deployment
* Monitoring-Ready Design
* Reproducible Machine Learning Workflows
