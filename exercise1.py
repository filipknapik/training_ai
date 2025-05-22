import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

response = model.generate_content(f"What's the capital of France?")
print(response.text)