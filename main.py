import numpy as np
from PIL import Image as im

# Set canvas size
h = 14
w = 11
max_value = 2**256  # max value allowed for uint256

# Get image and convert to matrix
img_path = input("Please enter the path of your image. Has to be 22p wide and 14p high.\n")
try:
    image = im.open(img_path)
except FileNotFoundError as E:
    print("File not found.")
    exit()

image_array = np.array(image)

# Split into left an right
left_split, right_split = np.split(image_array, 2, axis=1)

# Flatten 2d arrays into 1d
left_split = left_split.flatten(order='F')
right_split = right_split.flatten(order='F')

# Generate slots with 2 ^ x binaries
slot_map_left = np.array([2 ** x for x in range(h*w)])
slot_map_right = np.array([2 ** x for x in range(h*w)])

# Multiply image vector with slot matrix
zip_left_slots = slot_map_left * left_split
zip_right_slots = slot_map_right * right_split

# Sum up
left = zip_left_slots.sum()
right = zip_right_slots.sum()

if left > max_value or right > max_value:
    raise ValueError("Number too big. This Image cant be printed the way you would like.")
else:
    print(f"Left:\t{left} \nRight:\t{right}")
    print(f"CopyPaste for mint: {left},{right}")
