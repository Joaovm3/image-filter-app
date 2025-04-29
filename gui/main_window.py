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
        self.current_image_index = 0
        self.current_image = self.original_images[self.current_image_index].copy()
        self.current_image_without_contrast = self.current_image.copy()

        self.filters = {
            'sobel': False,
            'median': False,
            'invert': False,
            'contrast': 1.0
        }

        self.image_viewer = ImageViewer(
            self.root, 
            self.original_images[self.current_image_index], 
            self.current_image, 
            self.original_images
        )

        self.controls = Controls(self.root, self)
        self.controls.frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.image_viewer.frame.pack(side=tk.TOP, padx=10, pady=10)
        self.image_viewer.bind_preview_click(self.change_active_image)
        
    def change_active_image(self, image_index):
        self.current_image_index = image_index
        self.reset_image()
        
    def change_filter(self, filter_name):
        from core.image_processor import ImageProcessor

        if filter_name in ['sobel', 'median', 'invert']:
            self.filters[filter_name] = not self.filters[filter_name]
            self.current_image = self.original_images[self.current_image_index].copy()

            if self.filters['sobel']:
                self.current_image = ImageProcessor.apply_sobel(self.current_image)
            if self.filters['median']:
                self.current_image = ImageProcessor.apply_median(self.current_image)
            if self.filters['invert']:
                self.current_image = ImageProcessor.invert_colors(self.current_image)
            self.current_image_without_contrast = self.current_image.copy()
            if self.filters['contrast'] != 1.0:
                self.current_image = ImageProcessor.adjust_contrast(self.current_image, self.filters['contrast'])

        elif filter_name == 'contrast':
            self.filters['contrast'] = float(self.controls.contrast_scale.get())
            temp_image = self.current_image_without_contrast.copy()
            self.current_image = ImageProcessor.adjust_contrast(temp_image, self.filters['contrast'])

        self.image_viewer.update_modified_image(self.current_image)

    def reset_image(self):
        self.current_image = self.original_images[self.current_image_index].copy()
        self.current_image_without_contrast = self.current_image.copy()
        self.image_viewer.update_images(self.current_image, self.current_image)
        self.controls.contrast_scale.set(1.0)
        self.filters = {
            'sobel': False,
            'median': False,
            'invert': False,
            'contrast': 1.0
        }

    def save_modified_image(self):
        self.file_manager.save_image(self.current_image)
        