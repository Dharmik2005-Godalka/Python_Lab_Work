from PIL import Image, ImageOps

img = Image.open(r'C:\Users\Dharmik\Pictures\MU.jpg')
padded_img = ImageOps.expand(img, border=50, fill='black')
padded_img.show()
