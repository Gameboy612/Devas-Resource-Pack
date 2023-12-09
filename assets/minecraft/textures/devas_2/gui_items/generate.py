import os
from PIL import Image

workspace = __file__.replace('\\', '/').replace('/generate.py', '')
folder = input("Which folder do you want to convert? ")

dirs = os.listdir(f"{workspace}/{folder}/")
HEIGHT = 256

image1 = Image.new('RGBA', (HEIGHT, HEIGHT * len(dirs)))
image2 = Image.new('RGBA', (HEIGHT, HEIGHT * len(dirs)))
image1.paste( (50, 50, 50), (0, 0, image1.size[0], image1.size[1]))
image2.paste( (50, 50, 50), (0, 0, image2.size[0], image2.size[1]))
for i, dir in enumerate(dirs):
    frame = Image.open(f"{workspace}/{folder}/{dir}")
    frame = frame.resize((int(frame.width * HEIGHT / frame.height), HEIGHT))
    print(dir)
    image1.paste(frame, ((HEIGHT - frame.width) // 2, i * HEIGHT), frame)
    image2.paste(frame, ((HEIGHT - frame.width) // 2, i * HEIGHT), frame)

# 2x3
# image1.crop((int(HEIGHT / 6), 0, int(5 * HEIGHT / 6), 0))
rect = Image.new("RGBA", (int(HEIGHT / 6), image1.height), (255, 255, 255, 0))
image1.paste(rect, (0, 0))
image1.paste(rect, (5 * HEIGHT // 6 + 1, 0))
# 1x2
rect = Image.new("RGBA", (int(HEIGHT / 4), image2.height), (255, 255, 255, 0))
image2.paste(rect, (0, 0))
image2.paste(rect, (3 * HEIGHT // 4 + 1, 0))

image1.save(f"{workspace}/{folder}_2_3.png")
image2.save(f"{workspace}/{folder}_1_2.png")

with open(f"{workspace}/{folder}_2_3.png.mcmeta", "w") as file:
    file.write("""{
  "animation": {
    "interpolate": false,
    "frametime": 2
  }
}""")
    
with open(f"{workspace}/{folder}_1_2.png.mcmeta", "w") as file:
    file.write("""{
  "animation": {
    "interpolate": false,
    "frametime": 2
  }
}""")
    
with open(f"{workspace.replace('/textures/', '/models/')}/{folder}_1_2.json", "w") as file:
    file.write("""{
    "parent": "item/generated",
    "textures": {
        "layer0": "devas_2/gui_items/%f_1_2"
    },
    "display": {
        "gui": {
            "rotation": [ 0, 0, 0 ],
            "translation": [ 0, -9, 0 ],
            "scale": [ 2.2, 2.2, 1 ]
        }
    }
}
""".replace("%w", workspace).replace("%f", folder))
    
    
with open(f"{workspace.replace('/textures/', '/models/')}/{folder}_2_3.json", "w") as file:
    file.write("""{
    "parent": "item/generated",
    "textures": {
        "layer0": "devas_2/gui_items/%f_2_3"
    },
    "display": {
        "gui": {
            "rotation": [ 0, 0, 0 ],
            "translation": [ 8, -18, 0 ],
            "scale": [ 3.4, 3.4, 1 ]
        }
    }
}
""".replace("%f", folder))