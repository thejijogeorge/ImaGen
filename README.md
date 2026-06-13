# ImaGen

This project allows you to generate images using Hugging Face models.

## Setup

1.  **Create a `.env` file**: In the root directory of this project, create a file named `.env`.

2.  **Add your Hugging Face Token**: Open the newly created `.env` file and add your Hugging Face API token in the following format:

    ```
    HF_TOKEN=YOUR_HUGGING_FACE_TOKEN_HERE
    ```

    **How to get a Hugging Face Token**:
    *   Go to [Hugging Face](https://huggingface.co/).
    *   Sign in or create an account.
    *   Navigate to your profile settings.
    *   Go to "Access Tokens" and generate a new token with "read" permissions.
    *   Copy the generated token and paste it into your `.env` file.

## Updating the Model

To change the image generation model used by this project, you will need to modify the code where the model is specified. Look for the model identifier (e.g., "runwayml/stable-diffusion-v1-5") in the project's source code and replace it with the desired Hugging Face model identifier.

**Example (conceptual, actual file and line may vary):**

```python
# In a file like `app.py` or `model_loader.py`
model_id = "runwayml/stable-diffusion-v1-5" # Change this line
```

You can find various image generation models on the [Hugging Face Hub](https://huggingface.co/models?pipeline_tag=text-to-image&sort=downloads).