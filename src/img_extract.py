import colorgram
from PIL import Image
from pathlib import Path
import sys
import os

def isImage(str):
    if str.endswith(".jpg") or str.endswith(".png") or str.endswith(".jpeg"):
        return True


"""

Switch colorgram to extcolor?

"""
def getColors(ec_list, iname):
    i = 1
    palette = []
    
    for color in ec_list:
        # each color is a named tuple so to remove the named part,
        # i used the list function and then turned it back into a tuple
        col_tuple = tuple(list(color.rgb))

        # create a 100x100 color block from the color_tuple
        img = Image.new('RGB', (100, 100), col_tuple)
        name_only = os.path.splitext(iname)[0]
        pname = name_only + "_" + str(i)

        # output the color block to the output dir
        output_dir = os.path.join(os.getcwd(), '..', 'output', pname )
        fname = output_dir + '_' + str(i)
        img.save(fname + ".jpg", "JPEG")

        palette.append(fname + ".jpg")
        i += 1

    # palette will be used for
    # stitching the individual images we just saved
    # into a single, row of images
    # so I stored each filename into palette
    # for when we stitch together the color  blocks next to eachother
    return palette

# create the row of new images
# from palette by lining up all the color blacks
# where each color block is offset from one another by
# its width (x dimension)
def stitchBlocks(blocks, num):
    opened = map(Image.open, blocks)
    opened = list(opened)

    widths, heights = zip(*(img.size for img in opened))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    # lineup the color blocks in a row
    # offset by their width
    x_offset = 0    


    # for each image, late them side by side
    # and then keep track of how much to offset
    # the next image by adding up the total width
    for im in opened:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    # file path manipulation
    # could use some cleaning up
    path = os.path.join(os.getcwd(), '..', 'output')
    c_fname = "combined_" + str(num) + ".png"

    
    new_im.save(os.path.join(path, c_fname), "PNG")
    return c_fname

def final_combine(image):
    opened = map(Image.open, blocks)
    opened = list(opened)

    widths, heights = zip(*(img.size for img in opened))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    # lineup the color blocks in a row
    # offset by their width
    x_offset = 0    
    for im in opened:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    # file path manipulation
    # could use some cleaning up
    path = os.path.join(os.getcwd(), '..', 'output')
    c_fname = "combined_" + str(num) + ".png"

    # save the stitched image together
    new_im.save(os.path.join(path, c_fname), "PNG")
    return c_fname


dir_path = os.path.join( os.getcwd(), '..', 'images')
j = 1

for img_name in os.listdir(dir_path):
    if isImage(img_name):

        palette = []

        # combine the current working directory and the image name
        img_path = os.path.join(dir_path, img_name) 
        extracted_colors = colorgram.extract(img_path, 2) 

        # extract the colors from the images
        # returns a list of color blocks
        color_blocks = getColors(extracted_colors, img_name)

        # stitch together the 4 color_blocks
        # return a list of files so we can delete them
        files = stitchBlocks(color_blocks, j)
        j += 1

        # delete the old color blocks used to make the stitched image
        for file in color_blocks:
            os.remove(file)

        # now vertically stitch the output along with the image

        """
            need to implement
        """


