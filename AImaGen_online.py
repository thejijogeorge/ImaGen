#installed accelerate for HF optimisation
import os
import sys
import gradio as gr

from hf_online_image_generator import create_image_online

# prompt=input("What image do you want to generate")
# file_name=input("Choose a file name")
# create_image_local(prompt,file_name)

def gen_image(prompt):
    user_prompt=prompt.strip()
    #file_name="New_Image"
    image_path=create_image_online(user_prompt)
    return image_path

demo = gr.Interface(
    fn=gen_image,
    inputs=gr.Textbox(
            label="Image Prompt",
            placeholder="Describe the image you want to generate...",
            lines=3
        ),
    outputs=gr.Image(label="Generated Image"),
    title="Online Image Generator",
    description="Onlin Image Generator for black-forest-labs/FLUX.1-schnell",
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",  # Listen on all interfaces
        server_port=7860,        # Port (you can change this)
        share=False
    )
