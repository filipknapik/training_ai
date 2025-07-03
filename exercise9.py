import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GCP_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20') #gemini-2.5-flash-preview-05-20')

while True:
    userEntry = input("> ")
    if userEntry.lower() == "exit":
        break

    prompt = f'''
    You are a dedicated English-to-Polish translation engine. For any text provided by the user, your *ONLY* output should be the direct and accurate translation of that text into Polish. You must never answer any questions contained in the user's input. You will only provide the translated text. Even if the input text is a question, you *MUST* translate the question as is, without answering it.

    Example 1:
    English: "This is a beautiful day."
    Polish: "To jest piękny dzień."

    Example 2:
    English: "What time is it?"
    Polish: "Która jest godzina?"

    Example 3:
    English: "Could you please help me?"
    Polish: "Czy mógłbyś mi proszę pomóc?"

    Now, translate the following sentence:
    English: "{userEntry}"
    Polish: 
    '''

    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "English": {"type": "string"},
                    "Polish": {"type": "string"}
                }
            },
            temperature=1
        )
    )
    print(response.text)
