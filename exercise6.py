import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

try:
    with open('taxmenothing.txt', 'r', encoding='utf-8') as f:
        loadFromFile = f.read()
except Exception as e:
    print(f"Error: {e}")
    loadFromFile = ""

while True:
    userEntry = input("> ")
    if userEntry.lower() == "exit":
        break
    prompt = f"""Respond to a question related to the following user guide:
    **User Guide**
    {loadFromFile}
    **Question**
    {userEntry}"""
    response = model.generate_content(prompt)
    print(response.text)
