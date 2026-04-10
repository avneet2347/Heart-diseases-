#!/usr/bin/env python3
"""
Patient Data Collection Chatbot for Heart Disease Prediction
This interactive chatbot collects all patient medical information through conversation
and saves it for automatic form filling in the Streamlit application.
"""

import json
import os
from pathlib import Path

class PatientDataChatbot:
    def __init__(self):
        self.patient_data = {}
        self.project_root = Path(__file__).parent

    def ask_question(self, question, default=None, options=None, validation=None, explanation=None):
        """Ask a question and get user input with validation"""
        while True:
            print(f"\n🤖 {question}")
            if explanation:
                print(f"   💡 {explanation}")
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

    def validate_age(self, age):
        """Validate age input"""
        try:
            age_num = int(age)
            if 1 <= age_num <= 120:
                return age_num
            else:
                raise ValueError("Age must be between 1 and 120 years")
        except ValueError:
            raise ValueError("Please enter a valid age (whole number)")

    def validate_bp(self, bp):
        """Validate blood pressure input"""
        try:
            bp_num = int(bp)
            if 80 <= bp_num <= 200:
                return bp_num
            else:
                raise ValueError("Blood pressure must be between 80 and 200 mm Hg")
        except ValueError:
            raise ValueError("Please enter a valid blood pressure (whole number)")

    def validate_cholesterol(self, chol):
        """Validate cholesterol input"""
        try:
            chol_num = int(chol)
            if 100 <= chol_num <= 600:
                return chol_num
            else:
                raise ValueError("Cholesterol must be between 100 and 600 mg/dL")
        except ValueError:
            raise ValueError("Please enter a valid cholesterol level (whole number)")

    def validate_heart_rate(self, hr):
        """Validate heart rate input"""
        try:
            hr_num = int(hr)
            if 60 <= hr_num <= 220:
                return hr_num
            else:
                raise ValueError("Heart rate must be between 60 and 220 bpm")
        except ValueError:
            raise ValueError("Please enter a valid heart rate (whole number)")

    def validate_st_depression(self, st):
        """Validate ST depression input"""
        try:
            st_num = float(st)
            if 0.0 <= st_num <= 6.2:
                return st_num
            else:
                raise ValueError("ST depression must be between 0.0 and 6.2 mm")
        except ValueError:
            raise ValueError("Please enter a valid ST depression value (decimal number)")

    def collect_patient_data(self):
        """Collect all patient information through interactive questions"""

        print("🏥 Welcome to the Heart Disease Prediction Patient Data Collector!")
        print("=" * 70)
        print("I'll ask you questions about the patient's medical information.")
        print("Please answer each question carefully. You can use default values by pressing Enter.")
        print("=" * 70)

        # Patient Name (optional)
        self.patient_data['patient_name'] = self.ask_question(
            "What is the patient's name? (Optional - press Enter to skip)",
            "",
            validation=lambda x: x  # Accept any string
        )

        # Age
        self.patient_data['age'] = self.ask_question(
            "What is the patient's age in years?",
            explanation="Age is a crucial factor in heart disease risk assessment. Older age increases risk.",
            validation=self.validate_age
        )

        # Sex
        sex_options = ["0 (Male)", "1 (Female)"]
        sex_choice = self.ask_question(
            "What is the patient's sex?",
            options=sex_options,
            explanation="Biological sex affects heart disease risk patterns. Males generally have higher risk."
        )
        self.patient_data['sex'] = int(sex_choice.split()[0])

        # Chest Pain Type
        cp_options = [
            "0 (Typical Angina - chest pain during physical activity or stress)",
            "1 (Atypical Angina - chest pain not clearly related to exertion)",
            "2 (Non-anginal Pain - chest pain not related to heart)",
            "3 (Asymptomatic - no chest pain)"
        ]
        cp_choice = self.ask_question(
            "What type of chest pain does the patient experience?",
            options=[opt.split()[0] for opt in cp_options],
            explanation="Chest pain type helps determine if symptoms are cardiac-related."
        )
        self.patient_data['cp'] = int(cp_choice)

        # Resting Blood Pressure
        self.patient_data['trestbps'] = self.ask_question(
            "What is the patient's resting blood pressure in mm Hg?",
            120,
            explanation="Normal range: 90-120 mm Hg. High blood pressure is a major risk factor.",
            validation=self.validate_bp
        )

        # Cholesterol Level
        self.patient_data['chol'] = self.ask_question(
            "What is the patient's cholesterol level in mg/dL?",
            200,
            explanation="Desirable: <200 mg/dL, Borderline: 200-239 mg/dL, High: ≥240 mg/dL",
            validation=self.validate_cholesterol
        )

        # Fasting Blood Sugar
        fbs_options = [
            "0 (Normal - FBS ≤ 120 mg/dL)",
            "1 (High - FBS > 120 mg/dL)"
        ]
        fbs_choice = self.ask_question(
            "What is the patient's fasting blood sugar level?",
            options=["0", "1"],
            explanation="Elevated fasting blood sugar indicates diabetes, a heart disease risk factor."
        )
        self.patient_data['fbs'] = int(fbs_choice)

        # Resting ECG Results
        ecg_options = [
            "0 (Normal ECG)",
            "1 (ST-T wave abnormality)",
            "2 (Left Ventricular Hypertrophy - LVH)"
        ]
        ecg_choice = self.ask_question(
            "What do the resting ECG results show?",
            options=["0", "1", "2"],
            explanation="ECG abnormalities can indicate heart muscle stress or enlargement."
        )
        self.patient_data['restecg'] = int(ecg_choice)

        # Maximum Heart Rate
        self.patient_data['thalach'] = self.ask_question(
            "What is the patient's maximum heart rate achieved (bpm)?",
            explanation=f"Expected maximum: 220 - age = {220 - self.patient_data['age']} bpm. Lower than expected may indicate heart issues.",
            validation=self.validate_heart_rate
        )

        # Exercise Induced Angina
        exang_options = [
            "0 (No - no chest pain during exercise)",
            "1 (Yes - chest pain occurs during exercise)"
        ]
        exang_choice = self.ask_question(
            "Does the patient experience chest pain during exercise?",
            options=["0", "1"],
            explanation="Exercise-induced chest pain suggests coronary artery disease."
        )
        self.patient_data['exang'] = int(exang_choice)

        # ST Depression
        self.patient_data['oldpeak'] = self.ask_question(
            "What is the ST depression value in mm?",
            1.0,
            explanation="ST depression during exercise indicates heart muscle stress. 0.0-1.0 mm is mild, >2.0 mm is severe.",
            validation=self.validate_st_depression
        )

        # Slope of ST Segment
        slope_options = [
            "0 (Upsloping - ST segment rises)",
            "1 (Flat - ST segment is horizontal)",
            "2 (Downsloping - ST segment falls)"
        ]
        slope_choice = self.ask_question(
            "What is the slope of the peak exercise ST segment?",
            options=["0", "1", "2"],
            explanation="Downsloping ST segments are more concerning than upsloping ones."
        )
        self.patient_data['slope'] = int(slope_choice)

        # Number of Major Vessels
        ca_options = [
            "0 (No major vessel blockage)",
            "1 (1 vessel affected)",
            "2 (2 vessels affected)",
            "3 (3 vessels affected)"
        ]
        ca_choice = self.ask_question(
            "How many major vessels are affected?",
            options=["0", "1", "2", "3"],
            explanation="More affected vessels indicate more severe coronary artery disease."
        )
        self.patient_data['ca'] = int(ca_choice)

        # Thalium/Thalassemia
        thal_options = [
            "1 (Normal thalium scan)",
            "2 (Fixed defect - permanent damage)",
            "3 (Reversible defect - ischemia)"
        ]
        thal_choice = self.ask_question(
            "What do the thalium stress test results show?",
            options=["1", "2", "3"],
            explanation="Thalium scan shows blood flow to heart muscle. Reversible defects indicate coronary artery disease."
        )
        self.patient_data['thal'] = int(thal_choice)

    def save_patient_data(self):
        """Save the collected patient data to a JSON file"""
        data_file = self.project_root / 'patient_data.json'

        # Add metadata
        self.patient_data['collected_at'] = str(Path(__file__).stat().st_mtime)
        self.patient_data['data_version'] = '1.0'

        with open(data_file, 'w') as f:
            json.dump(self.patient_data, f, indent=2)

        print(f"\n✅ Patient data saved to {data_file}")
        return data_file

    def display_summary(self):
        """Display a summary of collected data"""
        print("\n📋 PATIENT DATA SUMMARY")
        print("=" * 40)

        if self.patient_data.get('patient_name'):
            print(f"Patient Name: {self.patient_data['patient_name']}")

        print(f"Age: {self.patient_data['age']} years")
        print(f"Sex: {'Female' if self.patient_data['sex'] == 1 else 'Male'}")
        print(f"Chest Pain Type: {self.patient_data['cp']}")
        print(f"Blood Pressure: {self.patient_data['trestbps']} mm Hg")
        print(f"Cholesterol: {self.patient_data['chol']} mg/dL")
        print(f"Fasting Blood Sugar: {'High' if self.patient_data['fbs'] == 1 else 'Normal'}")
        print(f"Resting ECG: {self.patient_data['restecg']}")
        print(f"Max Heart Rate: {self.patient_data['thalach']} bpm")
        print(f"Exercise Angina: {'Yes' if self.patient_data['exang'] == 1 else 'No'}")
        print(f"ST Depression: {self.patient_data['oldpeak']} mm")
        print(f"ST Slope: {self.patient_data['slope']}")
        print(f"Major Vessels Affected: {self.patient_data['ca']}")
        print(f"Thalium Result: {self.patient_data['thal']}")

    def run(self):
        """Main execution flow"""
        try:
            self.collect_patient_data()
            self.display_summary()

            # Confirm and save
            confirm = self.ask_question(
                "Does this information look correct? (yes/no)",
                "yes",
                validation=lambda x: x.lower() in ['yes', 'y', 'true', '1']
            )

            if confirm:
                data_file = self.save_patient_data()
                print("
🎉 Data collection complete!"                print(f"📁 Data saved to: {data_file}")
                print("🚀 You can now run the heart disease prediction app to see the results!")
                print("   Run: streamlit run app.py --server.port 8502")
            else:
                print("\n❌ Data collection cancelled. Please run this script again.")

        except KeyboardInterrupt:
            print("\n\n👋 Data collection stopped by user.")
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    chatbot = PatientDataChatbot()
    chatbot.run()