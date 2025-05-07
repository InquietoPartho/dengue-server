# import streamlit as st
# import numpy as np
# import joblib
# import shap
# import matplotlib.pyplot as plt
# import streamlit.components.v1 as components

# # ----------------- Load Model & Scaler -----------------
# model = joblib.load('F:\dd-stream\stacking_classifier.pkl')
# scaler = joblib.load('F:\dd-stream\scaler.pkl')

# # ----------------- Page Setup -----------------
# st.set_page_config(
#     page_title="🦟 Dengue Diagnosis Predictor",
#     page_icon="🦟",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# st.markdown("<h1 style='text-align: center;'>🦟 Dengue Diagnosis Predictor</h1>", unsafe_allow_html=True)
# st.markdown("""
# <div style='text-align: center; font-size: 16px;'>
# Estimate <b>risk of Dengue</b> based on hematological and demographic parameters.<br>
# Enter patient data and click <b>Predict</b> to see the results.
# </div>
# """, unsafe_allow_html=True)
# st.markdown("---")

# # --- User Input ---
# st.header("🧾 Patient Data")

# col1, col2, col3 = st.columns(3)
# gender = col1.selectbox("Gender", ["Male", "Female"])
# age = col2.slider("Age", 1, 100, 30)
# hb = col3.slider("Hemoglobin (g/dl)", 3.0, 20.0, 13.0, step=0.1)

# col4, col5, col6 = st.columns(3)
# neut = col4.slider("Neutrophils (%)", 10, 90, 50)
# lymph = col5.slider("Lymphocytes (%)", 5, 80, 40)
# mono = col6.slider("Monocytes (%)", 0, 15, 5)

# col7, col8, col9 = st.columns(3)
# eos = col7.slider("Eosinophils (%)", 0, 10, 2)
# rbc = col8.slider("RBC (million cells/μL)", 2.0, 6.5, 4.5, step=0.1)
# hct = col9.slider("HCT (%)", 20.0, 60.0, 45.0, step=0.5)

# col10, col11, col12 = st.columns(3)
# mcv = col10.slider("MCV (fl)", 50.0, 120.0, 85.0, step=0.5)
# mch = col11.slider("MCH (pg)", 10.0, 40.0, 27.0, step=0.5)
# mchc = col12.slider("MCHC (g/dl)", 20.0, 40.0, 32.0, step=0.5)

# col13, col14, col15 = st.columns(3)
# rdw = col13.slider("RDW-CV (%)", 10.0, 20.0, 14.0, step=0.1)
# platelets = col14.slider("Platelet Count (/cumm)", 20000, 600000, 150000, step=1000)
# mpv = col15.slider("MPV (fl)", 5.0, 15.0, 10.0, step=0.1)

# col16, col17 = st.columns(2)
# pdw = col16.slider("PDW (%)", 5.0, 25.0, 15.0, step=0.1)
# pct = col17.slider("PCT (%)", 0.01, 0.50, 0.1, step=0.01)

# wbc = st.slider("Total WBC count (/cumm)", 1000, 20000, 5000, step=100)

# # ----------------- Prepare Input -----------------
# gender_numeric = 0 if gender.lower() == 'male' else 1
# input_data = np.array([[
#     gender_numeric, age, hb, neut, lymph, mono, eos, rbc, hct, mcv,
#     mch, mchc, rdw, platelets, mpv, pdw, pct, wbc
# ]])
# input_scaled = scaler.transform(input_data)

# # ----------------- Prediction -----------------
# st.markdown("---")
# if st.button("🔮 Predict Dengue Status"):
#     prediction = model.predict(input_scaled)[0]
#     probability = model.predict_proba(input_scaled)[0][1]

#     st.markdown("### 🎯 Prediction Result")
#     status = "🦟 Likely Dengue Positive" if prediction == 1 else "✅ Likely Dengue Negative"
#     st.metric("Risk Probability", f"{probability * 100:.2f}%", label_visibility="visible")
    
#     if prediction == 1:
#         st.error(f"{status}: Immediate medical attention recommended.")
#     else:
#         st.success(f"{status}: Normal profile detected.")

#     st.markdown("---")
#     st.info("📌 This tool provides an AI-based estimation. Always consult a licensed medical professional for diagnosis or treatment.")

#     # ---------------- SHAP Force Plot ----------------
#     st.markdown("## 🔬 Model Explanation (SHAP Force Plot)")

