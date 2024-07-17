import torch
from torch import autocast
from diffusers import StableDiffusionPipeline 

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16) 
pipe.to(device) 

def generate_image(prompt):

    # Generate the image
    image = pipe(prompt).images[0]

    return image
