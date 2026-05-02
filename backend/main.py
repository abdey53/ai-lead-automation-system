from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Lead(BaseModel):
    name: str
    email: str
    company: str

class Message(BaseModel):
    message: str

@app.get('/')
def home():
    return {"message": "API is running"}

#Enrichment Api
@app.post('/enrich')
def enrich(data: Lead):
    return {
        "linkedin_url": f'https://linkedin.com/in/{data.name.replace(' ', '').lower()}',
        "company_size": "51-200",
        "industry": "Technology"
    }

@app.post('/classify')
def classify(msg: Message):
    text = msg.message.lower()

    if 'interested' in text:
        return {'intent': 'sales_enquiry', 'confidence':0.9}
    elif "price" in text:
        return {'intent': 'pricing_query', 'confidence': 0.9}
    else:
        return {'intent': 'general_query', 'confidence': 0.7}

