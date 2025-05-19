import os
import random
import shutil
from PIL import Image

image_folder = './images'  
output_folder = './output_images'  

os.makedirs(output_folder, exist_ok=True)

subfolder_image_counts = []

for item in os.listdir(image_folder):
    item_path = os.path.join(image_folder, item)
        
    if os.path.isdir(item_path):
        image_count = 0
        
        
        for filename in os.listdir(item_path):
            if any(filename.lower().endswith(ext) for ext in ['.jpg', '.png', '.jpeg', '.gif', '.bmp']):
                image_count += 1
        
        
        subfolder_image_counts.append((item, image_count))

subfolder_image_counts.sort(key=lambda x: x[1], reverse=True)

top_10_subfolders = subfolder_image_counts[:10]

print("Top 10 subfolders with the most images:")
for subfolder, count in top_10_subfolders:
    print(f"{subfolder}: {count} images")

smallest_image_count = min([count for _, count in top_10_subfolders])
for subfolder, _ in top_10_subfolders:
    subfolder_path = os.path.join(image_folder, subfolder)
    subfolder_output_path = os.path.join(output_folder, subfolder)

    os.makedirs(subfolder_output_path, exist_ok=True)
    
    images = [filename for filename in os.listdir(subfolder_path) 
              if any(filename.lower().endswith(ext) for ext in ['.jpg', '.png', '.jpeg', '.gif', '.bmp'])]
    
    random_images = random.sample(images, smallest_image_count)
    
    print(f"\nSaving {smallest_image_count} randomly selected images from {subfolder}:")
    for image in random_images:
        image_path = os.path.join(subfolder_path, image)
        output_image_path = os.path.join(subfolder_output_path, image)
        
        shutil.copy(image_path, output_image_path)

        print(f"  Saved: {image}")

print("\nProcess completed. Images saved in the new folder structure.")
