import os
import cv2
from functions import delete_folder, save_image

# Constants
DATA_FOLDER = 'data'

# Global Variables
current_image_name = 0

def initialize_data_folder():
    # Create the main data folder if it does not exist.
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def list_existing_folders():
    # List existing folders in the data directory.
    folders = [
        f for f in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, f))
    ]
    if folders:
        print("Existing folders in 'data':")
        for folder in folders:
            print(f"- {folder}")
    else:
        print("No folders in 'data'.")

def get_save_folder_name():
    # Prompt user for the folder name where images will be saved.
    user_folder_name = input("Enter the folder name where the images will be saved: ")
    return os.path.join(DATA_FOLDER, user_folder_name)

def initialize_image_counter(save_folder):
    # Initialize the image counter based on existing files.
    global current_image_name
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    existing_files = os.listdir(save_folder)
    numbers = [
        int(file.split('.')[0]) for file in existing_files
        if file.endswith('.png') and file.split('.')[0].isdigit()
    ]

    current_image_name = max(numbers, default=0) + 1

def start_video_capture():
    # Start video capture from the default camera.
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open the camera")
        exit()
    return cap

def capture_frames(cap, save_folder):
    # Capture frames from the camera and process user inputs.
    global current_image_name
    while True:    
        ret, frame = cap.read()
        if not ret:
            print("Could not receive the frame. Exiting...")
            break

        cv2.imshow('Video', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        if key == ord('s'):
            save_image(save_folder, current_image_name, frame)
            current_image_name += 1
        if key == ord('d'):
            eliminar_carpeta(save_folder)

def main():
    # Main function to run the application.
    initialize_data_folder()
    list_existing_folders()
    save_folder = get_save_folder_name()
    initialize_image_counter(save_folder)

    cap = start_video_capture()
    capture_frames(cap, save_folder)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
