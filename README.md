# Heart Disease Prediction App

A comprehensive machine learning application for predicting heart disease risk with detailed medical analysis and educational insights.

## Features

- **13 Medical Parameters**: Comprehensive analysis including age, sex, chest pain type, blood pressure, cholesterol, etc.
- **Detailed Explanations**: Each parameter includes medical explanations and risk factors
- **Symptom Analysis**: Advanced symptom detection and risk stratification
- **Interactive Interface**: User-friendly Streamlit web application
- **Educational Content**: Medical information and disclaimers for educational purposes

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

3. **Access the App**: Open your browser to the provided URL (usually http://localhost:8501)

## Manual Configuration

If you need custom configuration:

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