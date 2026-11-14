# Will This Visitor Buy? – Real-Time Purchase Intent

## 1. Project Overview

This project uses Machine Learning to predict whether an online shopper will make a purchase based on their browsing session behavior.

The goal is to help e-commerce businesses identify visitors who are more likely to purchase and make better marketing decisions.

## 2. Problem Statement

Most visitors leave e-commerce websites without purchasing anything.

This project aims to predict the purchase intention of a visitor using session-related information such as:
- Number of pages visited
- Time spent on different pages
- Bounce rate and exit rate
- Visitor type
- Month and weekend information

The model predicts whether the visitor will generate revenue (True or False).

## 3. Dataset

The project uses the Online Shoppers Purchasing Intention Dataset from the UCI Machine Learning Repository.

- Number of sessions: 12,330
- Number of input features: 17
- Target variable: Revenue

Dataset: https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

## 4. Project Workflow

1. Data collection and understanding
2. Exploratory Data Analysis (EDA)
3. Data preprocessing
4. Feature encoding and scaling
5. Model training
6. Model comparison and evaluation
7. Hyperparameter tuning
8. Saving the trained model
9. Building and deploying a Streamlit web application

## 5. Machine Learning Models

The project compares multiple classification models:

- Dummy Classifier (baseline)
- Logistic Regression
- Decision Tree
- Random Forest

## 6. Web Application

The project includes an interactive Streamlit application where users can enter visitor session information and receive a purchase prediction.

**Live Application:** [https://purchase-intent-prediction-apm5eqjewary5txvxpsyvj.streamlit.app/]

## 7. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## 8. Project Files

- `wrong_file_backup.ipynb` – Jupyter Notebook containing the project analysis and machine learning workflow.
- `app.py` – Streamlit web application.
- `purchase_intent_model_compressed.pkl` – Saved trained machine learning model.
- `requirements.txt` – Required Python packages.

## 9. How to Run the Project Locally

1. Clone this repository.
2. Install the required packages:

   `pip install -r requirements.txt`

3. Run the application:

   `streamlit run app.py`

## 10. Future Improvements

- Improve prediction performance.
- Experiment with additional machine learning algorithms.
- Optimize prediction thresholds based on business objectives.
- Develop more advanced marketing recommendations.

---

**Project:** Will This Visitor Buy? – Real-Time Purchase Intent
