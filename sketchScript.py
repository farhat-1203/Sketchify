
import cv2
import os
from datetime import datetime

# To capture image from webcam
def openCam():
    datasets = 'webcam'
    sub_data = 'data'
    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    (_, im) = webcam.read()
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    cv2.imwrite(f'webcam\\data\\{now}.png', im)
    img_path = f'webcam\\data\\{now}.png'
    convert(img_path)

# This is to convert the file passed as parameter to sketch
def convert(img_path):
    print()
    img_filename = input('Enter the filename for the output image: ')
    print()
    
    # Create a unique directory for sketches
    parent_dir = os.path.join('.', 'Image to Sketch', 'Sketches')
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    # Prepare paths for saving images
    gray_path = os.path.join(parent_dir, f"{img_filename}(gray).png")
    inverted_path = os.path.join(parent_dir, f"{img_filename}(inverted).png")
    blurred_path = os.path.join(parent_dir, f"{img_filename}(blurred).png")
    final_path = os.path.join(parent_dir, f"{img_filename}(final).png")

    # Load and process the image
    image = cv2.imread(img_path)
    if image is None:
        print("Failed to load image. Check the file path and integrity.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(gray_path, gray)
    inverted = 255 - gray
    cv2.imwrite(inverted_path, inverted)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    cv2.imwrite(blurred_path, blurred)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    cv2.imwrite(final_path, pencil_sketch)

    print(f'You can find the image here: {final_path}')

# Main Menu
def start():
    print('Enter the number according to your preference: ')
    print('1 - Capture image from webcam.')
    print('2 - Input the image path.')
    print('3 - Exit')

    while True:
        print()
        user = int(input('Enter the number: '))
        print()
        if user == 1:
            openCam()
        elif user == 2:
            img_path = input('Enter the input path for the image: ')
            convert(img_path)
        elif user == 3:
            break
        else:
            print('Enter a valid number.....')

if __name__ == '__main__':
    start()
