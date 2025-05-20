import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

userEntry = ""

while userEntry != "exit":
    userEntry = input("> ")
    response = model.generate_content(f"Respond to the following question in as rude way as you only can: {userEntry}")
    print(response.text)
