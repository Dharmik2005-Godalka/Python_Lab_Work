from PIL import Image
import numpy as np

img = Image.open(r'C:\Users\Dharmik\Pictures\MU.jpg')
img_array = np.array(img)

print("Image mode:", img.mode)
print("Dimensions:", img.size)
print("Shape:", img_array.shape)
print("Minimum pixel value in Blue channel:", img_array[:, :, 2].min())
