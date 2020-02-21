#image processing library for image processing
from PIL import Image
#math library for square root
import math
#set variable im to read image
im = Image.open('hawaii-nc.jpg', 'r')
#set pix_val to array of (R, B, G) from im
pix_val = list(im.getdata())
#color_array is based on (R, G, B) values to match the map image file
#the 4th tuple in color_array is the index for minecraft script's block_array as well as the relative height (variable value in topo.js)
#blue(ocean)0, white(sand)1, dark green (lowlands)2, medium green3, lighter green 4, lightest green 5, light yellow 6, orange 7, dark orange 8, dark red orange 9, dark red 10, black 11
color_array = [(0, 0, 255, 0), (255, 255, 255, 1), (0, 102, 0, 2), (51, 153, 51, 3), (0, 204, 0, 4), (0, 255, 0, 5), (255, 255, 102, 6), (255, 204, 0, 7), (255, 153, 51, 8), (255, 102, 0, 9), (153, 0, 0, 10), (0, 0, 0, 11)]
pix_array = []
#iterate through pix_val and choose the best color by least difference for each pixel
for pixel in pix_val:
	#initialize current_best at an arbitrarily high value
	current_best = 1000
	#iterate through all colors in the array comparing the difference between color array items and the current pixel's RGB values
	for color in color_array:
		#distance is sqrt((R-r)^2+(B-b)^2+(G-g)^2)
		distance = math.sqrt((color[0] - pixel[0])**2 + (color[1] - pixel[1])**2 + (color[2] - pixel[2])**2)
		#set current_best to best_color if the distance is less than the current_best
		if distance < current_best:
			current_best = distance
			best_color = color[3]
	#add current best_color to the output array
	pix_array.append(best_color)
#print output array
print(pix_array)
