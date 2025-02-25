from PIL import Image
image = Image.open("img/cat1.png")
if image.mode == "RGBA":
    image.convert("RGB")
size = (1000,500)
resized = image.resize(size,Image.Resampling.LANCZOS)

resized.show()
