import cv2
import os

def apply_interpolation(input_dir, output_dir, method):
    methods = {
        'nearest': cv2.INTER_NEAREST,
        'bilinear': cv2.INTER_LINEAR,
        'bicubic': cv2.INTER_CUBIC
    }
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for img_file in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_file)
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Upscale image
        height, width = img.shape[:2]
        upscale_img = cv2.resize(img, (width * 2, height * 2), interpolation=methods[method])

        # Save upscaled image
        upscaled_path = os.path.join(output_dir, f"{method}_{img_file}")
        cv2.imwrite(upscaled_path, upscale_img)

    print(f"Super-resolution images saved in {output_dir}")

# Example usage
if __name__ == "__main__":
    apply_interpolation("datasets/DIV2K/LR", "output/super_res", method="bicubic")
