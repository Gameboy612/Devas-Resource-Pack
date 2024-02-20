import os
from PIL import Image

# Get the directory path of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory path of the folder containing the PNG images
folder_path = script_dir

# Initialize variables for the final image dimensions
image_width = 16
image_height = 16
num_columns = 6
num_rows = 5
final_width = image_width * num_columns
final_height = image_height * num_rows

# Create a new blank image with the final dimensions
combined_image = Image.new("RGBA", (final_width, final_height))

# Input the sequence of photo names
photo_sequence = ["blank","weapon","perk","gadget","spell","ability_item","signature","element","bow","wand","shield","_offensive","_defensive","mobility","supportive","debuff","deployable","others","healing","mana","ability_item_arrow","ability_item_melee","fire", "water", "wind", "earth","light","dark"]

# Iterate over the photo sequence
for i, photo_name in enumerate(photo_sequence):
    # Create the filename based on the photo name
    filename = f"{photo_name}.png"

    # Open each PNG image
    image_path = os.path.join(folder_path, filename)
    image = Image.open(image_path)

    # Calculate the row and column indices for pasting the image
    row_index = i // num_columns
    column_index = i % num_columns

    # Calculate the paste position for the image
    paste_x = column_index * image_width
    paste_y = row_index * image_height

    # Resize the image to 16x16 if necessary
    if image.size != (image_width, image_height):
        image = image.resize((image_width, image_height))

    # Paste the image onto the combined image
    combined_image.paste(image, (paste_x, paste_y))

# Save the combined image in the same folder as the script
combined_image_path = os.path.join(folder_path, "_combined_image.png")
combined_image.save(combined_image_path)

print(f"Combined image saved at: {combined_image_path}")