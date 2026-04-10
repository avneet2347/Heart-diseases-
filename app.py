import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🫀 Heart Disease Prediction")

# Age input (integer only)
age = st.number_input("Age", min_value=1, max_value=120, value=50, step=1, format="%d")
st.info(f"**Age:** {age} years")

# Sex selection
sex_options = {0: "Male", 1: "Female"}
sex = st.selectbox("Sex", options=list(sex_options.keys()), format_func=lambda x: sex_options[x], index=0)
st.info(f"**Selected:** {sex_options[sex]}")

# Chest Pain Type
cp_options = {
    0: "Typical Angina",
    1: "Atypical Angina",
    2: "Non-anginal Pain",
    3: "Asymptomatic"
}
cp = st.selectbox("Chest Pain Type", options=list(cp_options.keys()), format_func=lambda x: f"{x} → {cp_options[x]}", index=0)
st.info(f"**Selected:** {cp_options[cp]}")

# Blood Pressure and Cholesterol with risk table
st.subheader("🩸 Blood Pressure & Cholesterol")

col1, col2 = st.columns(2)

with col1:
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120, step=1)
    st.info(f"**Blood Pressure:** {trestbps} mm Hg")

with col2:
    chol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=600, value=200, step=1)
    st.info(f"**Cholesterol:** {chol} mg/dL")

# Risk assessment table
st.markdown("**Risk Assessment Table:**")
risk_data = {
    "BP": [120, 150, 130],
    "Cholesterol": [180, 250, 300],
    "Risk": ["Low", "High", "Medium-High"]
}

st.table(risk_data)

# Fasting Blood Sugar
fbs_options = {
    0: "FBS ≤ 120 mg/dL (Normal)",
    1: "FBS > 120 mg/dL (High)"
}
fbs = st.selectbox("Fasting Blood Sugar", options=list(fbs_options.keys()), format_func=lambda x: f"{x}: {fbs_options[x]}", index=0)
st.info(f"**Selected:** {fbs_options[fbs]}")

# Thalium (Thalassemia)
thal_options = {
    1: "Normal",
    2: "Fixed Defect",
    3: "Reversible Defect"
}
thal = st.selectbox("Thallium (Thalassemia)", options=list(thal_options.keys()), format_func=lambda x: f"{x}: {thal_options[x]}", index=0)
st.info(f"**Selected:** {thal_options[thal]}")

# Max Heart Rate
thalach = st.number_input("Maximum Heart Rate (bpm)", min_value=60, max_value=220, value=150, step=1)
max_hr_calc = 220 - age
st.info(f"**Max Heart Rate:** {thalach} bpm")
st.success(f"**Expected Max HR (220 - Age):** {max_hr_calc} bpm")

# Exercise Induced Angina
exang_options = {
    0: "No (exercise pe pain nahi)",
    1: "Yes (exercise pe pain hota hai)"
}
exang = st.selectbox("Exercise Induced Angina", options=list(exang_options.keys()), format_func=lambda x: f"{x}: {exang_options[x]}", index=0)
st.info(f"**Selected:** {exang_options[exang]}")

# ST Depression
oldpeak = st.number_input("ST Depression (mm)", min_value=0.0, max_value=6.2, value=1.0, step=0.1, format="%.1f")

# ST Depression risk assessment
if oldpeak == 0.0:
    st_risk = "Low"
    st_meaning = "Normal"
elif oldpeak <= 1.0:
    st_risk = "Medium"
    st_meaning = "Mild change"
elif oldpeak <= 2.0:
    st_risk = "High"
    st_meaning = "Significant depression"
else:
    st_risk = "Very High"
    st_meaning = "Severe"

st.info(f"**ST Depression:** {oldpeak} mm")
st.warning(f"**Risk Level:** {st_risk} - {st_meaning}")

# ST Depression risk table
st.markdown("**ST Depression Risk Table:**")
st_table = {
    "ST Depression": ["0.0", "0.1 – 1.0", "> 1.0", "> 2.0"],
    "Meaning": ["Normal", "Mild change", "Significant depression", "Severe"],
    "Risk": ["Low", "Medium", "High", "Very High"]
}
st.table(st_table)

# Slope
slope_options = {
    0: "Upsloping (ST segment upar ja raha hai)",
    1: "Flat (ST segment straight hai)",
    2: "Downsloping (ST segment niche ja raha hai)"
}
slope = st.selectbox("Slope of Peak Exercise ST Segment", options=list(slope_options.keys()), format_func=lambda x: f"{x}: {slope_options[x]}", index=1)
st.info(f"**Selected:** {slope_options[slope]}")

# ECG Results
restecg_options = {
    0: "Normal",
    1: "ST-T wave abnormality",
    2: "Left Ventricular Hypertrophy (LVH)"
}
restecg = st.selectbox("Resting ECG Results", options=list(restecg_options.keys()), format_func=lambda x: f"{x}: {restecg_options[x]}", index=0)
st.info(f"**Selected:** {restecg_options[restecg]}")

