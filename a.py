import os
from pathlib import Path
from PIL import Image

def get_image_dimensions(folder_path):
    """
    Analyze all images in a folder and report their dimensions.
    
    Args:
        folder_path: Path to the folder containing images
    """
    
    # Check if folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder")
        return
    
    # Common image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.ico'}
    
    # Find all image files
    image_files = []
    for file in os.listdir(folder_path):
        if Path(file).suffix.lower() in image_extensions:
            image_files.append(file)
    
    if not image_files:
        print(f"No images found in '{folder_path}'")
        return
    
    print(f"\nImage Dimensions in '{folder_path}':")
    print("=" * 70)
    
    for filename in sorted(image_files):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"{filename}")
                print(f"  Dimensions: {width} x {height} pixels")
                print(f"  File Size: {file_size_mb:.2f} MB")
                print()
        
        except Exception as e:
            print(f"{filename}")
            print(f"  Error: Could not read image - {str(e)}")
            print()
    
    print("=" * 70)

if __name__ == "__main__":
    # Specify your folder path here
    folder = input("Enter the folder path containing images: ").strip()
    get_image_dimensions(folder)