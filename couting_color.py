import os
import numpy as np
from PIL import Image
from skimage import measure
from skimage.segmentation import clear_border

def create_masks_and_save(image_path, output_folder):
    # Load the image
    image = Image.open(image_path)
    image_array = np.array(image)

    # Define what we'll consider as "black" and "white"
    black_threshold = np.array([15, 15, 15])
    white_threshold = np.array([240, 240, 240])

    # Create a mask for non-black and non-white pixels
    mask = (image_array[:, :, :3] > black_threshold).any(axis=2) & (image_array[:, :, :3] < white_threshold).any(axis=2)

    # Clear the border to separate the cells completely
    separated_cells = clear_border(mask)

    # Label the separated cells
    labeled_cells, num_labels = measure.label(separated_cells, background=0, return_num=True)

    # Create an temp image that is white where the shapes are and black elsewhere
    mask_image = np.zeros_like(image_array[:, :, :3])
    mask_image[labeled_cells != 0] = [255, 255, 255]
    
    # Save only the mask image
    mask_image_path = os.path.join(output_folder, 'mask_only.png')
    Image.fromarray(mask_image).save(mask_image_path)

    # Create individual masks for each labeled shape and save them
    for label_num in range(1, num_labels + 1):
        # Create an individual mask
        individual_mask = (labeled_cells == label_num)

        # Find the bounding box of the individual mask to crop it
        region_props = measure.regionprops(individual_mask.astype(int))
        minr, minc, maxr, maxc = region_props[0].bbox

        # Crop the image around the bounding box of the mask
        cropped_image = image_array[minr:maxr, minc:maxc]

        # Generate filename based on the grid position
        row, col = divmod(label_num - 1, 10)  # Assuming a 10-column grid
        filename = f'{chr(97 + row)}{col + 1}.png'  # Starting from 'a1.png'
        file_path = os.path.join(output_folder, filename)

        # Save the individual cropped image
        Image.fromarray(cropped_image).save(file_path)

    return mask_image_path, output_folder

# Set the path to your image and the temp directory
image_path = 'path_to_your_image.png'
output_folder = 'path_to_output_directory'

# Create the temp directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Call the function and get the paths
mask_only_path, cells_output_folder = create_masks_and_save(image_path,
