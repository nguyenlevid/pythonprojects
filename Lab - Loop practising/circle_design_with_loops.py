"""
Draw circles using loops.
"""
from graphics import *


def main():
    numCircles = int(input("Enter number of circles: "))
    radius = int(input("Enter radius: "))
    # Create a window to draw the circle design in
    window = GraphWin("Circles", 800, 800)
    window.setBackground('white')
    # Draw the left vertical volume of circles
    x = radius  + 5
    y = radius + 5
    for num in range(numCircles-2):
        y = y + 2*radius
        center = Point(x, y) 
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
    # Draw the top horizontal volume of circles
    x = radius  + 5
    y = radius + 5
    for num in range(numCircles-2):
        x = x + 2*radius
        center = Point(x, y) 
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
    # Draw the right vertical volume of circles
    x = radius*2*numCircles - radius + 5
    y = radius + 5
    for num in range(numCircles-2):
        y = y + radius*2
        center = Point(x, y) 
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
    # Draw the bottom horizontal volume of circles
    y = radius*2*numCircles - radius + 5
    x = radius + 5
    for num in range(numCircles-2):
        x = x + radius*2
        center = Point(x, y) 
        circle = Circle(center, radius)
        circle.setOutline('red')        
        circle.draw(window)
    # Draw the first diagonal volume of circles
    x = radius + 5
    y = radius + 5
    center = Point(x, y) 
    circle = Circle(center, radius)
    circle.setOutline('blue')        
    circle.draw(window)
    for num in range(numCircles-1):
        x = x + radius*2
        y = y + radius*2
        center = Point(x, y) 
        circle = Circle(center, radius)
        circle.setOutline('blue')        
        circle.draw(window)
    # Draw the second diagonal volume of circles
    x = radius + 5
    y = radius*2*numCircles - radius + 5
    center = Point(x, y) 
    circle = Circle(center, radius)
    circle.setOutline('blue')        
    circle.draw(window)
    for num in range(numCircles-1):
        x = x + radius*2
        y = y - radius*2
        center = Point(x, y) 
        circle = Circle(center, radius)
        circle.setOutline('blue')        
        circle.draw(window) 

    window.getMouse()  # wait for the mouse to be clicked in the window.
    window.close()     # close the window after the mouse is clicked in the window.


main()