import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("❤️ Heart Disease Prediction")

st.markdown("""
### 🏥 Advanced Heart Disease Risk Assessment
Enter patient information below to get an AI-powered heart disease risk prediction.
""")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Patient Demographics")

    # Age - Integer input
    age = st.number_input("Age (years)", min_value=1, max_value=120, value=50, step=1, format="%d")
    st.info(f"💡 Max Heart Rate should be: **{220 - age} bpm**")

    # Sex with descriptive labels
    sex_options = {0: "Female", 1: "Male"}
    sex_display = st.selectbox("Sex", options=list(sex_options.keys()), format_func=lambda x: sex_options[x])
    st.caption(f"Selected: **{sex_options[sex_display]}**")

with col2:
    st.subheader("🫀 Cardiac Parameters")

    # Chest Pain Type with descriptions
    cp_options = {
        0: "Typical Angina - Chest pain during physical activity",
        1: "Atypical Angina - Chest pain not related to physical activity",
        2: "Non-anginal Pain - Chest discomfort not typical of angina",
        3: "Asymptomatic - No chest pain symptoms"
    }
    cp_display = st.selectbox("Chest Pain Type", options=list(cp_options.keys()), format_func=lambda x: f"{x} - {cp_options[x].split(' - ')[1]}")
    st.caption(f"Selected: **{cp_options[cp_display]}**")

# Blood Pressure and Cholesterol with risk assessment
st.subheader("🩸 Blood Pressure & Cholesterol")

col3, col4 = st.columns(2)

with col3:
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
    # Blood pressure risk assessment
    if trestbps < 120:
        bp_risk = "🟢 Normal (< 120)"
    elif trestbps < 130:
        bp_risk = "🟡 Elevated (120-129)"
    elif trestbps < 140:
        bp_risk = "🟠 Stage 1 Hypertension (130-139)"
    else:
        bp_risk = "🔴 Stage 2 Hypertension (≥ 140)"
    st.success(f"Blood Pressure Risk: {bp_risk}")

with col4:
    chol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=600, value=200)
    # Cholesterol risk assessment
    if chol < 200:
        chol_risk = "🟢 Desirable (< 200)"
    elif chol < 240:
        chol_risk = "🟡 Borderline High (200-239)"
    else:
        chol_risk = "🔴 High (≥ 240)"
    st.success(f"Cholesterol Risk: {chol_risk}")

# Additional parameters
st.subheader("🔬 Diagnostic Tests")

col5, col6 = st.columns(2)

with col5:
    # Fasting Blood Sugar
    fbs_options = {
        0: "Normal (FBS ≤ 120 mg/dL)",
        1: "High (FBS > 120 mg/dL)"
    }
    fbs_display = st.selectbox("Fasting Blood Sugar", options=list(fbs_options.keys()), format_func=lambda x: fbs_options[x])
    st.caption(f"Selected: **{fbs_options[fbs_display]}**")

    # EKG Results
    restecg_options = {
        0: "Normal - No abnormalities",
        1: "ST-T Wave Abnormality - Possible heart stress",
        2: "Left Ventricular Hypertrophy - Heart muscle thickening"
    }
    restecg_display = st.selectbox("EKG Results", options=list(restecg_options.keys()), format_func=lambda x: f"{x} - {restecg_options[x].split(' - ')[1]}")
    st.caption(f"Selected: **{restecg_options[restecg_display]}**")

with col6:
    # Max Heart Rate
    thalach = st.number_input("Max Heart Rate Achieved (bpm)", min_value=60, max_value=220, value=150)
    max_hr_expected = 220 - age
    if thalach >= max_hr_expected * 0.8:
        hr_status = "🟢 Good exercise capacity"
    elif thalach >= max_hr_expected * 0.6:
        hr_status = "🟡 Moderate exercise capacity"
    else:
        hr_status = "🟠 Poor exercise capacity"
    st.info(f"Heart Rate Status: {hr_status}")

    # Exercise Angina
    exang_options = {
        0: "No - No chest pain during exercise",
        1: "Yes - Chest pain occurs during exercise"
    }
    exang_display = st.selectbox("Exercise Angina", options=list(exang_options.keys()), format_func=lambda x: exang_options[x])
    st.caption(f"Selected: **{exang_options[exang_display]}**")

