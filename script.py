""" First part. Follow the circle"""

from PIL import Image

img = Image.open('circle.png', 'r')
width, height = img.size
pixels_list = list(img.getdata())
ix = 0
pixels_dict = {}
for y in range(height):
    for x in range(width):
        if pixels_list[ix] != (0, 0, 0):
            pixels_dict[(x, y)] = pixels_list[ix]
        ix += 1

pixels_sorted = sorted(pixels_dict.items())

file = open("file.txt", "w+")
for i in pixels_sorted:
    if i[0][0] in range(320, 480) and i[0][1] in range(160, 320):
        file.write("{} ".format(i[1][1]))
file.seek(0)
result_array = [[chr(int(i)) for i in line.split()] for line in file]
result_1 = "".join(result_array[0])

print "__________First part. Result.___________\n"
print result_1, "\n"

""" Second part. Decipher the code """

import bz2

pre_result_2 = "".join(result_1[:result_1.find("Congratulations")].split("pickles ")[1])
print "__________Second part. Result.___________\n"
print bz2.decompress(pre_result_2)
