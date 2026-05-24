# 🛡️ Secure Post-Surgery Recovery Tracker

An automated medical threshold tracking script built with built-in data sanitization, input validation, and secure log management. This project represents the software development execution phase of my **RISE in Computing Fellowship** project at Georgia State University.

## 🛠️ Cyber & Data Features Implemented
* **Input Sanitization:** Utilizes robust error handling (`try/except`) to filter out non-numeric or malicious string injections, mitigating system crash exploits.
* **Automated Clinical Threshold Logic:** Evaluates multiple health metric thresholds (Fahrenheit temperature, pain scales, visual metrics) to instantly trigger automated emergency alerts.
* **Immutable Compliance Auditing:** Generates and appends structured JSON logs with system-generated timestamps to simulate secure Electronic Health Record (EHR) entry logging.

## 🖥️ How to Run Locally
Ensure you have Python 3 installed, then execute the script via terminal:
```bash
python tracker.py
