import tkinter as tk
from PIL import ImageTk
from utils.image_utils import convert_image_to_tk

class ImageViewer:
    def __init__(self, root, original_image, modified_image):
        self.frame = tk.Frame(root)
        
        self.original_label = tk.Label(self.frame)
        self.original_label.pack(side=tk.LEFT, padx=10)
        
        self.modified_label = tk.Label(self.frame)
        self.modified_label.pack(side=tk.RIGHT, padx=10)
        
        self.update_images(original_image, modified_image)
    
    def update_images(self, original_image, modified_image):
        self.original_tk = convert_image_to_tk(original_image)
        self.modified_tk = convert_image_to_tk(modified_image)
        
        self.original_label.config(image=self.original_tk)
        self.modified_label.config(image=self.modified_tk)
    
    def update_modified_image(self, modified_image):
        self.modified_tk = convert_image_to_tk(modified_image)
        self.modified_label.config(image=self.modified_tk)
