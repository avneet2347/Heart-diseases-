# Heart Disease Prediction System - Makefile
# Professional development workflow management

.PHONY: help install run test clean docker-build docker-run docs format lint

# Default target
help: ## Show this help message
	@echo "Heart Disease Prediction System - Development Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Installation
install: ## Install Python dependencies
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	@echo "🔧 Installing development dependencies..."
	pip install -r requirements.txt
	pip install pytest black flake8 mkdocs

# Running the application
run: ## Run the Streamlit application locally
	@echo "🚀 Starting Heart Disease Prediction System..."
	streamlit run app.py

run-docker: ## Run the application using Docker
	@echo "🐳 Starting application with Docker..."
	docker-compose up --build

# Testing
test: ## Run all tests
	@echo "🧪 Running tests..."
	pytest tests/ -v --cov=.

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	pytest tests/unit/ -v

test-integration: ## Run integration tests
	@echo "🔗 Running integration tests..."
	pytest tests/integration/ -v

# Code Quality
format: ## Format code with Black
	@echo "🎨 Formatting code..."
	black . --line-length 88

lint: ## Lint code with Flake8
	@echo "🔍 Linting code..."
	flake8 . --max-line-length 88 --extend-ignore E203,W503

quality: format lint ## Run both formatting and linting

# Docker
docker-build: ## Build Docker image
	@echo "🏗️ Building Docker image..."
	docker build -t heart-disease-prediction .

docker-run: ## Run Docker container
	@echo "🐳 Running Docker container..."
	docker run -p 8501:8501 heart-disease-prediction

docker-clean: ## Clean Docker resources
	@echo "🧹 Cleaning Docker resources..."
	docker-compose down -v
	docker system prune -f

# Documentation
docs: ## Build and serve documentation
	@echo "📚 Building documentation..."
	mkdocs build
	mkdocs serve

docs-build: ## Build documentation only
	@echo "📚 Building documentation..."
	mkdocs build

# Data and Model
train-model: ## Re-train the machine learning model
	@echo "🧠 Training model..."
	python -m src.model.train

validate-model: ## Validate model performance
	@echo "📊 Validating model..."
	python -m src.model.validate

# Deployment
deploy-dev: ## Deploy to development environment
	@echo "🚀 Deploying to development..."
	# Add your deployment commands here

deploy-prod: ## Deploy to production environment
	@echo "🚀 Deploying to production..."
	# Add your production deployment commands here

# Cleanup
clean: ## Clean up temporary files and caches
	@echo "🧹 Cleaning up..."
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

clean-all: clean docker-clean ## Clean everything including Docker

# Health checks
health-check: ## Check application health
	@echo "❤️ Checking application health..."
	curl -f http://localhost:8501/health || echo "Application not running"

# Development setup
setup-dev: install-dev ## Set up development environment
	@echo "🔧 Setting up development environment..."
	pre-commit install
	@echo "✅ Development environment ready!"

# CI/CD
ci: quality test ## Run CI pipeline locally
	@echo "🔄 Running CI pipeline..."
	make quality
	make test

# Information
info: ## Show project information
	@echo "🫀 Heart Disease Prediction System"
	@echo "=================================="
	@echo "Python Version: $$(python --version)"
	@echo "Streamlit Version: $$(python -c "import streamlit; print(streamlit.__version__)")"
	@echo "Scikit-learn Version: $$(python -c "import sklearn; print(sklearn.__version__)")"
	@echo "Model Accuracy: 87.04%"
	@echo "=================================="

# Security
security-scan: ## Run security scan
	@echo "🔒 Running security scan..."
	# Add security scanning commands here
	safety check

# Backup
backup: ## Create backup of model and data
	@echo "💾 Creating backup..."
	tar -czf backup_$$(date +%Y%m%d_%H%M%S).tar.gz \
		model.pkl \
		Heart_Disease_Prediction.csv \
		requirements.txt \
		app.py \
		notebook.ipynb

# Monitoring
logs: ## Show application logs
	@echo "📋 Showing application logs..."
	docker-compose logs -f heart-prediction