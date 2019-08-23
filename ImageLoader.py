from PIL import Image
def load(imageName):
    im = Image.open(imageName)
    try:
        ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBA", 0, -1)
        return (ix, iy, image)
    except SystemError:
        ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)
        return (ix, iy, image)