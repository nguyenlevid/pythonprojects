"""
Click to draw donuts with sprinkles.
"""

from graphics import *
import random
import math

COLOR_LIST = ['red','blue','lime','black', 'magenta', 'darkviolet', 'deeppink3', 'dodgerblue1', 'firebrick2']
NUM_SPRINKLES = 150
SPRINKLE_RADIUS = 3
HOLE_RATIO = 1/3

def drawOneDonut(window, glazeColor, backgroundColor, radius, center):
    """
    The function draws one donut with color, size, and placement given by the parameters.
    
    Parameters:
    window (GraphWin): the window to draw the donut in
    glazeColor (str): a string for the color of the donut
    backgroundColor (str): a string for the color of the background used to draw the hole
    radius (int): the outer radius of the donut
    center (Point): the center point of the donut
    """


    donut = Circle(center, radius)
    donut.setFill(glazeColor)
    donut.draw(window)
    inside_circle = Circle(center, radius*HOLE_RATIO)
    inside_circle.setFill(backgroundColor)
    inside_circle.draw(window)
    drawSprinkles(window, center, donut)
        
def drawSprinkles(window, center, donut):
    x = center.getX()
    y = center.getY()
    circle_radius = donut.getRadius()
    radius = circle_radius
    for num in range(NUM_SPRINKLES):
        sprinkle_center_x = random.randrange(x-radius+3,x+radius-2)
        sprinkle_center_y = random.randrange(y-radius+3,y+radius-2)
        distance_sprinkle = math.sqrt((x-sprinkle_center_x)**2 + (y-sprinkle_center_y)**2)
        sprinkle_center = Point(sprinkle_center_x, sprinkle_center_y)
        sprinkle = Circle(sprinkle_center, SPRINKLE_RADIUS)
        if distance_sprinkle <= (radius - 3) and distance_sprinkle >= (radius*HOLE_RATIO + 3):
            sprinkle_color = random.choice(COLOR_LIST)        
            sprinkle.setFill(sprinkle_color)
            sprinkle.draw(window)
        else:
            sprinkle.undraw()
def main():
    # create window
    window = GraphWin("Donut Shop", 500, 500)
    window.setBackground('cyan')
    directions = Text(Point(250, 30), "Click three times to get your donuts!")
    directions.draw(window)
    
    
    # draw donuts in window
    center = window.getMouse()
    drawOneDonut(window, 'pink', 'cyan', 100, center)
    center = window.getMouse()
    drawOneDonut(window, 'yellow', 'cyan', 75, center)
    center = window.getMouse()
    drawOneDonut(window, 'brown', 'cyan', 85, center)

main()
    
    