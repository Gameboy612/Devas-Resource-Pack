import os
from PIL import Image

# Get the directory path of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory path of the folder containing the PNG images
folder_path = script_dir

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        # Open the PNG image
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Create a new transparent 9x9 image
        transparent_image = Image.new("RGBA", (9, 9), (0, 0, 0, 0))

        # Save the transparent image with the original filename
        transparent_image.save(image_path)

        print(f"Replaced {filename} with a transparent 9x9 PNG image.")

print("All PNG images in the same folder as the script replaced with transparent 9x9 PNG images.")