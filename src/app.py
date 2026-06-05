from fastapi import FastAPI
from pydantic import BaseModel
from openai import AzureOpenAI
import os

app = FastAPI(title="Azure AI Platform API")


class TicketRequest(BaseModel):
    text: str


@app.get("/")
def health_check():
    return {"status": "healthy"}


@app.post("/summarize")
def summarize_ticket(request: TicketRequest):

    client = AzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version="2025-01-01-preview",
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
    )

    response = client.chat.completions.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        messages=[
            {
                "role": "system",
                "content": "You are an IT service desk assistant. Summarize support tickets clearly and professionally."
            },
            {
                "role": "user",
                "content": request.text
            }
        ],
        max_tokens=300
    )

    return {
        "summary": response.choices[0].message.content
    }
