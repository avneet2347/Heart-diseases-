# Heart Disease Prediction System - Docker Configuration
# Professional containerized deployment for healthcare applications

FROM python:3.9-slim

# Metadata
LABEL maintainer="Heart Disease Prediction Team <support@heartprediction.ai>"
LABEL version="1.0.0"
LABEL description="AI-powered heart disease risk prediction system"
LABEL org.opencontainers.image.source="https://github.com/your-username/heart-disease-prediction"

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Create non-root user for security
RUN groupadd -r healthcare && useradd -r -g healthcare healthcare

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/logs && \
    chown -R healthcare:healthcare /app

# Switch to non-root user
USER healthcare

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import streamlit; print('Health check passed')" || exit 1

# Expose port
EXPOSE 8501

# Default command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Security notes:
# - Runs as non-root user
# - Minimal base image
# - No sensitive data in image
# - Health checks implemented
# - Proper labeling for container management