import os
import cv2
import shutil

def delete_folder(directory):
    # Delete a folder and all its contents
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"The folder '{directory}' and all its contents have been deleted.")
    else:
        print(f"The folder '{directory}' does not exist.")

def save_image(save_folder, image_name, frame):
    # Save a captured image to the specified folder
    ensure_directory_exists(save_folder)
    
    # Create the name for the new file
    filename = os.path.join(save_folder, f"{image_name}.png")
    cv2.imwrite(filename, frame)

def ensure_directory_exists(directory):
    # Ensure that the specified directory exists, creating it if necessary
    if not os.path.exists(directory):
        os.makedirs(directory)

