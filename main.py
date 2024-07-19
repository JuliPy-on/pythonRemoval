from rembg import remove
from PIL import Image
from pathlib import Path


def process_images(input_dir: Path, output_dir: Path, extensions: list):
    output_dir.mkdir(parents=True, exist_ok=True)
    all_files = [f for ext in extensions for f in input_dir.glob(ext)]

    for index, file_path in enumerate(all_files):
        try:
            file_name = file_path.stem
            output_path = output_dir / f'{file_name}_output.png'
            with Image.open(file_path) as img:
                output_img = remove(img)
                output_img.save(output_path)
            print(f'Completed: {index + 1}/{len(all_files)}')
        except Exception as e:
            print(f'Error processing file {file_path}: {e}')


def main():
    input_dir = Path('input_imgs')
    output_dir = Path('output_imgs')
    image_formats = ['*.jpeg', '*.jpg', '*.png', '*.bmp', '*.gif']
    process_images(input_dir, output_dir, image_formats)


if __name__ == '__main__':
    main()