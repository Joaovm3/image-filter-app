import tkinter as tk

class Controls:
    def __init__(self, root, main_window):
        self.main_window = main_window
        self.frame = tk.Frame(root)
        
        self.sobel_button = tk.Button(self.frame, text="Apply Sobel", command=self.main_window.switch_sobel_filter)
        self.sobel_button.pack(side=tk.LEFT, padx=5)
        
        self.median_button = tk.Button(self.frame, text="Apply Median", command=self.main_window.switch_median_filter)
        self.median_button.pack(side=tk.LEFT, padx=5)
        
        self.invert_button = tk.Button(self.frame, text="Invert Colors", command=self.main_window.switch_invert_colors)
        self.invert_button.pack(side=tk.LEFT, padx=5)
        
        self.contrast_scale = tk.Scale(self.frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Contrast", command=self.main_window.switch_adjust_contrast)
        self.contrast_scale.set(1.0)
        self.contrast_scale.pack(side=tk.LEFT, padx=5)
        
        self.save_button = tk.Button(self.frame, text="Save Image", command=self.main_window.save_modified_image)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(self.frame, text="Reset Image", command=self.main_window.reset_image)
        self.reset_button.pack(side=tk.LEFT, padx=5)
