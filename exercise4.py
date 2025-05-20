import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

userEntry = ""

while userEntry != "exit":
    userEntry = input("> ")
    response = model.generate_content(userEntry)
    finalResponse = model.generate_content(f"Transform this response to a funny, youth language. Use as much slang as you only can. Return only the updated sentence, no introduction. Input sentence: {response.text}")
    print(finalResponse.text)
