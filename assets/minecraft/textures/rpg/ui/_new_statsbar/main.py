from PIL import Image


def generateFiles(path, save_path, height, num_range = (0, 10)):
    for i in range(num_range[0], num_range[1] + 1, 1):
        image = Image.open(path.replace("$", str(i)))

        extended_image = Image.new("RGBA", (image.size[0], height))

        extended_image.paste(image, (0, height - image.size[1]))

        extended_image.save(save_path.replace("$", str(i)))

generateFiles(
    path="assets/minecraft/textures/rpg/ui/_new_statsbar/_references/9px/health/$.png",
    save_path="assets/minecraft/textures/rpg/ui/_new_statsbar/health/$.png",
    height=39
)
generateFiles(
    path="assets/minecraft/textures/rpg/ui/_new_statsbar/_references/9px/stamina/$.png",
    save_path="assets/minecraft/textures/rpg/ui/_new_statsbar/stamina/$.png",
    height=39
)
generateFiles(
    path="assets/minecraft/textures/rpg/ui/_new_statsbar/_references/9px/mana/$.png",
    save_path="assets/minecraft/textures/rpg/ui/_new_statsbar/mana/$.png",
    height=39
)

generateFiles(
    path="assets/minecraft/textures/rpg/ui/_new_statsbar/_references/9px/health/$.png",
    save_path="assets/minecraft/textures/rpg/ui/_new_statsbar/health_top/$.png",
    height=27
)
generateFiles(
    path="assets/minecraft/textures/rpg/ui/_new_statsbar/_references/9px/mana/$.png",
    save_path="assets/minecraft/textures/rpg/ui/_new_statsbar/mana_top/$.png",
    height=27
)

generateFiles(
    path="assets/minecraft/textures/rpg/ui/_new_statsbar/_references/9px/stamina/$.png",
    save_path="assets/minecraft/textures/rpg/ui/_new_statsbar/stamina_top/$.png",
    height=27
)

generateFiles(
    path="assets/minecraft/textures/rpg/ui/_new_statsbar/_references/ultimate_point/ultimate_option$.png",
    save_path="assets/minecraft/textures/rpg/ui/_new_statsbar/ultimate_point/$.png",
    height=26,
    num_range=(1, 3)
)