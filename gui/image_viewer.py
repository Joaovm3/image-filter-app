import tkinter as tk
from PIL import ImageTk
from utils.image_utils import convert_image_to_tk

class ImageViewer:
    def __init__(self, root, original_image, modified_image, preview_images=None):
        self.frame = tk.Frame(root)
        
        self.left_frame = tk.Frame(self.frame)
        self.left_frame.pack(side=tk.LEFT, padx=10)
        
        self.original_label = tk.Label(self.left_frame)
        self.original_label.pack(side=tk.TOP, pady=5)
        
        self.preview_frame = tk.Frame(self.left_frame)
        self.preview_frame.pack(side=tk.TOP)
        
        self.preview_labels = []
        if preview_images:
            self.setup_preview_images(preview_images)
        
        self.modified_label = tk.Label(self.frame)
        self.modified_label.pack(side=tk.RIGHT, padx=10)
        
        self.update_images(original_image, modified_image)
    
    def setup_preview_images(self, images):
        preview_size = (100, 100)
        for i, image in enumerate(images):
            preview = image.resize(preview_size)
            preview_tk = ImageTk.PhotoImage(preview)
            preview_label = tk.Label(self.preview_frame, image=preview_tk)
            preview_label.image = preview_tk
            preview_label.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.preview_labels.append(preview_label)
    
    def update_images(self, original_image, modified_image):
        self.original_tk = convert_image_to_tk(original_image)
        self.modified_tk = convert_image_to_tk(modified_image)
        
        self.original_label.config(image=self.original_tk)
        self.modified_label.config(image=self.modified_tk)
    
    def update_modified_image(self, modified_image):
        self.modified_tk = convert_image_to_tk(modified_image)
        self.modified_label.config(image=self.modified_tk)
    
    def bind_preview_click(self, callback):
        for i, label in enumerate(self.preview_labels):
            label.bind('<Button-1>', lambda e, idx=i: callback(idx))
