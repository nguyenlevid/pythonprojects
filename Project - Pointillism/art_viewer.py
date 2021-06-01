"""

This program reads a text file created
from art_maker program (.art) and draws
circles to make pointilism of the image.


"""
from graphics import *
import tkinter as tk
from tkinter import filedialog

WINDOW_SIZE = 600

def display(artFileName):
    # Check file name
    if artFileName[-3:] != 'art':
        print("Invalid file format.")
        exit()
    else:
        window = GraphWin('Art Viewer', WINDOW_SIZE, WINDOW_SIZE)
        window.setBackground('black')
        file_open = open(artFileName, 'r')
        size = file_open.readline()
        # Scaling to make image properly sized
        scaleX = WINDOW_SIZE/int(size)
        scaleY = WINDOW_SIZE/int(size)
        # Read content from .art file to draw
        for line in file_open:
            data = line.split()
            xCenter = int(data[0])
            yCenter = int(data[1])
            radius = int(data[2])
            red = int(data[3])
            green = int(data[4])
            blue = int(data[5])
            circle_color = color_rgb(red, green, blue)
            circle = Circle(Point(xCenter*scaleX, yCenter*scaleY), radius)
            circle.setOutline(circle_color)
            circle.setFill(circle_color)
            circle.draw(window)


def main():
    # opens a file dialog to choose a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)
    display(file_path)

main()