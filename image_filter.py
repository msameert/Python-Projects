import numpy as np
from PIL import Image

img = Image.open("My Selfie.png")
img_array = np.array(img)
print("Image shape : ", img_array.shape)

gray = np.mean(img_array, axis=2)
gray_image = Image.fromarray(gray.astype(np.uint8))
gray_image.save("Gray Selfie.png")