import os
import cv2
import shutil

# Function to delete a folder and all its contents
def eliminar_carpeta(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"The folder '{directory}' and all its contents have been deleted.")
    else:
        print(f"The folder '{directory}' does not exist.")

# Function to save a captured image
def save_image(save_folder, image_name, frame):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Create the name for the new file
    filename = os.path.join(save_folder, f"{image_name}.png")
    cv2.imwrite(filename, frame)
