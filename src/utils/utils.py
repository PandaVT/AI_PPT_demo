# src/utils/utils.py
import os

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_text_to_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

# Example usage
if __name__ == "__main__":
    ensure_directory_exists("output/test_directory")
    save_text_to_file("Sample text", "output/test_directory/sample.txt")
