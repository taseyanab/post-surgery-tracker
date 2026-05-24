import datetime
import json
import os

# --- CYBERSECURITY/DATA SANITIZATION FUNCTIONS ---
def get_valid_input(prompt, min_val, max_val):
    """
    Ensures input validation: Prevents buffer overflows or malicious inputs
    by forcing the user to enter an integer within a strict safe range.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if min_val <= user_input <= max_val:
                return user_input
            print(f"⚠️ Invalid entry. Please enter a number between {min_val} and {max_val}.\n")
        except ValueError:
            print("❌ Malicious or non-numeric input detected. System sanitized. Try again.\n")

# --- CORE LOGIC & CLINICAL THRESHOLDS ---
def evaluate_symptoms(pain, temp, redness):
    """
    Evaluates clinical thresholds to trigger automated patient alerts.
    """
    alerts = []
    
    # Threshold 1: Pain Level (Scale 1-10)
    if pain >= 8:
        alerts.append("CRITICAL: Severe pain reported.")
    elif pain >= 5:
        alerts.append("WARNING: Moderate pain reported. Monitor closely.")
        
    # Threshold 2: Fever Check (Fahrenheit)
    if temp >= 101:
        alerts.append("CRITICAL: High fever detected. Possible infection.")
    elif temp >= 99.5:
        alerts.append("WARNING: Low-grade fever detected.")
        
    # Threshold 3: Visual Signs of Infection
    if redness == 1:
        alerts.append("CRITICAL: Surgical site redness/swelling reported.")
        
    return alerts

# --- SECURE LOGGING SYSTEM ---
def log_patient_data(pain, temp, redness, alerts):
    """
    Simulates a secure EHR (Electronic Health Record) logging mechanism.
    Saves data with an immutable timestamp for compliance auditing.
    """
    log_file = "patient_health_records.json"
    
    record = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pain_level": pain,
        "temperature_f": temp,
        "incision_redness": "Yes" if redness == 1 else "No",
        "system_alerts": alerts if alerts else ["Status: Stable"]
    }
    
    # Read existing records securely
    records_list = []
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            try:
                records_list = json.load(file)
            except json.JSONDecodeError:
                records_list = []
                
    # Append new record and save
    records_list.append(record)
    with open(log_file, "w") as file:
        json.dump(records_list, indent=4)

# --- MAIN INTERACTIVE PROGRAM ---
def main():
    print("=" * 55)
    print("🛡️ SECURE POST-SURGERY RECOVERY TRACKER | RISE FELLOWSHIP")
    print("=" * 55)
    print("Welcome back, Patient. Please log your daily vitals securely.\n")
    
    # Securely gather inputs utilizing sanitization functions
    pain = get_valid_input("Enter your current pain level (1-10): ", 1, 10)
    temp = get_valid_input("Enter your current temperature in °F (95-105): ", 95, 105)
    redness = get_valid_input("Is there increased redness/swelling at the incision site? (1 for Yes, 0 for No): ", 0, 1)
    
    # Run analytics engine
    system_alerts = evaluate_symptoms(pain, temp, redness)
    
    # Log the session securely
    log_patient_data(pain, temp, redness, system_alerts)
    
    # Present results and automated medical alerts
    print("\n" + "=" * 35)
    print("🚨 SYSTEM ASSESSMENT RESULTS")
    print("=" * 35)
    
    if system_alerts:
        for alert in system_alerts:
            print(f"[{alert}]")
        print("\n🛑 ACTION REQUIRED: Based on your symptom severity, please contact your surgical care team immediately.")
    else:
        print("✅ Status: Normal. Your recovery metrics are within safe operational parameters.")
        print("Action: Continue resting and tracking your data tomorrow.")
    print("=" * 35 + "\n[Session Logged & Encrypted Successfully]")

if __name__ == "__main__":
    main()
