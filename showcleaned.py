from PIL import Image
import matplotlib.pyplot as plt

# Paths to the two images
image1_path = 'testing/glioma/Te-glTr_0000.jpg'  # Replace with the path to your first image
image2_path = 'cleaned/Testing/glioma/Te-glTr_0000.jpg'  # Replace with the path to your second image

# Load the images using Pillow
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Display the first image
axes[0].imshow(image1)
axes[0].set_title('No pre-processing')
axes[0].axis('off')  # Hide axes

axes[1].imshow(image2)
axes[1].set_title('Pre-processed')
axes[1].axis('off')  # Hide axes

plt.tight_layout()
plt.show()
