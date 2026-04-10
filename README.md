# Heart Disease Prediction App

A comprehensive machine learning application for predicting heart disease risk with detailed medical analysis and educational insights.

## Features

- **13 Medical Parameters**: Comprehensive analysis including age, sex, chest pain type, blood pressure, cholesterol, etc.
- **Detailed Explanations**: Each parameter includes medical explanations and risk factors
- **Symptom Analysis**: Advanced symptom detection and risk stratification
- **Interactive Interface**: User-friendly Streamlit web application
- **Educational Content**: Medical information and disclaimers for educational purposes

## Patient Data Collection Chatbot

The interactive patient data collection chatbot (`patient_chatbot.py`) guides you through collecting all 13 medical parameters through conversation:

### How to Use:
```bash
python patient_chatbot.py
```

### What it collects:
- **Patient Name** (optional)
- **Age** (1-120 years)
- **Sex** (Male/Female)
- **Chest Pain Type** (4 categories)
- **Resting Blood Pressure** (80-200 mm Hg)
- **Cholesterol Level** (100-600 mg/dL)
- **Fasting Blood Sugar** (Normal/High)
- **Resting ECG Results** (3 categories)
- **Maximum Heart Rate** (60-220 bpm)
- **Exercise Induced Angina** (Yes/No)
- **ST Depression** (0.0-6.2 mm)
- **ST Segment Slope** (3 types)
- **Major Vessels Affected** (0-3)
- **Thallium Stress Test** (3 results)

### Features:
✅ **Interactive Q&A**: Step-by-step medical data collection  
✅ **Input Validation**: Ensures medically valid ranges  
✅ **Medical Explanations**: Educational information for each parameter  
✅ **Data Persistence**: Saves to `patient_data.json` for app integration  
✅ **Form Pre-filling**: Streamlit app automatically loads saved data  

### Workflow:
1. Run `python patient_chatbot.py`
2. Answer questions about patient medical history
3. Review and confirm the collected data
4. Data is automatically saved and loaded in the prediction app
5. Use the "Clear Patient Data" button in the app to reset

## Quick Start

1. **Collect Patient Data**:
   ```bash
   python patient_chatbot.py
   ```

2. **Run the Prediction App**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

3. **View Results**: The form will be pre-filled with patient data, click "Predict" to see analysis.

## Deployment Chatbot

The interactive deployment chatbot (`deploy_chatbot.py`) will ask you detailed questions about:

- **Application Name**: Custom name for your deployment
- **Deployment Type**: Local, Docker, Cloud, or Server deployment
- **Environment**: Development, Staging, or Production
- **Port Configuration**: Custom port for the application
- **Database Setup**: Optional database configuration
- **Authentication**: User authentication options
- **Monitoring**: Logging and monitoring preferences
- **API Endpoints**: REST API exposure
- **Security**: HTTPS and security settings
- **Performance**: Upload limits and scaling options
- **Backups**: Automatic backup configuration
- **Notifications**: Email notification setup

The chatbot will automatically:
- Generate configuration files (`.streamlit/config.toml`, `.env`)
- Create Docker files if needed
- Install dependencies
- Start the application

## Manual Configuration

If you prefer manual setup:

### Environment Variables (.env)
```bash
ENVIRONMENT=development
APP_NAME=Heart Disease Prediction App
DB_TYPE=sqlite
API_PORT=8000
```

### Streamlit Configuration (.streamlit/config.toml)
```toml
[server]
port = 8501
maxUploadSize = 50
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

## Project Structure

```
├── app.py                 # Main Streamlit application
├── deploy_chatbot.py      # Interactive deployment assistant
├── notebook.ipynb         # Model training notebook
├── requirements.txt       # Python dependencies
├── Heart_Disease_Prediction.csv  # Dataset
├── model.pkl             # Trained ML model
├── .streamlit/           # Streamlit configuration
├── .env                  # Environment variables
└── README.md             # This file
```

## Dependencies

The application uses comprehensive Python packages for:
- **Machine Learning**: scikit-learn, pandas, numpy
- **Web Interface**: Streamlit
- **Data Processing**: Various scientific computing libraries
- **Visualization**: Plotting and charting libraries

## Usage

1. Run the deployment chatbot: `python deploy_chatbot.py`
2. Follow the interactive prompts
3. The application will start automatically or provide deployment instructions

## Medical Disclaimer

This application is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

## License

This project is open source and available under standard licensing terms.

## Contributing

Contributions are welcome! Please use the deployment chatbot for consistent setup across development environments.