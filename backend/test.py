from services.gemini_client import model

response = model.generate_content(
    "Say Hello"
)

print(response.text)