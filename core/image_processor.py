import numpy as np
from PIL import Image
from core.filters import Filters

class ImageProcessor:
    @staticmethod
    def apply_sobel(image):
        image_array = np.array(image)
        sobel_array = Filters.apply_sobel(image_array)
        return Image.fromarray(sobel_array)

    @staticmethod
    def apply_median(image):
        image_array = np.array(image)
        median_array = Filters.apply_median(image_array)
        return Image.fromarray(median_array)

    @staticmethod
    def invert_colors(image):
        image_array = np.array(image)
        inverted_array = Filters.invert_colors(image_array)
        return Image.fromarray(inverted_array)

    @staticmethod
    def adjust_contrast(image, factor):
        image_array = np.array(image).astype(np.float32)
        mean = np.mean(image_array)
        adjusted = mean + factor * (image_array - mean)
        adjusted = np.clip(adjusted, 0, 255).astype(np.uint8)
        return Image.fromarray(adjusted)
