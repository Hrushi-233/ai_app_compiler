import json

from services.gemini_client import model


def generate_schema(design):

    prompt = f"""
You are a software application compiler.

Your response MUST be valid JSON.

Do NOT explain.
Do NOT use markdown.
Do NOT use code blocks.
Do NOT write any text before or after JSON.

Given this application design:

{design.model_dump_json()}

Generate a complete application schema.

Return exactly this structure:

{{
  "ui": {{
    "pages": [
      {{
        "name": "",
        "route": ""
      }}
    ]
  }},

  "api": {{
    "endpoints": [
      {{
        "path": "",
        "method": ""
      }}
    ]
  }},

  "db": {{
    "tables": [
      {{
        "name": "",
        "fields": [
          {{
            "name": "",
            "type": ""
          }}
        ]
      }}
    ]
  }},

  "auth": {{
    "roles": [
      {{
        "name": "",
        "permissions": []
      }}
    ]
  }}
}}
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

    print("\n===== RAW SCHEMA RESPONSE =====")
    print(response.text)

    text = response.text.strip()

    if not text:

        raise Exception(
            "Empty response from Gemini"
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

    return data