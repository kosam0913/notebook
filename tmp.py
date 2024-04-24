import os
import re
import shutil

# Open the markdown file and read its content
note_dir = "C:/Users/kosam/Documents/Workspace/- xhu_notes"
target_file = rf'{note_dir}/2402_deeplearning_specialization.md'
with open(target_file, 'r') as file:
    content = file.read()

# Find all image references in the markdown file
image_refs = re.findall(r'/!/[.*?/]/((.*?)/)', content)

for image_ref in image_refs:
    # Get the image file name and its extension
    image_name = os.path.basename(image_ref)
    image_ext = os.path.splitext(image_name)[1]

    new_image_ref = image_ref.replace('./', note_dir + '/')
    print(new_image_ref)
    # Create a subdirectory with the image extension (if it doesn't exist)
    subdir = os.path.join(note_dir, "images", "2402_deeplearning_specialization")
    os.makedirs(subdir, exist_ok=True)

    # Move the image file to the subdirectory
    new_path = os.path.join(subdir, image_name).replace("//", "/")
    print(new_path)
    shutil.copy(new_image_ref, new_path)

    # Replace the image reference in the markdown file with the new path
    new_path_remove = new_path.replace(note_dir + "/", "/./")
    content = content.replace(image_ref, new_path_remove)

# Write the updated content back to the markdown file
with open(target_file, 'w') as file:
    file.write(content)


# rename all files in the directory to lowercase
from pathlib import Path

input_dir = r"C:/Users/kosam/Documents/Workspace/- xhu_notes/assignments/ml_operation_specialization"

for path in Path(input_dir).rglob('*'):
    if path.is_file():
        new_name = path.with_name(path.name.lower())
        path.rename(new_name)
        print(f"Renamed: {path} -> {new_name}")
