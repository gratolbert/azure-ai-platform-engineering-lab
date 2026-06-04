import os
import json
import logging

import azure.functions as func
from openai import AzureOpenAI

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="summarize")
def summarize(req: func.HttpRequest) -> func.HttpResponse:

    try:
        body = req.get_json()

        text = body.get("text", "")

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "No text provided"}),
                status_code=400,
                mimetype="application/json"
            )

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
                    "content": "You are an IT service desk assistant. Summarize tickets clearly and professionally."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            max_tokens=300
        )

        summary = response.choices[0].message.content

        return func.HttpResponse(
            json.dumps({"summary": summary}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as ex:
        logging.exception(ex)

        return func.HttpResponse(
            json.dumps({"error": str(ex)}),
            status_code=500,
            mimetype="application/json"
        )