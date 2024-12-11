import cv2
import os
import random
import numpy as np


def create_synthetic_scratches(input_dir, output_dir, num_scratches=5):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for img_file in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_file)
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Add scratches
        for _ in range(num_scratches):
            x1, y1 = random.randint(0, img.shape[1]), random.randint(0, img.shape[0])
            x2, y2 = random.randint(0, img.shape[1]), random.randint(0, img.shape[0])
            thickness = random.randint(1, 3)
            color = (0, 0, 0)  # Black scratch
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

        # Save scratched image
        scratched_path = os.path.join(output_dir, img_file)
        cv2.imwrite(scratched_path, img)
    print(f"Synthetic scratches created in {output_dir}")


# Example usage
if __name__ == "__main__":
    create_synthetic_scratches("datasets/synthetic_scratches/original_images",
                               "datasets/synthetic_scratches/scratched_images")
