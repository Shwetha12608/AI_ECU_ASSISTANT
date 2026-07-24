# 🚗 ECU Root Cause & Diagnostic Assistant

An AI-powered automotive diagnostic assistant that helps engineers quickly identify the root cause of ECU faults using Diagnostic Trouble Codes (DTCs), validation reports, waveform analysis, and Gemini AI.

---

## 📌 Overview

Modern vehicles contain multiple Electronic Control Units (ECUs) that continuously monitor sensors and actuators. When a fault is detected, the ECU stores a Diagnostic Trouble Code (DTC).

Diagnosing the actual cause requires engineers to analyze:

- Diagnostic Trouble Codes (DTCs)
- Validation Reports
- Sensor Waveforms
- Service Manuals

This process is often time-consuming and relies heavily on expert knowledge.

Our solution automates this workflow by combining ECU diagnostic data with AI-powered analysis to provide probable root causes and repair recommendations.

---

# 🚀 Features

✅ DTC Analysis

- Select or enter a DTC
- Displays:
  - Description
  - Vehicle System
  - Severity
  - Possible Causes
  - Symptoms
  - Recommended Actions

---

✅ Validation Report Analysis

Upload a PDF validation report.

The application:

- Extracts text from the PDF
- Detects:
  - PASS
  - FAIL
  - WARNING
- Displays report summary

---

✅ Waveform Analysis

Upload a CSV waveform.

The system calculates:

- Minimum Voltage
- Maximum Voltage
- Average Voltage

and plots the waveform for visual inspection.

---

✅ AI Root Cause Analysis

Combines:

- DTC Information
- Validation Report
- Waveform Analysis

to generate:

- Root Cause
- Confidence Score
- Repair Procedure
- Engineer Notes

using Google Gemini AI.

---

✅ AI Diagnostic Chatbot

Ask follow-up questions such as:

- Can bad wiring cause this?
- Why did the ECU detect this fault?
- How do I troubleshoot this issue?

The chatbot provides engineering explanations and troubleshooting guidance.

---

# 🏗 System Architecture

Vehicle ECU

↓

Detects Sensor Fault

↓

Stores DTC

↓

OBD-II / CAN Interface

↓

ECU Root Cause Assistant

├── DTC Analyzer

├── Validation Report Parser

├── Waveform Analyzer

└── Gemini AI

↓

Root Cause Analysis

↓

Repair Recommendation

---

# 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- PyMuPDF (fitz)
- Google Gemini AI
- Git
- GitHub

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/your_username/AI_ECU_ASSISTANT.git
```

Move into the project

```bash
cd AI_ECU_ASSISTANT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Demo Workflow

### Step 1

Select or enter a DTC.

Example:

```
P0117
```

---

### Step 2

Upload:

- Validation Report (PDF)

---

### Step 3

Upload:

- Waveform CSV

---

### Step 4

Click

```
Run Full Diagnosis
```

---

### Step 5

View:

- DTC Details
- Validation Report Status
- Waveform Statistics
- AI Root Cause
- Confidence Score
- Repair Procedure

---

### Step 6

Ask questions in the AI Chatbot.

Example:

```
Can bad wiring cause this?
```
Demo Link: 
---

# 🌍 Real World Implementation

In production, the system can connect directly to a vehicle using:

- OBD-II Interface
- CAN Bus
- UDS Diagnostics

Instead of manually uploading files, the application can automatically receive:

- Live DTCs
- Sensor Values
- Freeze Frame Data
- Validation Reports
- Oscilloscope Data

making diagnostics faster and more reliable.

---

# 🔮 Future Enhancements

- Live CAN Bus Integration
- OBD-II Scanner Support
- Predictive Maintenance
- Cloud Fleet Monitoring
- Multi-ECU Diagnostics
- Voice-enabled AI Assistant
- Mobile Application
- Digital Twin Integration

---

# 👨‍💻 Team Contributions

### Member 1

- Streamlit UI
- Dashboard Design
- System Integration

### Member 2

- DTC Database
- DTC Analyzer Module
- Diagnostic Logic
- AI Integration Support

### Member 3

- Validation Report Parser
- Waveform Analyzer
- Signal Visualization

---

# 📄 License

This project is developed for educational and hackathon purposes.

---

## 🚗 "AI-Assisted Diagnostics for Faster, Smarter, and More Reliable ECU Fault Analysis."
