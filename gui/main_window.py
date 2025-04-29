import tkinter as tk
from gui.image_viewer import ImageViewer
from gui.controls import Controls
from core.file_manager import FileManager

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter Application")
        
        self.file_manager = FileManager()
        self.original_images = self.file_manager.load_images()
        self.current_image = self.original_images[0].copy()
        
        self.image_viewer = ImageViewer(self.root, self.original_images[0], self.current_image)
        self.image_viewer.frame.pack(side=tk.TOP, padx=10, pady=10)
        
        self.controls = Controls(self.root, self)
        self.controls.frame.pack(side=tk.BOTTOM, padx=10, pady=10)
    
    def apply_sobel_filter(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.apply_sobel(self.current_image)
        self.image_viewer.update_modified_image(self.current_image)
    
    def apply_median_filter(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.apply_median(self.current_image)
        self.image_viewer.update_modified_image(self.current_image)
    
    def invert_colors(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.invert_colors(self.current_image)
        self.image_viewer.update_modified_image(self.current_image)
    
    def adjust_contrast(self, value):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.adjust_contrast(self.current_image, float(value))
        self.image_viewer.update_modified_image(self.current_image)
    
    def save_modified_image(self):
        self.file_manager.save_image(self.current_image)
