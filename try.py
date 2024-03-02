import cv2
import os

def extract_bounding_boxes(image_path, bounding_boxes_file, text_file, output_folder):
    # Read the main image
    main_image = cv2.imread(image_path)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Read bounding box coordinates from the text file
    with open(bounding_boxes_file, 'r') as f:
        bounding_boxes_data = f.read().strip().split(';')
    bounding_boxes_data = bounding_boxes_data[1:]
    print(bounding_boxes_data) #first value is for page number so skip it
    # Read text data from the text file
    with open(text_file, 'r') as f:
        text_data = f.read().strip().split('\n')
    print(text_data)

    for indx in range(len(text_data)):
        word = text_data[indx].split(' ')
        print(word)
        bounding_boxes_data[indx] = bounding_boxes_data[indx].strip()
        print(bounding_boxes_data[indx])
        bounding_box_coords = bounding_boxes_data[indx].split('\n')
        print(bounding_box_coords)
        for cnt in range(min(len(text_data[indx]),len(bounding_boxes_data[indx]))):
            
            # Parse bounding box coordinates
            coords = list(map(int, bounding_box_coords[cnt].split(',')))
            print(coords)
            x_min, y_min, x_max, y_min, x_max, y_max, x_min, y_max = coords

            # Extract the bounding box from the main image
            bounding_box = main_image[y_min:y_max, x_min:x_max]
            
            # Save the bounding box as a separate image
            output_path = os.path.join(output_folder, f'{word[cnt]}.png')
            cv2.imwrite(output_path, bounding_box)
            
            print(f'Saved bounding box for "{word[cnt]}" as {output_path}')


    # Loop over bounding box coordinates and text data
    # for bounding_box_coords, word in zip(bounding_boxes_data[1:], text_data):
    #     # Parse bounding box coordinates
    #     coords = list(map(int, bounding_box_coords.strip().split(',')))
    #     x_min, y_min, x_max, y_min, x_max, y_max, x_min, y_max = coords

    #     # Extract the bounding box from the main image
    #     bounding_box = main_image[y_min:y_max, x_min:x_max]
        
    #     # Save the bounding box as a separate image
    #     output_path = os.path.join(output_folder, f'{word}.png')
    #     cv2.imwrite(output_path, bounding_box)
        
    #     print(f'Saved bounding box for "{word}" as {output_path}')

# Example usage
image_path = 'result/res_page_1.jpg'
bounding_boxes_file = '/home/shashank/Desktop/gitRepos/CRAFT-pytorch/sorted_result/res_page_1_sorted.txt'
text_file = '/home/shashank/Desktop/gitRepos/CRAFT-pytorch/output/PDF_p1.txt'
output_folder = 'tryFolder'
extract_bounding_boxes(image_path, bounding_boxes_file, text_file, output_folder)
