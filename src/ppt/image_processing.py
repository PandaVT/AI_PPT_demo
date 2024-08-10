from PIL import Image

class ImageProcessing:
    def __init__(self, size):
        self.size = size

    def resize_image(self, image_path, output_path):
        try:
            with Image.open(image_path) as img:
                if img is None:
                    raise ValueError(f"Image not found or cannot be opened: {image_path}")
                img = img.resize(self.size, Image.Resampling.LANCZOS)  # 使用LANCZOS替代ANTIALIAS
                img.save(output_path)
        except Exception as e:
            print(f"Error processing image: {e}")
            raise

# Example usage
if __name__ == "__main__":
    image_processor = ImageProcessing(size=(640, 480))
    image_processor.resize_image("data/backgroud/demo.jpg", "output_image.jpg")
