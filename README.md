# Image Background Removal

This project provides a Python script for removing backgrounds from images using the `rembg` library.
It supports multiple image formats and saves the processed images in `.png` format to retain transparency.


## Requirements

1. **Python**: Ensure you have Python 3.6 or higher installed.
2. **Libraries**: You need to install `rembg` and `Pillow`.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/JuliPy-on/-ImageBackgroundRemoval-.git

2. **Navigate to the Project Directory**

   ```bash
   cd ImageBackgroundRemoval
   
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

## Usage

1. **Prepare Directories**

   Create two directories:

   input_imgs for your input images.
   output_imgs for saving the processed images.

2. **Add Images**

   Place the images you want to process into the input_imgs directory. 
   Supported formats include .jpeg, .jpg, .png, .bmp, and .gif.

3. **Specify Paths in the Script**

   In the main.py file, specify your own paths for the input_dir and output_dir variables. For example:

   ```bash
    def main():
        input_dir = Path('/your/path/to/input_imgs')
        output_dir = Path('/your/path/to/output_imgs')
        image_formats = ['*.jpeg', '*.jpg', '*.png', '*.bmp', '*.gif']
        process_images(input_dir, output_dir, image_formats)

4. **Run the Script**

   Execute the script using Python:

   ```bash
   python main.py
   

The script will process all images in the input_imgs directory and save the output in the output_imgs directory with an _output suffix.
