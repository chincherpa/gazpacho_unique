# resize an image using the PIL image library
# free from:  http://www.pythonware.com/products/pil/index.htm
# tested with Python24        vegaseat     11oct2005
from PIL import Image
import os

# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder

folder_src = "A:/unique"
folder_trg = "A:/unique/resized Pillow"

lall_filenames = os.listdir(folder_src)

quality_val = 100

def resize_image(filename_in, filename_out, new_width):
    print(filename_in)
    print(filename_out)
    print(new_width)
    im = Image.open(filename_in)

    width, height = im.size

    scale = int(new_width) / width
    new_height = int(height * scale)

    im_out = im.resize((new_width, new_height), Image.BICUBIC)
    im_out.save(filename_out, 'JPEG', quality=quality_val)


def bulk(all_filenames):
    for filename in all_filenames:
        if filename.endswith("jpg"):
            print(filename)
            imageFile = os.path.join(folder_src, filename)
            im = Image.open(imageFile)

            width, height = im.size
            # new_width = 3000

            scale = new_width / width
            new_height = int(height * scale)

            im2 = im.resize((new_width, new_height), Image.NEAREST)  # use nearest neighbour
            im3 = im.resize((new_width, new_height), Image.BILINEAR)  # linear interpolation in a 2x2 environment
            im4 = im.resize((new_width, new_height), Image.BICUBIC)  # cubic spline interpolation in a 4x4 environment
            im5 = im.resize((new_width, new_height), Image.ANTIALIAS)  # best down-sizing filter

            im2.save(os.path.join(folder_trg, "NEAREST", filename), 'JPEG', quality=quality_val)
            im3.save(os.path.join(folder_trg, "BILINEAR", filename), 'JPEG', quality=quality_val)
            im4.save(os.path.join(folder_trg, "BICUBIC", filename), 'JPEG', quality=quality_val)
            im5.save(os.path.join(folder_trg, "ANTIALIAS", filename), 'JPEG', quality=quality_val)
