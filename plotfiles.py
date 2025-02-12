import os
import matplotlib.pyplot as plt

folders = ['training/glioma', 'training/meningioma', 'training/pituitary', 'training/notumor']  # Replace with your actual folder paths

image_counts = {folder: 0 for folder in folders}  # Initialize counts to 0
for folder in folders:
    for root, _, files in os.walk(folder):
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
        image_counts[folder] += len(image_files)


bars = plt.bar(image_counts.keys(), image_counts.values(), color=['blue', 'orange'])

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', 
             ha='center', va='bottom', fontsize=10)

plt.xlabel('Folders')
plt.ylabel('Number of Images')
plt.title('Number of Images in Each Folder')
plt.show()
