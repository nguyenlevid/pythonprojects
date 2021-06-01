"""

ProgressBar can be used to display a progress bar in a graphical window showing
progress from 0-100%

"""
from graphics import *
import time

class ProgressBar:
    """
    A progress bar is a bar whose fill can be increased to show progress from  0%-100%.
    
    instance variables:
        bar (Bar): the outer rectangle of the progress bar
        fillBar (Bar): the inner filled rectangle of the progress bar
        percent (float): the current percentage completed shown by the progress bar (eg. 23.5)
        color (str): the color for the fill of the progress bar (default color is black)
    """
    
    def __init__(self, topLeft, width, height, color):
        """
        Creates a progress bar such as ProgressBar(Point(50, 75), 300, 20) which uses
        the default color black or ProgressBar(Point(50, 75), 300, 20, 'red')
        """
        bottomRight = Point(topLeft.getX() + width, topLeft.getY() + height)
        self.bar = Rectangle(topLeft, bottomRight)
        self.percent = 0
        self.color = color
        self.fillBar = Rectangle(topLeft, topLeft)
        
    def draw(self,win):
        """Draws the progress bar on the window"""
        self.fillBar.draw(win)
        self.bar.draw(win)


    def undraw(self):
        """undraw the progress bar"""
        self.bar.undraw()
        self.fillBar.undraw()
        
        
    def update(self, win, newPercent):
        """undraws and draws the progress bar at the same location with an updated percent completed"""

        if newPercent < 0:
            self.percent = 0
        elif newPercent > 100:
            self.percent = 100
        else:
            self.percent = newPercent
        self.percent = newPercent
        self.undraw()
        barWidth = (self.bar.getP2().getX() - self.bar.getP1().getX()) * self.percent / 100
        bottomRight = Point(self.bar.getP1().getX() + barWidth, self.bar.getP2().getY())
        self.fillBar = Rectangle(self.bar.getP1(), bottomRight)
        self.fillBar.setFill(self.color)
        self.fillBar.setOutline(self.color)
        self.draw(win)
    
    def __str__(self):
        return f'Border: {str(self.bar)};  Fill: {str(self.fillBar)}'


def main():
    """Test code for the ProgressBar class"""
    window = GraphWin("Progress", 600, 600)
    window.setBackground('white')
    
    # Add your code here to create the progress bars
    red_bar = ProgressBar(Point(50, 100), 300, 50, 'red')
    red_bar.draw(window)
    yellow_bar = ProgressBar(Point(50, 250), 200, 20, 'yellow')
    yellow_bar.draw(window)    
    blue_bar = ProgressBar(Point(50, 400), 500, 40, 'blue')
    blue_bar.draw(window)
    time.sleep(2)
    red_bar.update(window, 20)
    yellow_bar.update(window, 50)
    blue_bar.update(window, 75)
    time.sleep(2)
    red_bar.undraw()
if __name__ == '__main__':
    main()
    
    
        