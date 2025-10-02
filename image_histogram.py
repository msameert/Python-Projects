import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("My Selfie.png")
img_array = np.array(img)

plt.figure(figsize=(6,6))
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")
plt.show()

red_channel = img_array[:, :, 0].flatten()
green_channel = img_array[:, :, 1].flatten()
blue_channel = img_array[:, :, 2].flatten()

# Plot histograms
plt.figure(figsize=(10,5))
plt.hist(red_channel, bins=256, color='red', alpha=0.5, label="Red")
plt.hist(green_channel, bins=256, color='green', alpha=0.5, label="Green")
plt.hist(blue_channel, bins=256, color='blue', alpha=0.5, label="Blue")

plt.title("Color Histogram of Image")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Frequency")
plt.legend()
plt.show()