# python3 JPEGtoPNG.py Pokedex/ new/
import sys
import os
from PIL import Image

# grab the first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check if new/ exists and create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # create output folder

# loop through folder
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("All done!")

# convert images to png


# save them to new folder

