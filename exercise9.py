import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

while True:
    userEntry = input("> ")
    if userEntry.lower() == "exit":
        break

    prompt = f"""Transle text from English to Polish, responding in a JSON object with 'English' and 'Polish' fields containing original and translated text respectively.
    **English text to translate**: {userEntry}"""

    response = model.generate_content(
        userEntry,
        generation_config=genai.types.GenerationConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "English": {"type": "string"},
                    "Polish": {"type": "string"}
                }
            }
        ))
    print(response.text)
