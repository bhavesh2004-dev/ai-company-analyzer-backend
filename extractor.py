from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

COMPANY_SCHEMA = {
    "type": "object",
    "properties": {
        "company_name": {"type": "string"},
        "about_company": {"type": "string"},
        "services": {
            "type": "array",
            "items": {"type": "string"}
        },
        "projects_or_products": {
            "type": "array",
            "items": {"type": "string"}
        },
        "industries": {
            "type": "array",
            "items": {"type": "string"}
        },
        "technologies": {
            "type": "array",
            "items": {"type": "string"}
        },
        "team_or_employees": {"type": "string"},
        "contact": {
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "phone": {"type": "string"},
                "address": {"type": "string"}
            },
            "required": ["email", "phone", "address"],
            "additionalProperties": False
        }
    },
    "required": [
        "company_name",
        "about_company",
        "services",
        "projects_or_products",
        "industries",
        "technologies",
        "team_or_employees",
        "contact"
    ],
    "additionalProperties": False
}
 

def extract_company_info(text: str):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Extract structured company information from website content."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "company_profile",
                "schema": COMPANY_SCHEMA,
                "strict": True
            }
        }
    )

    raw_json = response.output[0].content[0].text
    return json.loads(raw_json)
