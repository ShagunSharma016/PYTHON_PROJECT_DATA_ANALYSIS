import os
import requests
from PIL import Image
from io import BytesIO

# Retrieve the API token from the environment variable
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN")

# Ensure the token is available
if API_TOKEN is None:
    raise ValueError("API token is missing! Set the environment variable HUGGING_FACE_API_TOKEN.")
# Headers for the API request
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_image_from_text(text_prompt):
    """Generate an image from a text description using Stable Diffusion API."""
    response = requests.post(API_URL, headers=headers, json={"inputs": text_prompt})

    if response.status_code == 200:
        image_bytes = response.content
        image = Image.open(BytesIO(image_bytes))
        image.save("generated_image.png")
        print("Image saved as 'generated_image.png'")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Get the text prompt from the user
text_description = input("Enter the text description for image generation: ")

# Generate and save the image
generate_image_from_text(text_description)
