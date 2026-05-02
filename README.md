# 🚀 AI-Powered Lead Automation System

## 📌 Overview
This project is an end-to-end automation pipeline that processes incoming leads, enriches data, classifies user intent, stores structured output, and sends notifications automatically.

---

## 🛠️ Tech Stack
- n8n (Workflow Automation)
- FastAPI (Backend APIs)
- Google Sheets (Data Storage)
- SMTP Email (Notification)

---

## ⚙️ Setup Instructions

### 1️⃣ Run Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
