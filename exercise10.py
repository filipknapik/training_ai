import google.generativeai as genai
import google.auth
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import os

credentials, project_id = google.auth.default()


genai.configure(api_key=os.environ.get('GCP_KEY'))
vertexai.init(project=project_id, location="us-central1")

counter = 0

while True:
    positivePrompt = input("Describe what you want to have in the image: > ")
    negativePrompt = input("Describe what you DON'T want to have in the image: > ")


    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

    images = model.generate_images(
        prompt=positivePrompt,
        negative_prompt=negativePrompt,
        number_of_images=1,
        language="en",
        add_watermark=False,
        aspect_ratio="16:9"
    )

    images[0].save(location=f'output{counter}.png', include_generation_parameters=False)
    counter += 1
    
    print("File generated")
