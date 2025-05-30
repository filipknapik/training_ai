import google.generativeai as genai
import os
import pprint

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06')

while True:
    userEntry = input("> ")
    if userEntry.lower() == "exit":
        break
    response = model.generate_content(userEntry)
    pprint.pprint(response)
    print(response)