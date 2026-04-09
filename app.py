import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title(" Heart Disease Prediction")

# Inputs
age = st.number_input("Age")
sex = st.selectbox("Sex", [0,1])
cp = st.selectbox("Chest Pain Type", [1,2,3,4])
trestbps = st.number_input("Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])
restecg = st.selectbox("EKG Results", [0,1,2])
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Angina", [0,1])
oldpeak = st.number_input("ST Depression")
slope = st.selectbox("Slope", [1,2,3])
ca = st.selectbox("Number of Vessels", [0,1,2,3])
thal = st.selectbox("Thallium", [3,6,7])

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    result = model.predict(input_data)

    if result[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success(" No Heart Disease")