from PIL import Image
import math
im = Image.open('pikachu.jpg', 'r')
pix_val = list(im.getdata())
#white, orange, magenta, light blue, yellow, lime, pink, dark grey, light grey, cyan, purple, blue, brown, green, red, black
color_array = [(255, 255, 255, 0), (255, 102, 0, 1), (204, 0, 153, 2), (0, 204, 255, 3), (255, 204, 102, 4), (0, 204, 0, 5), (255, 102, 153, 6), (77, 77, 77, 7), (166, 166, 166, 8), (0, 153, 153, 9), (102, 0, 204, 10), (0, 0, 153, 11), (102, 51, 0, 12), (51, 102, 0, 13), (153, 0, 0, 14), (0, 0, 0, 15)]
pix_array = []
for pixel in pix_val:
	current_best = 1000
	for color in color_array:
		distance = math.sqrt((color[0] - pixel[0])**2 + (color[1] - pixel[1])**2 + (color[2] - pixel[2])**2)
		if distance < current_best:
			current_best = distance
			best_color = color[3]
	pix_array.append(best_color)
print(pix_array)
