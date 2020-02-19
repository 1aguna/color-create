# bunny-learn
Bunny-learn is a program that suggests a color scheme to users when given an input color. Bunny-learn uses machine learning to learn which colors are complimentary with other colors in order to create a beautiful color palette!

# Project Overview
The goal of this project is to be able to generate color palettes given a single color or photo. 

There are multiple ways to generate color palettes...

# Methodology
## Set up an extraction
* Gather a bunch of images together
* We will extract a number color palettes from all the images (possibly 5 colors per image)
* Put all the extracted color palettes into lists

## A user will input a color...
* Use machine learning to match the inputted color with a color in the list
* Use the matched color in the list to recommend other colors by iterating the list of extracted colors

***
# Methods to attempt in the future


## Machine Learning

### Classification 
We can use logistic regression in machine learning to classify if colors are "good" or "bad" together.
1) Get a batch of pre-assembled colors we believe are "good" together
2) Use those colors and use a color difference algorithm to extrapolate the "good" set, to a much large 
set of "good" color. Possibly 1,000's of colors together.
3) We train a model with the big set of "good" colors
4) After we trained the model, we can have our program randomly generate colors, and our model will 
  give us a probability if whether the colors are "good" 
5) if they the probability is greater than a chosen threshold, we can use it to create a color palette

### Using Color Theory and Math
We can also use more traditional methods to generate colors
* https://www.ethangardner.com/articles/2009/03/15/a-math-based-approach-to-color-theory-using-hue-saturation-and-brightness-hsb/
* Using the color difference algorithm previously mentioned

#
