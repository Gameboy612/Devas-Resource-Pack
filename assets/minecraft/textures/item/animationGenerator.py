from PIL import Image
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for the given image
image_filename = "given_image.png"
image_path = os.path.join(current_directory, image_filename)

# Open the given image
given_image = Image.open(image_path).convert("RGBA")
height = given_image.size[1]

# Step 2: Generate the pictures
output_directory = os.path.join(current_directory, "generated_pictures")
os.makedirs(output_directory, exist_ok=True)

# Save the initial given image as the first generated image (0.png)
given_image.save(os.path.join(output_directory, "0.png"))

for i in range(1, height):
    # Open the previous generated image
    previous_image_path = os.path.join(output_directory, f"{i-1}.png")
    previous_image = Image.open(previous_image_path).convert("RGBA")

    # Create a new image by moving the bottommost row of pixels to the top
    new_image = Image.new("RGBA", given_image.size)
    new_image_pixels = new_image.load()
    previous_pixels = previous_image.load()

    for x in range(new_image.width):
        for y in range(new_image.height - 1):
            new_image_pixels[x, y] = previous_pixels[x, y + 1]

    bottom_row = [previous_pixels[x, 0] for x in range(new_image.width)]
    for x in range(new_image.width):
        new_image_pixels[x, new_image.height - 1] = bottom_row[x]

    # Save the generated image
    new_image_path = os.path.join(output_directory, f"{i}.png")
    new_image.save(new_image_path)

# Step 3: Combine the generated images
combined_image = Image.new("RGBA", (given_image.width, height * height))

for i in range(height):
    image_path = os.path.join(output_directory, f"{i}.png")
    generated_image = Image.open(image_path).convert("RGBA")

    combined_image.paste(generated_image, (0, i * height), mask=generated_image)

# Save the combined image
combined_image.save(os.path.join(current_directory, "barrier.png"))