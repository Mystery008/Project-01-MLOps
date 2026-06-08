# 🚗 Vehicle Insurance Prediction – End-to-End MLOps Project

## 📌 Overview

This project implements a complete MLOps pipeline for predicting whether existing vehicle insurance customers are interested in purchasing a health insurance policy.

The solution follows industry-standard MLOps practices including data ingestion from MongoDB Atlas, automated training pipelines, model evaluation, AWS S3 model registry, FastAPI deployment, Docker containerization, and CI/CD automation using GitHub Actions and AWS services.

---

## 🎯 Business Problem

Insurance companies often target existing customers with additional insurance products. This project predicts whether a customer is likely to respond positively to a health insurance offer based on demographic and vehicle-related information.

---

## 🚀 Key Features

- End-to-End Training Pipeline
- MongoDB Atlas Data Ingestion
- Schema-Based Data Validation
- Data Transformation & Feature Engineering
- Class Imbalance Handling using SMOTEENN
- Random Forest Model Training
- Model Evaluation Against Production Model
- AWS S3 Model Registry
- FastAPI Prediction Application
- Docker Containerization
- GitHub Actions CI/CD Pipeline
- AWS ECR & EC2 Deployment
- Structured Logging & Exception Handling

---

## 🏗️ Architecture

```
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
Docker → AWS ECR → AWS EC2
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python 3.10 |
| Machine Learning | Scikit-Learn, Imbalanced-Learn (SMOTEENN) |
| Data Processing | Pandas, NumPy |
| Serialization | Dill |
| Database | MongoDB Atlas (PyMongo, Certifi) |
| Backend | FastAPI, Uvicorn, Jinja2 |
| Cloud | AWS S3, EC2, ECR, IAM (Boto3) |
| DevOps | Docker, GitHub Actions |
| Configuration | PyYAML, python-dotenv |

---

## 📂 Project Structure

```
Project-01-MLOps/
│
├── .github/
│   └── workflows/
│       └── aws.yaml                  # CI/CD pipeline
│
├── config/
│   ├── schema.yaml                   # Data schema for validation
│
├── notebook/
│   ├── exp-notebook.ipynb            # EDA & experimentation
│   └── mongoDB_demo.ipynb            # MongoDB connection demo
│
├── src/
│   ├── cloud_storage/                # AWS S3 utilities
│   ├── components/
│   │   ├── data_ingestion.py         # Stage 1: MongoDB → CSV
│   │   ├── data_validation.py        # Stage 2: Schema validation
│   │   ├── data_transformation.py    # Stage 3: Encoding + Scaling + SMOTEENN
│   │   ├── model_trainer.py          # Stage 4: RandomForest training
│   │   ├── model_evaluation.py       # Stage 5: F1 comparison vs production
│   │   └── model_pusher.py           # Stage 6: Push to S3
│   ├── configuration/                # MongoDB connection manager
│   ├── constants/                    # App-wide constants
│   ├── data_access/                  # MongoDB data access layer
│   ├── entity/                       # Config & artifact dataclasses
│   ├── exception/                    # Custom exception handling
│   ├── logger/                       # Structured logging
│   ├── pipline/
│   │   ├── training_pipeline.py      # Orchestrates all 6 stages
│   │   └── prediction_pipeline.py    # Real-time prediction from S3
│   └── utils/                        # I/O helpers (save/load, YAML)
│
├── static/                           # CSS for web UI
├── templates/                        # Jinja2 HTML templates
├── tests/                            # Unit tests
├── artifact/                         # Auto-generated pipeline artifacts
├── logs/                             # Auto-generated log files
│
├── app.py                            # FastAPI entry point
├── Dockerfile                        # Container definition
├── requirements.txt                  # Python dependencies
├── setup.py                          # Editable package setup
├── pyproject.toml                    # Build system config
└── LICENSE                           # MIT License
```

---

## 📂 Project Workflow

### 1️⃣ Data Ingestion

- Connects to MongoDB Atlas via PyMongo
- Extracts insurance data as a Pandas DataFrame
- Splits into train/test datasets
- Saves as CSV to the local `artifact/` directory

### 2️⃣ Data Validation

- Validates column count against `config/schema.yaml`
- Checks existence of all required numerical and categorical columns
- Saves JSON validation report
- Pipeline halts if validation fails

### 3️⃣ Data Transformation

- Gender encoding (`Female → 0`, `Male → 1`)
- One-hot encoding for `Vehicle_Age` and `Vehicle_Damage`
- Column renaming to sanitize special characters
- StandardScaler on `Age`, `Vintage`
- MinMaxScaler on `Annual_Premium`
- SMOTEENN for class imbalance handling
- Preprocessor pipeline serialized via Dill

### 4️⃣ Model Training

- Trains a Random Forest Classifier with fixed hyperparameters
- Evaluates: Accuracy, F1 Score, Precision, Recall
- Rejects model if accuracy falls below configured threshold
- Bundles preprocessor + model into a single `MyModel` object

### 5️⃣ Model Evaluation

- Downloads current production model from AWS S3
- Computes F1 Score for both models on the same test data
- New model accepted only if `F1(new) > F1(production)`

### 6️⃣ Model Deployment

- Uploads accepted model to AWS S3 as the new production baseline
- Serves real-time predictions through FastAPI

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

Create a `.env` file in the project root:

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

```
http://localhost:5000
```

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Renders the vehicle data prediction form |
| `POST` | `/` | Accepts form data, returns prediction (`Response-Yes` / `Response-No`) |
| `GET` | `/train` | Triggers the full training pipeline |

---

## 📊 Dataset Features

| Feature | Type | Description |
|---|---|---|
| `Gender` | Categorical | Gender of the customer (Male / Female) |
| `Age` | Integer | Age of the customer |
| `Driving_License` | Binary (0/1) | Whether the customer has a driving license |
| `Region_Code` | Float | Unique code for the customer's region |
| `Previously_Insured` | Binary (0/1) | Whether the customer already has vehicle insurance |
| `Vehicle_Age` | Categorical | Age of the vehicle (< 1yr, 1–2yr, > 2yr) |
| `Vehicle_Damage` | Categorical | Whether the vehicle was previously damaged (Yes / No) |
| `Annual_Premium` | Float | Annual premium amount (₹) |
| `Policy_Sales_Channel` | Float | Channel code used to reach the customer |
| `Vintage` | Integer | Days the customer has been with the company |
| **`Response`** | **Binary (0/1)** | **Target — Interested in health insurance?** |

---

## 🐳 Docker

### Build Image

```bash
docker build -t vehicle-insurance-mlops .
```

### Run Container

```bash
docker run -d -p 5000:5000 \
  -e AWS_ACCESS_KEY_ID="your_access_key" \
  -e AWS_SECRET_ACCESS_KEY="your_secret_key" \
  -e AWS_DEFAULT_REGION="us-east-1" \
  -e MONGODB_URL="your_mongodb_connection_string" \
  vehicle-insurance-mlops
```

> ⚠️ Environment variables are **required** — the container will fail without them.

---

## 🔄 CI/CD Pipeline

Implemented using GitHub Actions — triggers on every push to `main`.

### Continuous Integration

- Checkout source code
- Configure AWS credentials
- Build Docker image
- Push image to AWS ECR

### Continuous Deployment

- Pull latest image from ECR on EC2 (self-hosted runner)
- Run Docker container with environment variables
- Application live on port 5000

### Required GitHub Secrets

| Secret | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `AWS_DEFAULT_REGION` | AWS region (e.g., `us-east-1`) |
| `ECR_REPO` | Amazon ECR repository name |
| `MONGODB_URL` | MongoDB Atlas connection string |

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| AWS S3 | Model registry (stores production model) |
| AWS ECR | Docker image repository |
| AWS EC2 | Application hosting (self-hosted runner) |
| AWS IAM | Access management |

---

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

- MLOps Pipeline Development
- Machine Learning Model Lifecycle
- MongoDB Integration
- AWS Cloud Services (S3, ECR, EC2)
- Docker Containerization
- CI/CD Automation with GitHub Actions
- FastAPI Deployment
- Production-Ready ML Systems
