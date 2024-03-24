import numpy as np
from PIL import Image
import pyperclip

SIZE = 32
HEIGHT = 128
SPLITS = 16

save_path = "assets/minecraft/textures/rpg/ui/active_effects/phases/$.png"
font_path = "assets/minecraft/font/rpg/active_effects_phase.json"

FILE_TEMPLATE = '''
{
    "providers": [
$
    ]
}
'''
providers = []
PROVIDER_TEMPLATE = '''        {
            "type": "bitmap",
            "file": "minecraft:rpg/ui/active_effects/phases/$1.png",
            "ascent": 16,
            "height": 48,
            "chars": ["\\u$2"]
        }'''

translates = []
TRANSLATE_TEMPLATE = '"rpg.ui.active_effects.phases.$1": "\\u$2",\n'

def offset_t(t):
    return - np.pi / 2 - t

def create_image(circle: list[list[tuple[int, int, int, int]]], index: int):
    img = Image.new("RGBA", (SIZE, HEIGHT))
    flatten_list = [(0, 0, 0, 0) for _ in range(SIZE * (HEIGHT - SIZE))]
    flatten_list.extend(sum(circle, []))
    flatten_list[-1] = (1, 1, 1, 1)
    img.putdata(flatten_list)
    img.save(save_path.replace("$", str(index)))

    providers.append(PROVIDER_TEMPLATE.replace("$1", str(index)).replace("$2", str(1000 + index)))
    translates.append(TRANSLATE_TEMPLATE.replace("$1", str(index)).replace("$2", str(1000 + index)))
    
    

for index, t_max in enumerate(np.arange(0, 2 * np.pi, 2 * np.pi / SPLITS)):
    FRAMES = [[(0, 0, 0, 0) for _ in range(SIZE)] for _ in range(SIZE)]
    for t in np.arange(0, t_max, 0.05):
        x = np.cos(offset_t(t))
        y = np.sin(offset_t(t))
        for r in np.arange(0, SIZE // 2, 0.5):
            FRAMES[int(r * y + SIZE/2)][int(r * x + SIZE/2)] = (0, 0, 0, 220)

    for line in FRAMES:
        for c in line:
            if c == (0, 0, 0, 0):
                print(" ",end="")
            else:
                print("1",end="")
        print("")
    create_image(FRAMES, index)

    print("")


with open(font_path, "w") as f:
    f.write(FILE_TEMPLATE.replace("$", ',\n'.join(providers)))

print(''.join(translates))

print("Copied to clipboard!")
pyperclip.copy(''.join(translates))