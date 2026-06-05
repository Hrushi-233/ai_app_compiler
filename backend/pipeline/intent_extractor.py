import json

from schemas.intent import IntentSchema
from services.gemini_client import model


def extract_intent(prompt: str):

    extraction_prompt = f"""
You are a JSON API.

Your response MUST be valid JSON.

Do NOT explain.
Do NOT use markdown.
Do NOT use code blocks.
Do NOT write any text before or after JSON.

Return exactly this schema:

{{
  "app_type": "string",
  "features": [],
  "roles": []
}}

Allowed features:

[
 "authentication",
 "contacts",
 "dashboard",
 "payments",
 "analytics",
 "subscriptions",
 "notifications"
]

Allowed roles:

[
 "admin",
 "user",
 "manager"
]

User Request:

{prompt}
"""

    try:

        response = model.generate_content(
            extraction_prompt,
            generation_config={
                "response_mime_type": "application/json"
            }
        )

    except Exception as e:

        raise Exception(
            f"LLM Generation Failed: {str(e)}"
        )

    print("\n===== RAW GEMINI RESPONSE =====")
    print(response.text)

    text = response.text.strip()

    if not text:

        return IntentSchema(
            app_type="custom_app",
            features=[],
            roles=["user"]
        )

    # remove markdown if Gemini adds it

    text = text.replace(
        "```json",
        ""
    )

    text = text.replace(
        "```",
        ""
    )

    # extract JSON only

    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:

        text = text[
            start:end + 1
        ]

    try:

        data = json.loads(text)

    except Exception:

        raise Exception(
            f"Invalid JSON from Gemini:\n{text}"
        )

    try:

        return IntentSchema.model_validate(
            data
        )

    except Exception as e:

        raise Exception(
            f"Schema Validation Failed: {str(e)}"
        )