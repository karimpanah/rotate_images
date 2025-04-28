# Simple Image Rotator, Rotates all images in a folder
import os
from PIL import Image

def rotate_images_in_folder(folder_path, degrees=90, overwrite=False, output_folder=None):
    """
    Rotates all images in a folder by specified degrees
    
    Parameters:
    - folder_path: Path to folder containing images
    - degrees: Rotation angle (default: 90)
    - overwrite: Overwrite original files if True (default: False)
    - output_folder: Custom output folder (optional)
    """
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_formats):
            try:
                filepath = os.path.join(folder_path, filename)
                img = Image.open(filepath)
                
                # Rotate image
                rotated_img = img.rotate(degrees, expand=True)
                
                # Determine output path
                if overwrite:
                    output_path = filepath
                else:
                    if output_folder:
                        output_path = os.path.join(output_folder, filename)
                    else:
                        name, ext = os.path.splitext(filename)
                        output_path = os.path.join(folder_path, f"{name}_rotated{ext}")
                
                rotated_img.save(output_path)
                print(f'Processed: {filename} (Rotated {degrees}°)')
                
            except Exception as e:
                print(f'Error processing {filename}: {str(e)}')

# Customize these settings:
rotate_images_in_folder(
    folder_path = r'input_folder',     # Your image folder path
    degrees = 45,                      # Rotation angle (e.g., 45 degrees)
    overwrite = False,                 # Set True to overwrite original files
    output_folder = r'output_folder'   # Output folder
)
