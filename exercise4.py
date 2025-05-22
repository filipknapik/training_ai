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
        generation_config=genai.types.GenerationConfig(temperature=2))
    print(response.text)
