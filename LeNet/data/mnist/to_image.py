import numpy as np
import struct
from PIL import Image

file_name = "t10k-images-idx3-ubyte"
bin_file = open(file_name, "rb")

buf = bin_file.read()

index = 0
magic, num_images, num_rows, num_columns = struct.unpack_from(">IIII", buf, index)
index += struct.calcsize(">IIII")

num_images = 10

for image in range(0, num_images):
    im = struct.unpack_from(">784B", buf, index)
    index += struct.calcsize("784B")

    im = np.array(im, dtype="uint8")
    im = im.reshape(28, 28)

    im = Image.fromarray(im)
    im.save("image/image_{}.bmp".format(image), "bmp")
    pass
