# button.py
# A simple button widget implemented better than Zelle's text example


from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns True if the button is active and p is inside it.
    
    instance variables:
    rect (Rectangle): the rectangle representing the button
    label (Text): the text on the button
    active (bool): indicates whether the button will react to clicks(True)
    """

    def __init__(self, center, width, height, label):
        """
        Creates a rectangular button, eg:
        button = Button(Point(30,25), 20, 10, 'Quit')
        that is activated
        """ 
        # calculate the points the rectangle needs
        # from the center, width and height
        halfWidth = width/2.0
        halfHeight = height/2.0
        centerX = center.getX()
        centerY = center.getY()
        xMin = centerX - halfWidth
        xMax = centerX + halfWidth
        yMin = centerY - halfHeight
        yMax = centerY + halfHeight
        point1 = Point(xMin, yMin)
        point2 = Point(xMax, yMax)
        
        # create the instance variables
        self.rect = Rectangle(point1,point2)
        self.rect.setFill('lightgray')
        self.label = Text(center, label)
        self.active = False

    def draw(self,win):
        """Draws the button on the window"""
        self.rect.draw(win)
        self.label.draw(win)

    def undraw(self):
        """undraw the button"""
        self.rect.undraw()
        self.label.undraw()        

        
    def isClicked(self, point):
        "Returns true if button active and point is inside"
        xIsGood = self.rect.getP1().getX() < point.getX() < self.rect.getP2().getX()
        yIsGood = self.rect.getP1().getY() < point.getY() < self.rect.getP2().getY()
        return self.active and xIsGood and yIsGood

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def setLabel(self, newText):
        "Sets the label string of this button to the specified string."
        return self.label.setText(newText)
    
    def isActive(self):
        "Returns True if the button is activated, otherwise False"
        return self.active

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def move(self, dx, dy):
        "Move the button by offsets dx and dy"
        self.rect.move(dx, dy)
        self.label.move(dx,dy)


    def __str__(self):
        "returns a string/text version of this object"
        corner1 = self.rect.getP1()
        text = "A button with top left corner at: " + str(corner1.getX()) \
               + "," + str(corner1.getY())
        text = text + " with label= " + self.label.getText()
        return text
    

def main():
    # text code to see if we're on track!
    window = GraphWin("Testing Buttons", 400, 400)
    window.setBackground('white')
    
    rollButton = rollButton = Button(Point(200, 300), 150, 30, "Roll Dice")
    print(rollButton)




if __name__ == '__main__':
    main()








