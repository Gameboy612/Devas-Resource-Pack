import os
from PIL import Image


def generateFiles(path, save_path, height, num_range = (0, 10)):
    for i in range(num_range[0], num_range[1] + 1, 1):
        image = Image.open(path.replace("$", str(i)))

        extended_image = Image.new("RGBA", (image.size[0], height))

        extended_image.paste(image, (0, height - image.size[1]))
        extended_image.putpixel((0, 0), (0, 0, 0, 1))
        extended_image.save(save_path.replace("$", str(i)))

for name in os.listdir("assets/minecraft/textures/font/default_outlined"):
    if not name.endswith(".png"):
        continue
    generateFiles(
        path=f"assets/minecraft/textures/font/default_outlined/{name}",
        save_path=f"assets/minecraft/textures/font/shifted_default_outlined/{name}",
        height=40
    )