#     try:
#         feature_names = [
#             'Gender', 'Age', 'Hemoglobin(g/dl)', 'Neutrophils(%)', 'Lymphocytes(%)',
#             'Monocytes(%)', 'Eosinophils(%)', 'RBC', 'HCT(%)', 'MCV(fl)', 'MCH(pg)',
#             'MCHC(g/dl)', 'RDW-CV(%)', 'Total Platelet Count(/cumm)', 'MPV(fl)',
#             'PDW(%)', 'PCT(%)', 'Total WBC count(/cumm)'
#         ]

#         cat_model = model.named_estimators_['cat']
#         explainer = shap.TreeExplainer(cat_model)
#         shap_values = explainer.shap_values(input_scaled)

#         shap.initjs()
#         force_plot = shap.force_plot(
#             base_value=explainer.expected_value,
#             shap_values=shap_values[0],
#             features=input_scaled[0],
#             feature_names=feature_names,
#             matplotlib=False
#         )
#         components.html(
#             f"<head>{shap.getjs()}</head><body>{force_plot.html()}</body>",
#             height=130
#         )

#         st.markdown("## 🧠 Top Contributing Features")
#         shap_dict = {
#             name: (value, shap_val)
#             for name, value, shap_val in zip(feature_names, input_scaled[0], shap_values[0])
#         }
#         sorted_features = sorted(shap_dict.items(), key=lambda x: abs(x[1][1]), reverse=True)

#         for feature, (value, shap_val) in sorted_features[:5]:
#             direction = "⬆️ increased" if shap_val > 0 else "⬇️ decreased"
#             color = "#e74c3c" if shap_val > 0 else "#27ae60"
#             st.markdown(f"<span style='color:{color}'>→ <b>{feature}</b> = {value:.2f} ({direction} risk)</span>", unsafe_allow_html=True)

#     except Exception as e:
#         st.error("⚠️ SHAP explanation failed.")
#         st.exception(e)

# # ----------------- Footer -----------------
# st.markdown("""
# ---
# <div style='text-align: center; font-size: 15px;'>
# 🧠 Developed by <b>Pankaj Bhowmik</b><br>
# Lecturer, CSE Dept<br>
# Hajee Mohammad Danesh Science and Technology University<br>
# © 2025 All Rights Reserved.
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import numpy as np
import joblib
import shap
import streamlit.components.v1 as components

# ----------------- Load Model & Scaler -----------------
model = joblib.load('F:/dd-stream/stacking_classifier.pkl')
scaler = joblib.load('F:/dd-stream/scaler.pkl')

# ----------------- Page Setup -----------------
st.set_page_config(
    page_title="🦟 Dengue Diagnosis Predictor",
    page_icon="🦟",
    layout="centered"
)

