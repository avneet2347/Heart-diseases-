# Heart Disease Prediction Web Application

A full-stack web application for predicting heart disease risk using machine learning.

## Features

- **Machine Learning Model**: Logistic Regression model trained on heart disease dataset
- **FastAPI Backend**: RESTful API for model predictions
- **React Frontend**: Modern, responsive web interface
- **Real-time Predictions**: Instant risk assessment with confidence scores

## Project Structure

```
├── api.py                 # FastAPI backend
├── app.py                 # Streamlit app (alternative interface)
├── notebook.ipynb         # Model training notebook
├── model.pkl             # Trained model file
├── requirements.txt       # Python dependencies
├── Heart_Disease_Prediction.csv  # Dataset
└── frontend/             # React frontend
    ├── public/
    ├── src/
    │   ├── App.js
    │   ├── index.js
    │   └── index.css
    └── package.json
```

## Installation & Setup

### Backend Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the FastAPI server:
```bash
python api.py
```
The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```
The frontend will be available at `http://localhost:3000`

## API Endpoints

### POST /predict
Predict heart disease risk based on patient data.

**Request Body:**
```json
{
  "age": 45,
  "sex": 1,
  "cp": 2,
  "trestbps": 130,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.2,
  "slope": 2,
  "ca": 0,
  "thal": 3
}
```

**Response:**
```json
{
  "prediction": 1,
  "result": "Heart Disease Detected",
  "confidence": 87.45,
  "risk_level": "High Risk"
}
```

### GET /health
Check API health status.

## Usage

1. Start the backend API server
2. Start the frontend React app
3. Open your browser to `http://localhost:3000`
4. Fill in the patient information form
5. Click "Predict Heart Disease Risk" to get results

## Model Information

- **Algorithm**: Logistic Regression
- **Accuracy**: ~87%
- **Features**: 13 medical parameters
- **Target**: Heart disease presence/absence

## Technologies Used

- **Backend**: FastAPI, Python, scikit-learn
- **Frontend**: React, Material-UI
- **Machine Learning**: scikit-learn, pandas, numpy

## Deployment

### Backend Deployment
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Frontend Deployment
```bash
cd frontend
npm run build
# Serve the build folder with any static server
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.