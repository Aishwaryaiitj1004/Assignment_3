# 🌸 Auto-Scaling VM Project (Flower Shop Demo)

## 📌 Project Overview

This project demonstrates a simple **auto-scaling mechanism** where a local Virtual Machine (VM) monitors its resource usage and automatically creates a new VM in the cloud when CPU usage exceeds a defined threshold (75%).

---

## 🖥️ Local Environment Setup

* Virtual Machine created using **Oracle VirtualBox**
* Operating System: **Ubuntu 22.04 LTS**
* Python environment configured using **venv**

---

## 🌸 Sample Application (Flower Shop)

A simple Flask-based web application (`app.py`) simulates a flower shop.

* Users can simulate:

  * ✅ Normal traffic (10 users)
  * 🔥 High traffic (1000+ users)

When high traffic is triggered:

* The system uses the `stress` tool to increase CPU usage
* This simulates a real-world sudden spike in user requests (e.g., flash sale)

---

## ⚙️ Monitoring & Auto-Scaling

The `monitor.py` script continuously monitors CPU usage using the `psutil` library.

### Workflow:

1. Monitor CPU usage every few seconds
2. If CPU usage exceeds **75%**
3. Automatically trigger cloud scaling
4. Create a new VM instance in Google Cloud Platform (GCP) using **gcloud CLI**

---

## ☁️ Cloud Integration

* Cloud Platform: **Google Cloud Platform (GCP)**
* Tool used: **Google Cloud SDK (gcloud CLI)**
* VM is created dynamically using command-line automation

---

## 🔄 System Flow

Local VM → Monitor CPU → High Load Detected → Trigger gcloud → Create Cloud VM

---

## 📦 Technologies & Packages Used

### System Tools:

* Python 3
* Virtual Environment (venv)
* stress (for CPU load simulation)
* htop (optional monitoring tool)

### Python Libraries:

* Flask → Web application
* psutil → Resource monitoring
* subprocess → Execute gcloud commands
* datetime → Generate unique VM names
* logging → Track system activity

### Cloud Tools:

* Google Cloud SDK (gcloud CLI)

---

## ▶️ How to Run

### 1. Activate virtual environment

```
source myenv/bin/activate
```

### 2. Run Flask app

```
python3 app.py
```

### 3. Run monitoring script

```
python3 monitor.py
```

### 4. Simulate high load

* Open browser → `http://localhost:5000`
* Click **FLASH SALE (1000 users)**

---

## 🎯 Expected Output

* CPU usage increases above 75%
* `monitor.py` detects spike
* New VM instance is automatically created in GCP

---

## 📽️ Demonstration

The project demonstrates:

* Local application deployment
* Resource monitoring
* Trigger-based auto-scaling
* Cloud VM provisioning


