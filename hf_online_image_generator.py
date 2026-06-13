import io
import os
import sys
from PIL import Image
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()  # Loads from .env file

HF_TOKEN=os.getenv('HF_TOKEN')

# Initialize the client with your Hugging Face access token
client = InferenceClient(token=HF_TOKEN)

def create_image_online(uprompt):
    # Request the image from the cloud model
    image = client.text_to_image(
        prompt=uprompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    # Convert bytes to an image and save it locally
    # image = Image.open(io.BytesIO(image_bytes))
    image_path = "generated_image.png"
    image.save(image_path)
    print("Image saved successfully!")
    return image_path

#if __name__ == "__main__":
#    create_image_online("An Young Man with beard, highly detailed and realistic brown man")





