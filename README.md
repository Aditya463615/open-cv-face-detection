# Face Detection Project

## Description

This project is designed to detect faces in images using OpenCV's Haar cascades. The detected faces are then displayed in a standard size specified in the code.

## Code Explanation

The script `detect_face.py` contains two main functions:

1. `detect_face(file_name)`: This function takes an image file as input, detects faces in the image, and saves the detected faces as separate images in the `output_images` directory.

2. `main()`: This function scans the `input_images` directory for image files and calls the `detect_face` function for each image.

The script uses the Haar cascade classifier provided by OpenCV to detect faces. This is a machine learning-based approach where a cascade function is trained from a lot of positive (images with faces) and negative images (images without faces). It is then used to detect the objects (faces) in other images.

## Extending the Project

While this project is focused on face detection, the same approach can be used to detect other objects. OpenCV provides several pre-trained classifiers for different objects such as eyes, full body, etc. You can replace the face classifier with these other classifiers to detect different objects.

## Installation

This project requires Python and the following Python libraries installed:

- OpenCV

You can install these libraries using pip:

```bash
pip install opencv-python
```

## Running the Project

To run the script, use the following command:

```bash
python detect_face.py
```

## Directory Structure

The project has the following directory structure:

- `input_images`: This directory should contain the images on which face detection should be performed.
- `output_images`: This directory will contain the output images with detected faces.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
