import cv2
import os

def inpaint_image(input_dir, output_dir, method):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for img_file in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_file)
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Convert to grayscale and threshold
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)

        # Apply inpainting
        inpaint_method = cv2.INPAINT_TELEA if method == "telea" else cv2.INPAINT_NS
        inpainted_img = cv2.inpaint(img, mask, 3, inpaint_method)

        # Save inpainted image
        inpainted_path = os.path.join(output_dir, f"inpainted_{img_file}")
        cv2.imwrite(inpainted_path, inpainted_img)

    print(f"Inpainted images saved in {output_dir}")

# Example usage
if __name__ == "__main__":
    inpaint_image("datasets/synthetic_scratches/scratched_images", "output/inpainted", method="telea")
