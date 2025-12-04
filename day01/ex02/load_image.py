from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    try:
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        pixels = np.array(img)
        print(f"The shape of image is: {pixels.shape}")
        return (list(img.getdata()))


    except ValueError as error:
        print(f"Error: {error}")

