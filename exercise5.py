import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

while True:
    userEntry = input("> ")
    if userEntry.lower() == "exit":
        break
    response = model.generate_content(
        userEntry,
        generation_config=genai.types.GenerationConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "longitude": {"type": "number"},
                    "lattitude": {"type": "number"}
                }
            }
        ))
    print(response.text)
