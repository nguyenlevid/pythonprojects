"""
This program helps convert a .gif file to a .art one
then it generates random x and y coordinates for pixels
with Red, Green, Blue colors. Finally it writes those onto the .art file.


"""
from graphics import *
import random
import tkinter as tk
from tkinter import filedialog

NUM_CIRCLES = 5000

def convert(imageFileName):
    image = Image(Point(0,0),imageFileName)
    
    # Converting .gif to .art
    convertFileName = imageFileName.replace('gif','art')
    file_out = open(convertFileName, 'w')
    imageWidth = image.getWidth()
    imageHeight =image.getHeight()
    file_out.write(f'{imageWidth} \n')
    
    # Generating points' information
    for num in range(NUM_CIRCLES):
        radius = random.randrange(2,9)
        x_position = random.randrange(imageWidth)
        y_position = random.randrange(imageHeight)
        colors = image.getPixel(x_position,y_position)
        file_out.write(f'{x_position} {y_position} {radius} {colors[0]} {colors[1]} {colors[2]} \n')
        
def main():
    # opens file dialog to choose a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    convert(file_path)

main()
