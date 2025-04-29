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
        self.filter_applied = False
        
        self.image_viewer = ImageViewer(
            self.root, 
            self.original_images[0], 
            self.current_image, 
            self.original_images
        )
        self.image_viewer.frame.pack(side=tk.TOP, padx=10, pady=10)
        self.image_viewer.bind_preview_click(self.change_active_image)
        
        self.controls = Controls(self.root, self)
        self.controls.frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.current_image_index = 0
        self.filters = {}
    
    def change_active_image(self, image_index):
        self.current_image_index = image_index
        self.current_image = self.original_images[image_index].copy()
        self.image_viewer.update_images(self.original_images[image_index], self.current_image)
        self.controls.contrast_scale.set(1.0)
    
    def add_sobel_filter(self):
        if 'sobel' in self.filters:
            self.filters['sobel'] = False
        else: 
            self.filters['sobel'] = True

    def add_median_filter(self):
        if 'median' in self.filters:
            self.filters['median'] = False
        else: 
            self.filters['median'] = True

    def add_invert_colors(self):
        if 'invert' in self.filters:
            self.filters['invert'] = False
        else: 
            self.filters['invert'] = True

    def add_adjust_contrast(self, value):
        self.filters['contrast'] = value

    def apply_sobel_filter(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.apply_sobel(self.current_image)
        self.image_viewer.update_modified_image(self.current_image)
        self.filter_applied = True
    
    def apply_median_filter(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.apply_median(self.current_image)
        self.image_viewer.update_modified_image(self.current_image)
        self.filter_applied = True
    
    def invert_colors(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.invert_colors(self.current_image)
        self.image_viewer.update_modified_image(self.current_image)
        self.filter_applied = True
    
    def adjust_contrast(self, value):
        from core.image_processor import ImageProcessor
        base_image = self.original_images[self.current_image_index].copy()
        if (self.filter_applied):
            base_image = self.current_image.copy()
            base_image = ImageProcessor.adjust_contrast(base_image, float(value))
            self.image_viewer.update_modified_image(base_image)
        else:
            self.current_image = ImageProcessor.adjust_contrast(base_image, float(value))
            self.image_viewer.update_modified_image(self.current_image)

    def save_modified_image(self):
        self.file_manager.save_image(self.current_image)

    def reset_image(self):
        self.current_image = self.original_images[self.current_image_index].copy()
        self.image_viewer.update_modified_image(self.current_image)
        self.controls.contrast_scale.set(1.0)