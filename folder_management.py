# directory_management.py

import os
import shutil
from constants import DATA_FOLDER, TRAIN_FOLDER, VALIDATION_FOLDER

def sort_data():
    # Create the train and validation folders if they don't exist
    if not os.path.exists(TRAIN_FOLDER):
        os.makedirs(TRAIN_FOLDER)
    if not os.path.exists(VALIDATION_FOLDER):
        os.makedirs(VALIDATION_FOLDER)

    # List the existing folders in the data directory
    folders = [
        f for f in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, f))
    ]
    
    for folder in folders:
        # Create subfolders inside train and validation, keeping the original names
        train_subfolder = os.path.join(TRAIN_FOLDER, folder)
        validation_subfolder = os.path.join(VALIDATION_FOLDER, folder)

        # Create the subfolders if they don't exist
        if not os.path.exists(train_subfolder):
            os.makedirs(train_subfolder)
        if not os.path.exists(validation_subfolder):
            os.makedirs(validation_subfolder)

        # List all the files in the original folder
        files = os.listdir(os.path.join(DATA_FOLDER, folder)) 
        
        # Every 5th file goes to validation
        for i, file in enumerate(files):
            src_path = os.path.join(DATA_FOLDER, folder, file)  # Path to the original file
            
            # Define the destination path based on the index
            if i % 5 == 0:
                dest_path = os.path.join(validation_subfolder, file)  # Move to validation
            else:
                dest_path = os.path.join(train_subfolder, file)  # Move to train
                
            # Move the file to the corresponding folder
            shutil.move(src_path, dest_path)

# Run the sorting function
sort_data()
