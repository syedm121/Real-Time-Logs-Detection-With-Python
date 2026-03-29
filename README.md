# 🔍 Real-Time Brute Force Detection System (Windows Event Logs)

## 🚀 Overview
This project is a real-time security monitoring system built in Python that detects brute-force login attempts by analyzing Windows Security Event Logs.

It reads logs directly from the Windows API using `pywin32` and identifies multiple failed login attempts (Event ID 4625) within a defined time window.

---

## 🧠 Features
- Real-time monitoring of Windows Security logs  
- Detection of failed login attempts (Event ID 4625)  
- Threshold-based brute force detection  
- Sliding time window analysis  
- Modular architecture (event reader, detector, alerts)  
- No log file storage required (efficient and lightweight)  

---

## 🏗️ Project Structure
├── main.py
├── event_reader.py
├── detector.py
├── alerts.py
└── config.py


---

## ⚙️ Requirements

- Windows OS  
- Python 3.x  
- pywin32  

Install dependency:

```bash
pip install pywin32


▶️ How to Run

⚠️ Run the terminal as Administrator

python main.py

🚨 Example Output
🔍 Monitoring Windows Security Logs...

[!] Failed login | User: admin | Time: 2026-03-27 09:12:33

🧠 Concepts Demonstrated
Windows Event Log Analysis
Real-Time Monitoring
Detection Engineering Basics
Security Event Correlation
Python System Programming

