import tkinter as tk
from tkinter import filedialog
from super_resolution import apply_interpolation
from inpainting import inpaint_image

def process_image():
    input_path = filedialog.askopenfilename()
    output_path = filedialog.asksaveasfilename()
    method = method_var.get()
    if task_var.get() == "Super-Resolution":
        apply_interpolation(input_path, output_path, method)
    else:
        inpaint_image(input_path, output_path, method)

root = tk.Tk()
root.title("Image Processor")
tk.Label(root, text="Task:").pack()
task_var = tk.StringVar(value="Super-Resolution")
tk.Radiobutton(root, text="Super-Resolution", variable=task_var, value="Super-Resolution").pack()
tk.Radiobutton(root, text="Inpainting", variable=task_var, value="Inpainting").pack()

tk.Label(root, text="Method:").pack()
method_var = tk.StringVar(value="bicubic")
tk.Entry(root, textvariable=method_var).pack()

tk.Button(root, text="Process Image", command=process_image).pack()
root.mainloop()
