import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r'C:\Users\Dharmik\Pictures\MU.jpg')
img_array = np.array(img)

R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(R, cmap='Reds')
plt.title("Red Channel")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(G, cmap='Greens')
plt.title("Green Channel")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(B, cmap='Blues')
plt.title("Blue Channel")
plt.axis('off')

plt.show()
