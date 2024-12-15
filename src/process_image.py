import cv2
import os
from src.super_resolution import apply_interpolation
from src.inpainting import inpaint_image


def process_image(input_path, output_dir, sr_method='bicubic', inpaint_method='telea'):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Step 1: Perform Super-Resolution
    input_img = cv2.imread(input_path)
    if input_img is None:
        raise FileNotFoundError(f"Input file not found: {input_path}")

    height, width = input_img.shape[:2]
    upscale_img = cv2.resize(input_img, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)
    super_res_path = os.path.join(output_dir, "super_res_image.jpg")
    cv2.imwrite(super_res_path, upscale_img)
    print(f"Super-resolution completed: {super_res_path}")

    # Step 2: Convert to grayscale and threshold for mask
    gray = cv2.cvtColor(upscale_img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)

    # Step 3: Apply Inpainting
    inpaint_method_flag = cv2.INPAINT_TELEA if inpaint_method == "telea" else cv2.INPAINT_NS
    inpainted_img = cv2.inpaint(upscale_img, mask, 3, inpaint_method_flag)
    inpaint_path = os.path.join(output_dir, "final_output.jpg")
    cv2.imwrite(inpaint_path, inpainted_img)
    print(f"Inpainting completed: {inpaint_path}")

    return inpaint_path

def process_image1(input_path, output_dir, sr_method='bicubic', inpaint_method='telea'):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

        # Step 1: Read the Input Image
    input_img = cv2.imread(input_path)
    if input_img is None:
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Step 2: Convert to Grayscale and Create a Mask for Scratches
    gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)  # Adjust the threshold as needed
    mask_path = os.path.join(output_dir, "mask.jpg")
    cv2.imwrite(mask_path, mask)
    print(f"Mask generated and saved: {mask_path}")

    # Step 3: Apply Inpainting to Remove Scratches
    inpaint_method_flag = cv2.INPAINT_TELEA if inpaint_method == "telea" else cv2.INPAINT_NS
    inpainted_img = cv2.inpaint(input_img, mask, 3, inpaint_method_flag)
    inpaint_path = os.path.join(output_dir, "inpainted_image.jpg")
    cv2.imwrite(inpaint_path, inpainted_img)
    print(f"Inpainting completed: {inpaint_path}")

    # Step 4: Perform Super-Resolution on the Inpainted Image
    height, width = inpainted_img.shape[:2]
    upscale_img = cv2.resize(inpainted_img, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)
    super_res_path = os.path.join(output_dir, "final_super_res_image.jpg")
    cv2.imwrite(super_res_path, upscale_img)
    print(f"Super-resolution completed: {super_res_path}")

    return super_res_path

# Example usage for testing
if __name__ == "__main__":
    result = process_image1("path_to_input_image.jpg", "output1", sr_method="bicubic", inpaint_method="telea")
    print(f"Processed image saved at: {result}")
