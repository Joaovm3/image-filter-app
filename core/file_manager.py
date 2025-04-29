from PIL import Image
import os

class FileManager:
    def __init__(self):
        self.assets_folder = "assets"
    
    def load_images(self):
        images = []
        for file_name in sorted(os.listdir(self.assets_folder))[:4]:
            image_path = os.path.join(self.assets_folder, file_name)
            image = Image.open(image_path).convert("RGB")
            images.append(image)
        return images
    
    def save_image(self, image):
        save_path = os.path.join(self.assets_folder, "modified_image.png")
        image.save(save_path)
