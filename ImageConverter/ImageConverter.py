from PIL import Image

img = Image.open("monkey.jpg").convert("RGB")
img.save("monkey.png", "png")
