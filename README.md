🚀 AI-Powered Lead Automation System
📌 Overview

This project is an AI-powered automation system that:

Processes incoming leads
Enriches lead data
Classifies user intent
Stores results automatically

Built using n8n and FastAPI, it enables scalable and intelligent lead handling.

⚙️ Tech Stack
n8n – Workflow Automation
FastAPI – Backend APIs
Google Sheets – Data Storage
🔁 Workflow
Webhook → Validation → Enrichment API → Classification API → Merge → Storage → Notification
🚀 Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/ai-lead-automation-system.git
cd ai-lead-automation-system
2. Run Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

Server will run at:

http://127.0.0.1:8000
🔌 API Endpoints
📥 POST /enrich

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
📥 POST /classify

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
FastAPI manages business logic
Google Sheets stores processed leads

⚡ System Design
Scalability
Supports high-volume lead processing
Can integrate Redis + Celery for async execution
Reliability
Retry mechanisms for API calls
Execution logging via n8n
Idempotency
Email used as a unique identifier to prevent duplicates

📤 Push Code to GitHub
git init
git add .
git commit -m "Initial commit - AI Lead Automation System"
git branch -M main
git remote add origin https://github.com/your-username/ai-lead-automation-system.git
git push -u origin main
🎯 Final Checklist

Before submitting:

✅ FastAPI code uploaded
✅ n8n workflow JSON added
✅ README completed
✅ Repository is public
✅ Loom demo video ready
