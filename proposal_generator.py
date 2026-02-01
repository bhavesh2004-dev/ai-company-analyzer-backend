# proposal_generator.py

from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROPOSAL_SCHEMA = {
    "type": "object",
    "properties": {
        "subject": {
            "type": "string",
            "description": "Email subject line"
        },
        "email_body": {
            "type": "string",
            "description": "Professional proposal email body"
        }
    },
    "required": ["subject", "email_body"],
    "additionalProperties": False
}

def generate_proposal(company_profile: dict):
    """
    Generates a structured outreach proposal based on company profile
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are a business development expert. "
                    "Generate a professional outreach proposal based on the company profile."
                )
            },
            {
                "role": "user",
                "content": f"Company profile:\n{company_profile}"
            }
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "company_proposal",
                "schema": PROPOSAL_SCHEMA,
                "strict": True
            }
        }
    )

    # ✅ THESE LINES MUST BE INSIDE THE FUNCTION
    raw_json = response.output[0].content[0].text
    return json.loads(raw_json)
