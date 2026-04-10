#!/usr/bin/env python3
"""
Interactive Deployment Chatbot for Heart Disease Prediction App
This script guides users through the deployment process by asking detailed questions
and configuring the application accordingly.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

class DeploymentChatbot:
    def __init__(self):
        self.config = {}
        self.project_root = Path(__file__).parent

    def ask_question(self, question, default=None, options=None, validation=None):
        """Ask a question and get user input with validation"""
        while True:
            print(f"\n🤖 {question}")
            if default:
                print(f"   Default: {default}")
            if options:
                print(f"   Options: {', '.join(options)}")

            answer = input("👤 Your answer: ").strip()

            if not answer and default:
                answer = default

            if not answer:
                print("❌ Please provide an answer.")
                continue

            if options and answer.lower() not in [opt.lower() for opt in options]:
                print(f"❌ Please choose from: {', '.join(options)}")
                continue

            if validation:
                try:
                    answer = validation(answer)
                except ValueError as e:
                    print(f"❌ {e}")
                    continue

            return answer

    def validate_port(self, port):
        """Validate port number"""
        try:
            port_num = int(port)
            if 1024 <= port_num <= 65535:
                return port_num
            else:
                raise ValueError("Port must be between 1024 and 65535")
        except ValueError:
            raise ValueError("Please enter a valid port number")

    def validate_yes_no(self, answer):
        """Validate yes/no answers"""
        if answer.lower() in ['yes', 'y', 'true', '1']:
            return True
        elif answer.lower() in ['no', 'n', 'false', '0']:
            return False
        else:
            raise ValueError("Please answer yes or no")

    def check_dependencies(self):
        """Check if required dependencies are installed"""
        print("\n🔍 Checking system dependencies...")

        required_commands = ['python', 'pip']
        missing = []

        for cmd in required_commands:
            try:
                subprocess.run([cmd, '--version'], capture_output=True, check=True)
                print(f"✅ {cmd} is available")
            except (subprocess.CalledProcessError, FileNotFoundError):
                missing.append(cmd)
                print(f"❌ {cmd} is not available")

        if missing:
            print(f"\n⚠️  Missing dependencies: {', '.join(missing)}")
            install = self.ask_question("Would you like me to help install missing dependencies?", "yes", validation=self.validate_yes_no)
            if install:
                self.install_system_dependencies(missing)
            else:
                print("❌ Please install missing dependencies manually and run this script again.")
                sys.exit(1)

    def install_system_dependencies(self, missing):
        """Install system dependencies"""
        print("\n📦 Installing system dependencies...")

        # This is a basic implementation - in reality, you'd need package managers
        if 'python' in missing:
            print("Please install Python from https://python.org")
        if 'pip' in missing:
            print("Please install pip following Python installation")

    def gather_deployment_info(self):
        """Gather all deployment information through questions"""

        print("🚀 Welcome to the Heart Disease Prediction App Deployment Assistant!")
        print("=" * 60)

        # Basic project info
        self.config['app_name'] = self.ask_question(
            "What is the name of your application?",
            "Heart Disease Prediction App"
        )

        # Deployment type
        deployment_types = ['local', 'docker', 'cloud', 'server']
        self.config['deployment_type'] = self.ask_question(
            "What type of deployment do you want?",
            "local",
            options=deployment_types
        )

        # Environment
        environments = ['development', 'staging', 'production']
        self.config['environment'] = self.ask_question(
            "Which environment are you deploying to?",
            "development",
            options=environments
        )

        # Port configuration
        if self.config['deployment_type'] == 'local':
            self.config['port'] = self.ask_question(
                "Which port would you like to use for the Streamlit app?",
                8501,
                validation=self.validate_port
            )

        # Database configuration
        self.config['use_database'] = self.ask_question(
            "Do you need a database for this application?",
            "no",
            validation=self.validate_yes_no
        )

        if self.config['use_database']:
            db_types = ['sqlite', 'postgresql', 'mysql', 'mongodb']
            self.config['database_type'] = self.ask_question(
                "Which database type do you want to use?",
                "sqlite",
                options=db_types
            )

            if self.config['database_type'] != 'sqlite':
                self.config['db_host'] = self.ask_question("Database host?", "localhost")
                self.config['db_port'] = self.ask_question("Database port?", validation=self.validate_port)
                self.config['db_name'] = self.ask_question("Database name?")
                self.config['db_user'] = self.ask_question("Database username?")
                self.config['db_password'] = self.ask_question("Database password?", validation=lambda x: x)  # Basic validation

        # Authentication
        self.config['use_auth'] = self.ask_question(
            "Do you want to add user authentication?",
            "no",
            validation=self.validate_yes_no
        )

        if self.config['use_auth']:
            auth_types = ['basic', 'oauth', 'jwt']
            self.config['auth_type'] = self.ask_question(
                "Which authentication method?",
                "basic",
                options=auth_types
            )

        # Monitoring and logging
        self.config['enable_monitoring'] = self.ask_question(
            "Do you want to enable monitoring and logging?",
            "yes",
            validation=self.validate_yes_no
        )

        # API endpoints
        self.config['enable_api'] = self.ask_question(
            "Do you want to expose API endpoints?",
            "no",
            validation=self.validate_yes_no
        )

        if self.config['enable_api']:
            self.config['api_port'] = self.ask_question(
                "Which port for the API?",
                8000,
                validation=self.validate_port
            )

        # Security settings
        self.config['enable_https'] = self.ask_question(
            "Do you want to enable HTTPS?",
            "no",
            validation=self.validate_yes_no
        )

        # Performance settings
        self.config['max_upload_size'] = self.ask_question(
            "Maximum file upload size in MB?",
            50,
            validation=lambda x: int(x) if int(x) > 0 else 50
        )

        # Backup settings
        self.config['enable_backups'] = self.ask_question(
            "Do you want to enable automatic backups?",
            "yes",
            validation=self.validate_yes_no
        )

        if self.config['enable_backups']:
            self.config['backup_frequency'] = self.ask_question(
                "How often should backups run?",
                "daily",
                options=['hourly', 'daily', 'weekly', 'monthly']
            )

        # Notification settings
        self.config['enable_notifications'] = self.ask_question(
            "Do you want to enable email notifications?",
            "no",
            validation=self.validate_yes_no
        )

        if self.config['enable_notifications']:
            self.config['notification_email'] = self.ask_question("Notification email address?")

        # Scaling options
        if self.config['deployment_type'] in ['cloud', 'server']:
            self.config['auto_scaling'] = self.ask_question(
                "Do you want to enable auto-scaling?",
                "no",
                validation=self.validate_yes_no
            )

    def generate_config_files(self):
        """Generate configuration files based on user answers"""

        print("\n📝 Generating configuration files...")

        # Streamlit config
        streamlit_config = f"""
