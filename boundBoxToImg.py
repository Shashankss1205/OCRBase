import cv2
import os

def extract_bounding_boxes(image_path, bounding_boxes_file, output_folder):
    # Read the main image
    main_image = cv2.imread(image_path)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Read bounding box coordinates from the text file
    with open(bounding_boxes_file, 'r') as f:
        lines = f.readlines()
    
    # Extract bounding boxes from the main image
    for i, line in enumerate(lines):
        # Parse bounding box coordinates
        x_min, y_min, x_max, y_min, x_max, y_max, x_min, y_max = map(int, line.strip().split(','))
        
        # Extract the bounding box from the main image
        bounding_box = main_image[y_min:y_max, x_min:x_max]
        
        # Save the bounding box as a separate image
        output_path = os.path.join(output_folder, f'bounding_box_{i}.png')
        cv2.imwrite(output_path, bounding_box)
        
        print(f'Saved bounding box {i} as {output_path}')

# Example usage
image_path = '/home/shashank/Desktop/gitRepos/CRAFT-pytorch/testFolder/page_1.png'
bounding_boxes_file = '/home/shashank/Desktop/gitRepos/CRAFT-pytorch/sorted_bounding_boxes.txt'
output_folder = 'extracted_bounding_boxes'
extract_bounding_boxes(image_path, bounding_boxes_file, output_folder)
