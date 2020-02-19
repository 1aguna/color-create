import colorgram
from PIL import Image
import sys
import csv
import os

dir_path = os.path.join( os.getcwd(), '..', 'images')
color_set = []
count = 0
for img_name in os.listdir(dir_path):
    if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
        print("Image " + str(count))
        count += 1
        row = []
        img_path = os.path.join(dir_path, img_name) # combine the current directory, and the image bane
        img_colors = colorgram.extract(img_path, 2)  # extract 2 colors from each image        
        # for color in img_colors:
        #     # print(color.rgb)

        #     # each color is a named tuple so to remove the named part,
        #     # i used the list function 
        #     color = list(color.rgb)
        #     # add the reformatted colors into the set of all img colors 
        #     print(color)

        # This creates a list of type list
        #
        # the outer list is a list where each value is a list itself
        # 
        # the inner list contains 4 values wehre each value is the 
        # rgb value of the colors 4 colors extracted from the image
        color1 = img_colors[0].hsl
        color2 = img_colors[1].hsl

        for val in color1:
            row.append(val)

        for val in color2:
            row.append(val)

        row.append(1) # target is 1 since it is a "good" combination

        color_set.append(row)

print(color_set[0])


with open("data_set.csv", "w+") as fp:
    wr = csv.writer(fp)
    header = ["hue_1", "saturation_1", "lightness_1", "hue_2", "saturation_2", "lightness_2", "good_combo"]
    wr.writerow(header)

    for r in color_set:
        wr.writerow(r)
