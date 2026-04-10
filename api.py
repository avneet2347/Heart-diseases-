from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle
import uvicorn

# Load the trained model
try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    raise Exception("Model file 'model.pkl' not found. Please train the model first.")

app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease based on patient data",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HeartDiseaseInput(BaseModel):
    age: int
    sex: int  # 0 = female, 1 = male
    cp: int   # chest pain type (1-4)
    trestbps: int  # resting blood pressure
    chol: int  # serum cholesterol in mg/dl
    fbs: int   # fasting blood sugar > 120 mg/dl (0 = false, 1 = true)
    restecg: int  # resting electrocardiographic results (0-2)
    thalach: int  # maximum heart rate achieved
    exang: int  # exercise induced angina (0 = no, 1 = yes)
    oldpeak: float  # ST depression induced by exercise relative to rest
    slope: int  # slope of the peak exercise ST segment (1-3)
    ca: int    # number of major vessels colored by fluoroscopy (0-3)
    thal: int  # thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)

class PredictionResponse(BaseModel):
    prediction: int
    result: str
    confidence: float
    risk_level: str

@app.get("/")
async def root():
    return {"message": "Heart Disease Prediction API", "status": "active"}

@app.post("/predict", response_model=PredictionResponse)
async def predict_heart_disease(input_data: HeartDiseaseInput):
    try:
        # Convert input to numpy array
        features = np.array([[
            input_data.age,
            input_data.sex,
            input_data.cp,
            input_data.trestbps,
            input_data.chol,
            input_data.fbs,
            input_data.restecg,
            input_data.thalach,
            input_data.exang,
            input_data.oldpeak,
            input_data.slope,
            input_data.ca,
            input_data.thal
        ]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Get prediction probability for confidence
        prediction_proba = model.predict_proba(features)[0]
        confidence = float(max(prediction_proba))

        # Determine result and risk level
        if prediction == 1:
            result = "Heart Disease Detected"
            if confidence > 0.8:
                risk_level = "High Risk"
            elif confidence > 0.6:
                risk_level = "Medium Risk"
            else:
                risk_level = "Low Risk"
        else:
            result = "No Heart Disease Detected"
            risk_level = "Low Risk"

        return PredictionResponse(
            prediction=int(prediction),
            result=result,
            confidence=round(confidence * 100, 2),
            risk_level=risk_level
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)