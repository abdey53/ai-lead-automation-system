# AI-Powered Lead Automation System

## 📌 Overview
This project is an AI-powered automation system that processes incoming leads, enriches data, classifies intent, and stores results using n8n and FastAPI.

---

## ⚙️ Tech Stack
- n8n (Workflow Automation)
- FastAPI (Backend APIs)
- Google Sheets (Storage)

---

## 🔁 Workflow
Webhook → Validation → Enrichment API → Classification API → Merge → Storage → Notification

---

2. Run Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

Server runs at:

http://127.0.0.1:8000
🔌 API Endpoints
POST /enrich

Input:

{
  "name": "John Doe",
  "email": "john@test.com",
  "company": "ABC"
}

Output:

{
  "linkedin_url": "...",
  "company_size": "51-200",
  "industry": "Technology"
}
POST /classify

Input:

{
  "message": "I am interested in your services"
}

Output:

{
  "intent": "sales_enquiry",
  "confidence": 0.92
}
🧠 Architecture
n8n handles workflow orchestration
FastAPI handles business logic
Google Sheets stores processed leads
⚡ System Design
Scalability
Can use Redis + Celery for async processing
Supports high volume lead processing
Reliability
Retry mechanism in API calls
Logging via n8n executions
Idempotency
Email used as unique identifier to avoid duplicates

---

# 📤 STEP 6: Push Code

In terminal:

```bash
git init
git add .
git commit -m "Initial commit - AI Lead Automation System"
git branch -M main
git remote add origin https://github.com/your-username/ai-lead-automation-system.git
git push -u origin main
🎯 FINAL CHECKLIST

Before submitting:

✅ FastAPI code uploaded
✅ n8n JSON uploaded
✅ README added
✅ Repo public
✅ Loom video ready

## 🚀 Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/your-username/ai-lead-automation-system.git
cd ai-lead-automation-system
