# AI-Powered Healthcare Assistant (Basic Version)

import random

# Simulated IoT data
def get_iot_data():
    return {
        "heart_rate": random.randint(60, 100),         # bpm
        "temperature": round(random.uniform(97.0, 102.0), 1),  # °F
        "oxygen_level": random.randint(90, 100)        # %
    }

# Simple symptom checker
def diagnose(symptoms, iot_data):
    if "fever" in symptoms and iot_data["temperature"] > 99.5:
        return "You may have a fever or flu. Please rest and stay hydrated."
    elif "cough" in symptoms and iot_data["oxygen_level"] < 94:
        return "You may be showing early signs of a respiratory infection."
    elif "headache" in symptoms:
        return "It could be due to stress or dehydration."
    elif "chest pain" in symptoms:
        return "Chest pain requires immediate medical attention. Please visit a doctor."
    else:
        return "Your symptoms are not conclusive. Please consult a healthcare professional."

# Chatbot Loop
def chatbot():
    print("Welcome to the AI-Powered Healthcare Assistant.")
    user_input = input("Please describe your symptoms (e.g., fever, cough, headache): ").lower()
    symptoms = [s.strip() for s in user_input.split(",")]

    print("\nCollecting real-time health data from IoT devices...")
    iot_data = get_iot_data()
    print(f"Heart Rate: {iot_data['heart_rate']} bpm")
    print(f"Temperature: {iot_data['temperature']} °F")
    print(f"Oxygen Level: {iot_data['oxygen_level']}%\n")

    diagnosis = diagnose(symptoms, iot_data)
    print("AI Diagnosis:", diagnosis)

if _name_ == "_main_":
    chatbot()
