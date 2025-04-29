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
        self.filters = {
            'sobel': False,
            'median': False,
            'invert': False,
            'contrast': 1.0
        }
    
    def change_active_image(self, image_index):
        self.current_image_index = image_index
        self.current_image = self.original_images[image_index].copy()
        self.image_viewer.update_images(self.original_images[image_index], self.current_image)
        self.controls.contrast_scale.set(1.0)
    
    def switch_sobel_filter(self):
        self.filters['sobel'] = not self.filters['sobel']
        self.apply_filters()

    def switch_median_filter(self):
        self.filters['median'] = not self.filters['median']
        self.apply_filters()

    def switch_invert_colors(self):
        self.filters['invert'] = not self.filters['invert']
        self.apply_filters()

    def switch_adjust_contrast(self, value):
        self.filters['contrast'] = value
        self.apply_filters()

    def apply_filters(self):
        self.current_image = self.original_images[self.current_image_index].copy()
        if self.filters.get('sobel'):
            self.apply_sobel_filter()
        if self.filters.get('median'):
            self.apply_median_filter()
        if self.filters.get('invert'):
            self.invert_colors()
        if 'contrast' in self.filters:
            self.adjust_contrast(self.filters['contrast'])
        self.image_viewer.update_modified_image(self.current_image)

    def apply_sobel_filter(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.apply_sobel(self.current_image)
        
    
    def apply_median_filter(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.apply_median(self.current_image)
    
    def invert_colors(self):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.invert_colors(self.current_image)
    
    def adjust_contrast(self, value):
        from core.image_processor import ImageProcessor
        self.current_image = ImageProcessor.adjust_contrast(self.current_image, float(value))

    def save_modified_image(self):
        self.file_manager.save_image(self.current_image)

    def reset_image(self):
        self.current_image = self.original_images[self.current_image_index].copy()
        self.controls.contrast_scale.set(1.0)
        self.image_viewer.update_modified_image(self.current_image)
        self.filters = {
            'sobel': False,
            'median': False,
            'invert': False,
            'contrast': 1.0
        }
