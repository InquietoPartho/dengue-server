# 🦟 Dengue Diagnosis Predictor

**Live App:** [https://dengue-prediction-hstu.streamlit.app/](https://dengue-prediction-hstu.streamlit.app/)  
**Author:** Pijush Kanti Roy Partho  
**University:** Hajee Mohammad Danesh Science and Technology University  
**Department:** Electronics and Communication Engineering

---

---

## 🌐 Live Web App Preview

Below is a preview of the deployed Dengue Diagnosis Predictor web application:

![Dengue Predictor App Screenshot](![Alt text](app_preview.png))

You can try it yourself here: [https://dengue-prediction-hstu.streamlit.app/](https://dengue-prediction-hstu.streamlit.app/)

## 🧠 Project Overview

The **Dengue Diagnosis Predictor** is an intelligent web-based application built with **Streamlit** that leverages a **Stacking Classifier** ensemble machine learning model to estimate the likelihood of dengue infection using hematological and demographic parameters.

This tool empowers medical practitioners and health professionals with a decision support system that not only predicts dengue status but also explains the reasoning using **SHAP** (SHapley Additive exPlanations) visualizations.

---

## 🚀 Features

- 🔮 **AI-powered Prediction** of Dengue status (Positive/Negative)
- 📊 **Interactive Input Interface** for over 18 patient health indicators
- 🧾 **SHAP Force Plot** to visualize feature contribution for transparency
- 🧠 **Top 5 Influential Features** highlighted for clinical insight
- ⚡ Real-time performance using a pre-trained stacking ensemble model

---

## 🧪 Model Details

- **Algorithm**: Stacking Classifier
  - Base models include tree-based and linear classifiers
- **Explainability**: SHAP for local interpretability
- **Input Features**:
  - Gender, Age, Hemoglobin, Neutrophils, Lymphocytes, Monocytes, Eosinophils
  - RBC, HCT, MCV, MCH, MCHC, RDW, Platelet Count, MPV, PDW, PCT, WBC

---

## 🛠 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/dengue-diagnosis-app.git
   cd dengue-diagnosis-app
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**

   ```bash
   streamlit run app.py
   ```
