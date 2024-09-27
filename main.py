import cv2
import os

from functions import eliminar_carpeta, save_image

# Define the main folder
data_folder = 'data'

# List folders in 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

print("Existing folders in 'data':")
folders = [f for f in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, f))]
if folders:
    for folder in folders:
        print(f"- {folder}")
else:
    print("No folders in 'data'.")

# Ask the user to input the folder name
user_folder_name = input("Enter the folder name where the images will be saved: ")
save_folder = os.path.join(data_folder, user_folder_name)

# Global Variables
currentImageName = 0

# Initialize the values
def initValues():
    global currentImageName

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Get a list of files in the folder
    existing_files = os.listdir(save_folder)

    # Filter and get the numbers of the existing files
    numbers = [
        int(file.split('.')[0]) for file in existing_files
        if file.endswith('.png') and file.split('.')[0].isdigit()
    ]

    currentImageName = max(numbers, default=0) + 1

initValues()

# Start video capture (0 is for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is available
if not cap.isOpened():
    print("Could not open the camera")
    exit()

# Loop to capture frames continuously
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was captured correctly
    if not ret:
        print("Could not receive the frame. Exiting...")
        break

    # Display the frame in a window called 'Video'
    cv2.imshow('Video', frame)

    # Wait for 1 ms to detect keyboard input
    key = cv2.waitKey(1) & 0xFF

    # If 'q' is pressed, exit the loop
    if key == ord('q'):
        break

    # While 's' is pressed, capture images
    if key == ord('s'):
        save_image(save_folder, currentImageName, frame)
        currentImageName += 1  # Increment for the next image name

    # If 'd' is pressed, delete the folder with all images
    if key == ord('d'):
        eliminar_carpeta(save_folder)

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
