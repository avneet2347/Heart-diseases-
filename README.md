# Heart Disease Prediction App

A comprehensive machine learning application for predicting heart disease risk with detailed medical analysis and educational insights.

## Features

- **13 Medical Parameters**: Comprehensive analysis including age, sex, chest pain type, blood pressure, cholesterol, etc.
- **Detailed Explanations**: Each parameter includes medical explanations and risk factors
- **Symptom Analysis**: Advanced symptom detection and risk stratification
- **Interactive Interface**: User-friendly Streamlit web application
- **Educational Content**: Medical information and disclaimers for educational purposes

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/avneet2347/Heart-diseases-.git
   cd Heart-diseases-
   ```

2. **Use the Deployment Chatbot** (Recommended):
   ```bash
   python deploy_chatbot.py
   ```
   The chatbot will guide you through the entire deployment process, asking for all necessary details.

3. **Manual Installation**:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

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