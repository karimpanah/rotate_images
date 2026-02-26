# Simple Image Rotator

A simple Python script using Pillow (PIL) to batch-rotate all images in a folder by a specified angle.

---

## Features

* **Batch Processing:** Rotates all supported image files in a directory.
* **Custom Angle:** Specify any rotation angle in degrees (e.g., 45, 90, 180).
* **Flexible Output:**
    * Overwrite original images.
    * Save rotated images to a new, specified folder.
    * Save rotated images in the *same* folder with a `_rotated` suffix (default).
* **Error Handling:** Skips files that can't be processed and prints an error message.
* **Supported Formats:** Works with `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.gif`.

---

## Requirements

* Python 3.x
* Pillow (PIL)

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/karimpanah/rotate_images.git](https://github.com/karimpanah/rotate_images.git)
    
    cd rotate_images
    ```
    (Replace `karimpanah` and `rotate_images` with your actual GitHub info)

2.  **Install the required library (Pillow):**
    ```bash
    pip install Pillow
    ```

---

## How to Use

1.  Open the `rotate_images.py` script (or whatever you named the file) in a text editor.
2.  Find the section at the bottom of the file to customize the settings.
3.  Modify the parameters inside the `rotate_images_in_folder()` function call.

```python
# Customize these settings:
rotate_images_in_folder(
    folder_path = r'input_folder',    # Path to your image folder
    degrees = 90,                     # Rotation angle
    overwrite = False,                # Set True to overwrite originals
    output_folder = r'output_folder'  # (Optional) Specify an output folder
)
