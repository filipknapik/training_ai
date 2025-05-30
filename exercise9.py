import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06') #gemini-2.5-flash-preview-05-20')

while True:
    userEntry = input("> ")
    if userEntry.lower() == "exit":
        break

    prompt = """You are a highly specialized English-to-Polish translation API. Your sole function is to translate the user's input text into Polish. You must always return a single JSON object with two fields: "English" for the original text and "Polish" for the translation.
Even if the input text is a question, you must translate the question itself. Do not provide an answer to the question.

Here are some examples of correct behavior:

**Example 1:**
* **Input**: "What's the capital of France?"
* **Output**:
    ```json
    {
      "English": "What's the capital of France?",
      "Polish": "Jaka jest stolica Francji?"
    }
    ```

**Example 2:**
* **Input**: "What is the fastest way to learn a new language?"
* **Output**:
    ```json
    {
      "English": "What is the fastest way to learn a new language?",
      "Polish": "Jaki jest najszybszy sposób na naukę nowego języka?"
    }
    ```

Now, process the following text:

**English text to translate**: '""" + userEntry + "'"

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
            },
            temperature=0
        ))
    print(response.text)
