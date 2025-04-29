import numpy as np

class Filters:
    @staticmethod
    def apply_sobel(image_array):
        kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        
        grayscale = image_array.mean(axis=2)
        gradient_x = Filters.convolve(grayscale, kernel_x)
        gradient_y = Filters.convolve(grayscale, kernel_y)
        
        magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
        magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
        
        sobel_image = np.stack((magnitude, magnitude, magnitude), axis=2)
        return sobel_image

    @staticmethod
    def apply_median(image_array):
        padded = np.pad(image_array, ((1, 1), (1, 1), (0, 0)), mode='edge')
        new_image = np.zeros_like(image_array)
        
        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                for c in range(3):
                    neighborhood = padded[i:i+3, j:j+3, c].flatten()
                    new_image[i, j, c] = np.median(neighborhood)
        
        return new_image

    @staticmethod
    def invert_colors(image_array):
        return 255 - image_array

    @staticmethod
    def convolve(image, kernel):
        output = np.zeros_like(image)
        padded_image = np.pad(image, ((1, 1), (1, 1)), mode='edge')
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded_image[i:i+3, j:j+3]
                output[i, j] = np.sum(region * kernel)
        
        return output