# ----------------- Custom CSS -----------------
st.markdown("""
<style>
body {
    background-color: #f4f6f8;
    background-image: linear-gradient(to right top, #ffffffaa, #e5f3ffcc, #ffffffaa);
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    text-shadow: 0 1px 1px rgba(0,0,0,0.1);
}

[data-testid="stMetricLabel"] {
    font-size: 18px;
}

section.main > div {
    background: rgba(255, 255, 255, 0.8);
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}

button[kind="primary"] {
    background-color: #0077b6 !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    box-shadow: 0 4px 14px rgba(0, 119, 182, 0.3);
    transition: background-color 0.3s ease-in-out;
}
button[kind="primary"]:hover {
    background-color: #0096c7 !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------- Title -----------------
st.markdown("<h1 style='text-align: center;'>🦟 Dengue Diagnosis Predictor</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 16px;'>
Estimate <b>risk of Dengue</b> based on hematological and demographic parameters.<br>
Enter patient data and click <b>Predict</b> to see the results.
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ----------------- Input Section -----------------
st.header("🧾 Patient Data")

col1, col2, col3 = st.columns(3)
gender = col1.selectbox("Gender", ["Male", "Female"])
age = col2.slider("Age", 1, 100, 30)
hb = col3.slider("Hemoglobin (g/dl)", 3.0, 20.0, 13.0, step=0.1)

col4, col5, col6 = st.columns(3)
neut = col4.slider("Neutrophils (%)", 10, 90, 50)
lymph = col5.slider("Lymphocytes (%)", 5, 80, 40)
mono = col6.slider("Monocytes (%)", 0, 15, 5)

col7, col8, col9 = st.columns(3)
eos = col7.slider("Eosinophils (%)", 0, 10, 2)
rbc = col8.slider("RBC (million cells/μL)", 2.0, 6.5, 4.5, step=0.1)
hct = col9.slider("HCT (%)", 20.0, 60.0, 45.0, step=0.5)

col10, col11, col12 = st.columns(3)
mcv = col10.slider("MCV (fl)", 50.0, 120.0, 85.0, step=0.5)
mch = col11.slider("MCH (pg)", 10.0, 40.0, 27.0, step=0.5)
mchc = col12.slider("MCHC (g/dl)", 20.0, 40.0, 32.0, step=0.5)

col13, col14, col15 = st.columns(3)
rdw = col13.slider("RDW-CV (%)", 10.0, 20.0, 14.0, step=0.1)
platelets = col14.slider("Platelet Count (/cumm)", 20000, 600000, 150000, step=1000)
mpv = col15.slider("MPV (fl)", 5.0, 15.0, 10.0, step=0.1)

col16, col17 = st.columns(2)
pdw = col16.slider("PDW (%)", 5.0, 25.0, 15.0, step=0.1)
pct = col17.slider("PCT (%)", 0.01, 0.50, 0.1, step=0.01)

wbc = st.slider("Total WBC count (/cumm)", 1000, 20000, 5000, step=100)

# ----------------- Prepare Input -----------------
gender_numeric = 0 if gender.lower() == 'male' else 1
input_data = np.array([[
    gender_numeric, age, hb, neut, lymph, mono, eos, rbc, hct, mcv,
    mch, mchc, rdw, platelets, mpv, pdw, pct, wbc
]])
input_scaled = scaler.transform(input_data)

# ----------------- Prediction -----------------
st.markdown("---")
if st.button("🔮 Predict Dengue Status"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.markdown("### 🎯 Prediction Result")
    status = "🦟 Likely Dengue Positive" if prediction == 1 else "✅ Likely Dengue Negative"
    st.metric("Risk Probability", f"{probability * 100:.2f}%", label_visibility="visible")

    if prediction == 1:
        st.error(f"{status}: Immediate medical attention recommended.")
    else:
        st.success(f"{status}: Normal profile detected.")

    st.markdown("---")
    st.info("📌 This tool provides an AI-based estimation. Always consult a licensed medical professional for diagnosis or treatment.")

    # ---------------- SHAP Force Plot ----------------
    st.markdown("## 🔬 Model Explanation (SHAP Force Plot)")
    try:
        feature_names = [
            'Gender', 'Age', 'Hemoglobin(g/dl)', 'Neutrophils(%)', 'Lymphocytes(%)',
            'Monocytes(%)', 'Eosinophils(%)', 'RBC', 'HCT(%)', 'MCV(fl)', 'MCH(pg)',
            'MCHC(g/dl)', 'RDW-CV(%)', 'Platelets(/cumm)', 'MPV(fl)',
            'PDW(%)', 'PCT(%)', 'WBC(/cumm)'
        ]

        cat_model = model.named_estimators_['cat']
        explainer = shap.TreeExplainer(cat_model)
        shap_values = explainer.shap_values(input_scaled)

        shap.initjs()
        force_plot = shap.force_plot(
            base_value=explainer.expected_value,
            shap_values=shap_values[0],
            features=input_scaled[0],
            feature_names=feature_names,
            matplotlib=False
        )
        components.html(
            f"<head>{shap.getjs()}</head><body>{force_plot.html()}</body>",
            height=130
        )

        st.markdown("## 🧠 Top Contributing Features")
        shap_dict = {
            name: (value, shap_val)
            for name, value, shap_val in zip(feature_names, input_scaled[0], shap_values[0])
        }
        sorted_features = sorted(shap_dict.items(), key=lambda x: abs(x[1][1]), reverse=True)

        for feature, (value, shap_val) in sorted_features[:5]:
            direction = "⬆️ increased" if shap_val > 0 else "⬇️ decreased"
            color = "#e74c3c" if shap_val > 0 else "#27ae60"
            st.markdown(f"<span style='color:{color}'>→ <b>{feature}</b> = {value:.2f} ({direction} risk)</span>", unsafe_allow_html=True)

    except Exception as e:
        st.error("⚠️ SHAP explanation failed.")
        st.exception(e)

# ----------------- Footer -----------------
st.markdown("""
---
<div style='text-align: center; font-size: 15px;'>
🧠 Developed by <b>Pijush Kanti Roy Partho</b><br>
Student, ECE Dept<br>
Hajee Mohammad Danesh Science and Technology University<br>
© 2025 All Rights Reserved.
</div>
""", unsafe_allow_html=True)
