import json

from services.gemini_client import model
from schemas.design import DesignSchema


def design_system(intent):

    prompt = f"""
You are a software architect.

Your response MUST be valid JSON.

Do NOT explain.
Do NOT use markdown.
Do NOT use code blocks.
Do NOT write any text before or after JSON.

Based on this intent:

{intent.model_dump_json()}

Return exactly this schema:

{{
  "entities": [
    "User"
  ],
  "flows": [
    "Login"
  ]
}}

Rules:

- entities must be an array of strings
- flows must be an array of strings
- Return ONLY JSON
"""

    try:

        response = model.generate_content(
            prompt,
            generation_config={
                "response_mime_type": "application/json"
            }
        )

    except Exception as e:

        raise Exception(
            f"LLM Generation Failed: {str(e)}"
        )

    print("\n===== RAW DESIGN RESPONSE =====")
    print(response.text)

    text = response.text.strip()

    if not text:

        return DesignSchema(
            entities=["User"],
            flows=["Login"]
        )

    text = text.replace(
        "```json",
        ""
    )

    text = text.replace(
        "```",
        ""
    )

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

        return DesignSchema.model_validate(
            data
        )

    except Exception as e:

        raise Exception(
            f"Design Schema Validation Failed: {str(e)}"
        )