[server]
port = {self.config.get('port', 8501)}
maxUploadSize = {self.config.get('max_upload_size', 50)}
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
"""

        config_dir = self.project_root / '.streamlit'
        config_dir.mkdir(exist_ok=True)

        with open(config_dir / 'config.toml', 'w') as f:
            f.write(streamlit_config)

        print("✅ Created .streamlit/config.toml")

        # Environment variables
        env_vars = {
            'ENVIRONMENT': self.config['environment'],
            'APP_NAME': self.config['app_name'],
        }

        if self.config.get('use_database'):
            env_vars.update({
                'DB_TYPE': self.config['database_type'],
                'DB_HOST': self.config.get('db_host', ''),
                'DB_PORT': str(self.config.get('db_port', '')),
                'DB_NAME': self.config.get('db_name', ''),
                'DB_USER': self.config.get('db_user', ''),
                'DB_PASSWORD': self.config.get('db_password', ''),
            })

        if self.config.get('enable_api'):
            env_vars['API_PORT'] = str(self.config['api_port'])

        # Create .env file
        env_content = '\n'.join([f'{k}={v}' for k, v in env_vars.items()])

        with open(self.project_root / '.env', 'w') as f:
            f.write(env_content)

        print("✅ Created .env file")

        # Docker configuration if needed
        if self.config['deployment_type'] == 'docker':
            dockerfile_content = f"""
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE {self.config.get('port', 8501)}

CMD ["streamlit", "run", "app.py", "--server.port", "{self.config.get('port', 8501)}", "--server.address", "0.0.0.0"]
"""

            with open(self.project_root / 'Dockerfile', 'w') as f:
                f.write(dockerfile_content)

            docker_compose_content = f"""
version: '3.8'

services:
  heart-disease-app:
    build: .
    ports:
      - "{self.config.get('port', 8501)}:{self.config.get('port', 8501)}"
    environment:
      - ENVIRONMENT={self.config['environment']}
    volumes:
      - .:/app
"""

            with open(self.project_root / 'docker-compose.yml', 'w') as f:
                f.write(docker_compose_content)

            print("✅ Created Dockerfile and docker-compose.yml")

    def install_python_dependencies(self):
        """Install Python dependencies"""
        print("\n🐍 Installing Python dependencies...")

        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
            print("✅ Python dependencies installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies: {e}")
            return False
        return True

    def run_deployment(self):
        """Execute the deployment based on configuration"""
        print(f"\n🚀 Starting deployment for {self.config['app_name']}...")

        if self.config['deployment_type'] == 'local':
            print("🌐 Starting Streamlit app locally...")

            cmd = [
                sys.executable, '-m', 'streamlit', 'run', 'app.py',
                '--server.port', str(self.config.get('port', 8501))
            ]

            try:
                print(f"📱 App will be available at: http://localhost:{self.config['port']}")
                subprocess.run(cmd)
            except KeyboardInterrupt:
                print("\n🛑 Application stopped by user")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to start application: {e}")

        elif self.config['deployment_type'] == 'docker':
            print("🐳 Building and running Docker container...")

            try:
                subprocess.run(['docker-compose', 'up', '--build'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"❌ Docker deployment failed: {e}")

        else:
            print(f"📋 Configuration saved for {self.config['deployment_type']} deployment")
            print("Please follow your deployment platform's instructions")

    def save_config(self):
        """Save the configuration for future reference"""
        config_file = self.project_root / 'deployment_config.json'

        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

        print(f"✅ Configuration saved to {config_file}")

    def run(self):
        """Main execution flow"""
        try:
            self.check_dependencies()
            self.gather_deployment_info()
            self.generate_config_files()
            self.save_config()

            if not self.install_python_dependencies():
                return

            deploy_now = self.ask_question(
                "Would you like to deploy the application now?",
                "yes",
                validation=self.validate_yes_no
            )

            if deploy_now:
                self.run_deployment()
            else:
                print("\n📋 Configuration complete! Run this script again or manually start deployment.")

        except KeyboardInterrupt:
            print("\n\n👋 Deployment assistant stopped by user. Your progress has been saved.")
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Please try again or contact support.")

if __name__ == "__main__":
    chatbot = DeploymentChatbot()
    chatbot.run()