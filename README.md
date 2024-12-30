# Image to Sketch Conversion
This project allows you to convert any image to a pencil sketch using Python and OpenCV. The process includes capturing an image via webcam or providing an image file path, applying image transformations such as grayscale conversion, inversion, blurring, and generating a pencil sketch effect.

## Features
- Capture images from webcam.
- Convert any image (including webcam capture) to a pencil sketch.
- Save intermediate and final images in a user-defined directory.
- Supports saving grayscale, inverted, blurred, and final pencil sketch images.
- Provides an intuitive command-line interface.

## Requirements

To run this project, you need to have Python and the required libraries installed. You can install the necessary dependencies using `pip`:

- Python 3.x
- OpenCV (`cv2`)

## Requirements
To run this project, you'll need the following Python libraries:

- `pandas`
- `scikit-learn`
- `nltk`
- `tkinter` (comes pre-installed with Python)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/farhat-1203/Sketchify.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Sketchify
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   
## Project Structure
```
Image-to-Sketch
├── webcam/                       # Folder for webcam-captured images
│   └── data/                     # Folder where captured images are saved
├── Image to Sketch/              # Main folder for the sketch conversion program
│   └── Sketches/                 # Folder for storing the converted sketch images
├── sketchScript.py               # Main Python script for image capture and sketch conversion
├── README.md                     # Project documentation
├── requirements.txt              # List of dependencies for the project
└── .gitignore                    # Git ignore file (if using Git)

```
