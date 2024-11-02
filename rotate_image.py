# rotate images to 90 degree in a folder 
import os
from PIL import Image

folder_path = r'directory_of_your_folder' 

for filename in os.listdir(folder_path):
    
    img = Image.open(os.path.join(folder_path, filename))
    
    rotated_img = img.rotate(90)
    
    rotated_img.save(os.path.join(folder_path, filename))
    print('done', filename)