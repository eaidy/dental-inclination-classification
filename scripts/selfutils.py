import os
import cv2
import numpy as np

def count_files(directory):
    count = 0
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the path is a file (not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            count += 1
    return count

def load_images_from_dataset(directory):
    images = []
    for filename in os.listdir(directory):
        # Construct the full path to the image file
        file_path = os.path.join(directory, filename)
        # Read the image using OpenCV
        image = cv2.imread(file_path)
        # Convert the image to RGB format (OpenCV reads images in BGR format by default)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Append the image to the list
        images.append(image)
    return np.array(images)