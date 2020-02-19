# Generate random colors in python
import random

"""
    Type            Range
    ---------------------
    Hue:            0-360
    Saturation:     0-100
    Value:      0-100

    In the HSV model, hue is a circle,
    so we represent possible values out of 360.

    Different color ranges represent different colors...
    Red         falls between 0 and 60 degrees.
    Yellow      falls between 61 and 120 degrees.
    Green       falls between 121-180 degrees.
    Cyan        falls between 181-240 degrees.
    Blue        falls between 241-300 degrees.
    Magenta     falls between 301-360 degrees.

    Saturation and lightness are both percentages, so we will represent
    them as floats between 0 and 1.

"""

class Colors:
    def __init__(self, size):
        self.size = size
        self.base_set = [None] * size
        self.comp_set = [None] * size


        self.set_gen()
        self.comp_gen()

    def set_gen(self):

        for i in range(self.size):

            hue = random.randint(0, 360)
            sat = random.randint(0, 100)
            val = random.randint(40, 100)

            self.base_set[i] = (hue,sat,val)
    
    def comp_gen(self):
        for i in range(self.size):
            comp_hue = (self.base_set[i][0] + 180) % 360

            self.comp_set[i] = (comp_hue, self.base_set[i][1], self.base_set[i][2])



test_60 = Colors(1)
test_90 = Colors(1)
test_180 = Colors(1)


print(test.base_set)
print(test.comp_set)