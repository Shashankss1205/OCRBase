import os

# Function to process bounding boxes
def process_bounding_boxes(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Parse bounding box coordinates
    bounding_boxes = []
    for line in lines:
        coords = list(map(int, line.strip().split(',')))
        bounding_boxes.append(coords)

    # Sort bounding boxes based on y_min value
    bounding_boxes.sort(key=lambda box: box[1])

    # Group bounding boxes based on difference between max and min y_min values
    grouped_boxes = []
    current_group = []
    for box in bounding_boxes:
        if not current_group:
            current_group.append(box)
        else:
            min_y = min(current_group, key=lambda x: x[1])[1]
            max_y = max(current_group, key=lambda x: x[1])[1]
            if box[1] - min_y <= 10:
                current_group.append(box)
            else:
                grouped_boxes.append(current_group)
                current_group = [box]

    # Append the last group
    if current_group:
        grouped_boxes.append(current_group)

    # Sort each group based on x_min value
    for group in grouped_boxes:
        group.sort(key=lambda box: box[0])

    return grouped_boxes

# Path to the directory containing text files
input_directory = "/home/shashank/Desktop/gitRepos/CRAFT-pytorch/result"
output_directory = "/home/shashank/Desktop/gitRepos/CRAFT-pytorch/sorted_result"

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate over each text file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_directory, filename)
        sorted_bounding_boxes = process_bounding_boxes(file_path)
        
        # Write sorted bounding boxes to text file in output directory
        output_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_sorted.txt")
        with open(output_file_path, "w") as outfile:
            for group in sorted_bounding_boxes:
                for box in group:
                    outfile.write(','.join(map(str, box)) + '\n')
                outfile.write((';'))
