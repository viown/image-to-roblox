from PIL import Image
import model

def convert(image):
    image = Image.open(f"images/{image}")
    rows = image.size[0]
    col = image.size[1]
    MAIN = model.Main((rows * 2) - 2, col * 1.5)

    for y in range(1, col):
        for x in range(1, rows):
            getpixel = image.getpixel((x, y))
            MAIN += model.Pixel(getpixel[1], getpixel[2], getpixel[3])

    return MAIN

if __name__ == "__main__":
    print("Open console.py to convert images!")
    input()
