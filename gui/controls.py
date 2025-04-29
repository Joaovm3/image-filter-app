import tkinter as tk

class Controls:
    def __init__(self, root, main_window):
        self.main_window = main_window
        self.frame = tk.Frame(root)
        
        self.sobel_button = tk.Button(
            self.frame, text="Apply Sobel",
            command=lambda: self.main_window.change_filter('sobel')
        )
        self.sobel_button.pack(side=tk.LEFT, padx=5)
        
        self.median_button = tk.Button(
            self.frame, text="Apply Median",
            command=lambda: self.main_window.change_filter('median')
        )
        self.median_button.pack(side=tk.LEFT, padx=5)
        
        self.invert_button = tk.Button(
            self.frame, text="Invert Colors",
            command=lambda: self.main_window.change_filter('invert')
        )
        self.invert_button.pack(side=tk.LEFT, padx=5)
        
        self.contrast_scale = tk.Scale(
            self.frame, from_=0.0, to=2.0, resolution=0.1,
            orient=tk.HORIZONTAL, label="Contrast",
            command=lambda value: self.main_window.change_filter('contrast'),
            length=200
        )
        self.contrast_scale.set(1.0)
        self.contrast_scale.pack(side=tk.LEFT, padx=5)
        
        self.save_button = tk.Button(
            self.frame, text="Save Image",
            command=self.main_window.save_modified_image
        )
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(
            self.frame, text="Reset Image",
            command=self.main_window.reset_image
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
