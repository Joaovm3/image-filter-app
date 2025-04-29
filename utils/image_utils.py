from PIL import ImageTk

dimensions = (300, 300)

def convert_image_to_tk(image):
    resized_image = image.resize(dimensions)
    return ImageTk.PhotoImage(resized_image)