# Number of Major Vessels
ca_options = {
    0: "No major vessel blockage",
    1: "1 vessel affected",
    2: "2 vessels affected",
    3: "3 vessels affected"
}
ca = st.selectbox("Number of Major Vessels", options=list(ca_options.keys()), format_func=lambda x: f"{x}: {ca_options[x]}", index=0)
st.info(f"**Selected:** {ca_options[ca]}")

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)

    st.markdown("---")
    st.subheader("🔍 Patient Symptoms Analysis")

    # Analyze symptoms based on input parameters
    symptoms = []

    # Age-related symptoms
    if age > 50:
        symptoms.append("• Age > 50 years (increased cardiovascular risk)")

    # Sex-related symptoms
    if sex == 1:  # Female
        symptoms.append("• Female gender (different risk profile)")

    # Chest pain analysis
    if cp == 0:
        symptoms.append("• Typical Angina (chest pain during physical activity)")
    elif cp == 1:
        symptoms.append("• Atypical Angina (chest pain not related to physical activity)")
    elif cp == 2:
        symptoms.append("• Non-anginal Pain (chest discomfort not typical of angina)")
    elif cp == 3:
        symptoms.append("• Asymptomatic (no chest pain symptoms)")

    # Blood pressure symptoms
    if trestbps >= 140:
        symptoms.append(f"• High Blood Pressure ({trestbps} mm Hg - Hypertension)")
    elif trestbps >= 130:
        symptoms.append(f"• Elevated Blood Pressure ({trestbps} mm Hg - Stage 1 Hypertension)")

    # Cholesterol symptoms
    if chol >= 240:
        symptoms.append(f"• High Cholesterol ({chol} mg/dL - Hypercholesterolemia)")
    elif chol >= 200:
        symptoms.append(f"• Borderline High Cholesterol ({chol} mg/dL)")

    # Blood sugar symptoms
    if fbs == 1:
        symptoms.append("• High Fasting Blood Sugar (> 120 mg/dL - Possible Diabetes)")

    # ECG symptoms
    if restecg == 1:
        symptoms.append("• ST-T Wave Abnormality (possible heart stress)")
    elif restecg == 2:
        symptoms.append("• Left Ventricular Hypertrophy (heart muscle thickening)")

    # Heart rate symptoms
    max_expected_hr = 220 - age
    if thalach < max_expected_hr * 0.8:
        symptoms.append(f"• Low Exercise Heart Rate ({thalach} bpm - poor cardiovascular fitness)")

    # Exercise angina symptoms
    if exang == 1:
        symptoms.append("• Exercise Induced Angina (chest pain during exercise)")

    # ST depression symptoms
    if oldpeak > 1.0:
        if oldpeak > 2.0:
            symptoms.append(f"• Severe ST Depression ({oldpeak} mm - significant ischemia)")
        else:
            symptoms.append(f"• ST Depression ({oldpeak} mm - myocardial stress)")

    # Slope symptoms
    if slope == 2:
        symptoms.append("• Downsloping ST Segment (concerning ECG pattern)")

    # Vessel symptoms
    if ca > 0:
        symptoms.append(f"• {ca} coronary vessel(s) affected (blockage detected)")

    # Thalassemia symptoms
    if thal == 2:
        symptoms.append("• Fixed Defect (permanent heart muscle damage)")
    elif thal == 3:
        symptoms.append("• Reversible Defect (temporary reduced blood flow)")

    # Display results
    if prediction[0] == 1:
        st.error("🚨 **Heart Disease Risk Detected**")
        st.markdown("**Based on your symptoms, you may have heart disease. Please consult a cardiologist immediately.**")
    else:
        st.success("✅ **Low Heart Disease Risk**")
        st.markdown("**Your symptoms suggest low risk of heart disease, but regular check-ups are recommended.**")

    # Display symptoms
    st.markdown("### 📋 **Patient Symptoms Identified:**")
    if symptoms:
        for symptom in symptoms:
            st.markdown(symptom)
    else:
        st.info("No significant symptoms detected from the provided parameters.")

    # Risk assessment summary
    st.markdown("### 📊 **Risk Assessment Summary:**")
    risk_factors = len([s for s in symptoms if any(word in s.lower() for word in ['high', 'hypertension', 'hypercholesterolemia', 'diabetes', 'abnormality', 'hypertrophy', 'angina', 'depression', 'ischemia', 'damage', 'blockage'])])

    if risk_factors >= 3:
        st.error(f"**High Risk:** {risk_factors} major risk factors identified")
    elif risk_factors >= 1:
        st.warning(f"**Moderate Risk:** {risk_factors} risk factor(s) identified")
    else:
        st.success("**Low Risk:** Minimal risk factors detected")

    st.markdown("---")
    st.caption("⚠️ **Medical Disclaimer:** This analysis is for educational purposes only. Always consult qualified healthcare professionals for proper diagnosis and treatment.")
