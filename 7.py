from PIL import Image

img = Image.open("img/chó2.png")

if img.mode == "RGBA":
    img.convert("RGB")

# img.show()

# print(f"size: {img.size}, format: {img.format}, mode: {img.mode}")

# size = [748,1080]

# resized = img.resize(size,resample=Image.Resampling.LANCZOS)
# print(f"size: {resized.size}, format: {resized.format}, mode: {resized.mode}")
# resized.show()

# rotated = img.rotate(90,expand=True)
# rotated.show()