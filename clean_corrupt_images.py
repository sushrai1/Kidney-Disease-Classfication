import os
from PIL import Image

def clean_corrupted_images(folder):
    count = 0
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            try:
                with Image.open(path) as img:
                    img.verify()
            except Exception:
                print(f"Removing corrupted image: {path}")
                os.remove(path)
                count += 1
    print(f"✅ Removed {count} corrupted images")

if __name__ == "__main__":
    clean_corrupted_images("artifacts/data_ingestion/kidney-ct-scan-image")
