import sys
from PIL import Image

path = sys.argv[0]
#opening map image
img = Image.open("p.JPG")

#getting width and height
width, heigth = img.size
ratio = heigth/width

#setting new width and height
new_width = 120
new_height = ratio*new_width*0.55
img = img.resize((new_width,int(new_height)))

#Returns a converted copy of map
img = img.convert('L')

#Returns the contents of map
pixels = img.getdata()
chars = ["1","0","1","0","1","0","1","0","1","0"," "]

#assigning new character for pixel
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

#getting length of pixel
new_pixels_count = len(new_pixels)

#replacing pixel with character
binary_map = [new_pixels[index:index+new_width]
 for index in range(0, new_pixels_count, new_width)]
binary_map = "\n".join(binary_map)

#wrting binary code in text
with open("binary_map.txt", 'w') as f:
	f.write(binary_map)