# ST Depression and Slope
st.subheader("📈 ECG Analysis")

col7, col8 = st.columns(2)

with col7:
    oldpeak = st.number_input("ST Depression (mm)", min_value=0.0, max_value=6.2, value=1.0, step=0.1)
    # ST Depression risk assessment
    if oldpeak == 0.0:
        st_risk = "🟢 Normal - No depression"
    elif oldpeak <= 1.0:
        st_risk = "🟡 Mild - Slight depression (0.1-1.0 mm)"
    elif oldpeak <= 2.0:
        st_risk = "🟠 Significant - Moderate depression (1.1-2.0 mm)"
    else:
        st_risk = "🔴 Severe - Major depression (> 2.0 mm)"
    st.warning(f"ST Depression Risk: {st_risk}")

with col8:
    # Slope
    slope_options = {
        0: "Upsloping - ST segment rises upward",
        1: "Flat - ST segment is horizontal",
        2: "Downsloping - ST segment falls downward"
    }
    slope_display = st.selectbox("ST Segment Slope", options=list(slope_options.keys()), format_func=lambda x: f"{x} - {slope_options[x].split(' - ')[1]}")
    st.caption(f"Selected: **{slope_options[slope_display]}**")

# Final parameters
st.subheader("🔍 Advanced Cardiac Assessment")

col9, col10 = st.columns(2)

with col9:
    # Number of Vessels
    ca_options = {
        0: "No major vessel blockage",
        1: "1 vessel affected",
        2: "2 vessels affected",
        3: "3 vessels affected"
    }
    ca_display = st.selectbox("Number of Vessels Affected", options=list(ca_options.keys()), format_func=lambda x: f"{x} - {ca_options[x]}")
    st.caption(f"Selected: **{ca_options[ca_display]}**")

with col10:
    # Thallium Test
    thal_options = {
        1: "Normal - No defects detected",
        2: "Fixed Defect - Permanent damage",
        3: "Reversible Defect - Temporary ischemia"
    }
    thal_display = st.selectbox("Thallium Stress Test", options=list(thal_options.keys()), format_func=lambda x: f"{x} - {thal_options[x].split(' - ')[1]}")
    st.caption(f"Selected: **{thal_options[thal_display]}**")

# Prediction Section
st.markdown("---")
st.subheader("🔮 Prediction Results")

if st.button("🩺 Predict Heart Disease Risk", type="primary", use_container_width=True):
    with st.spinner("Analyzing patient data..."):
        # Prepare input data
        input_data = np.array([[age, sex_display, cp_display, trestbps, chol, fbs_display,
                                restecg_display, thalach, exang_display, oldpeak,
                                slope_display, ca_display, thal_display]])

        # Make prediction
        result = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)[0]

        # Display results
        if result[0] == 1:
            st.error("🚨 **Heart Disease Detected**")
            st.markdown(f"**Confidence:** {prediction_proba[1]*100:.1f}%")

            # Risk factors summary
            risk_factors = []
            if trestbps >= 140: risk_factors.append("High Blood Pressure")
            if chol >= 240: risk_factors.append("High Cholesterol")
            if fbs_display == 1: risk_factors.append("High Blood Sugar")
            if exang_display == 1: risk_factors.append("Exercise Angina")
            if oldpeak > 1.0: risk_factors.append("ST Depression")
            if ca_display >= 2: risk_factors.append("Multiple Vessel Blockage")

            if risk_factors:
                st.warning("**Key Risk Factors Identified:**")
                for factor in risk_factors:
                    st.markdown(f"• {factor}")

        else:
            st.success("✅ **No Heart Disease Detected**")
            st.markdown(f"**Confidence:** {prediction_proba[0]*100:.1f}%")

            st.info("**Recommendations:**")
            st.markdown("• Maintain regular check-ups")
            st.markdown("• Follow a heart-healthy lifestyle")
            st.markdown("• Monitor blood pressure and cholesterol")

# Footer
st.markdown("---")
st.caption("⚠️ **Medical Disclaimer:** This tool provides preliminary risk assessment. Always consult qualified healthcare professionals for proper diagnosis and treatment.")