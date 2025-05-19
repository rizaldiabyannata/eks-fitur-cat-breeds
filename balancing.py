import os
import random
import shutil


output_folder = './output_images'
balanced_folder = './balanced_dataset'  


os.makedirs(balanced_folder, exist_ok=True)


subfolder_image_counts = []
for subfolder in os.listdir(output_folder):
    subfolder_path = os.path.join(output_folder, subfolder)
    
    if os.path.isdir(subfolder_path):
        image_count = len([f for f in os.listdir(subfolder_path) 
                          if any(f.lower().endswith(ext) for ext in ['.jpg', '.png', '.jpeg', '.gif', '.bmp'])])
        
        subfolder_image_counts.append((subfolder, image_count))


min_image_count = min([count for _, count in subfolder_image_counts])

print(f"Balancing dataset so each class has {min_image_count} images")


for subfolder, count in subfolder_image_counts:
    subfolder_path = os.path.join(output_folder, subfolder)
    balanced_subfolder_path = os.path.join(balanced_folder, subfolder)
    
    
    os.makedirs(balanced_subfolder_path, exist_ok=True)
    
    
    images = [f for f in os.listdir(subfolder_path) 
              if any(f.lower().endswith(ext) for ext in ['.jpg', '.png', '.jpeg', '.gif', '.bmp'])]
    
    
    
    if count == min_image_count:
        selected_images = images
    else:
        selected_images = random.sample(images, min_image_count)
    
    
    print(f"Copying {len(selected_images)} images from {subfolder} to balanced dataset")
    for image in selected_images:
        src_path = os.path.join(subfolder_path, image)
        dst_path = os.path.join(balanced_subfolder_path, image)
        shutil.copy(src_path, dst_path)

print(f"\nBalancing complete. Each class now has exactly {min_image_count} images in {balanced_folder}")