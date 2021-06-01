'''

The program displays a virtual aquarium with animated fish and floating bubbles.
It utilizes a Fish and Bubble class.

    
'''


from graphics import *
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEFAULT_FISH_NUM = 10
DEFAULT_BUBBLE_NUM = 25

#---------
# FISH CLASS
#---------

class Fish:
    """
    Fish class.
    Create constructor's instance variables to design tail, body, eyes for fish. Each fish has a random color.
    Create move method to make fish move and draw method to draw them.
    If a fish moves from right end to left end of the screen, it'll wrap around when passing the left end.
    If a fish moves from left end to right end of the screen, it'll wrap around when passing the right end.
    Make fish bob up (or down) in each count to 10. Count resets to 0 when reaching 20.
    Params:
        x(int): X coordinate of the center of fish.
        y(int): y coordinate of the center of fish.
        color(): random color of fish.
        speed(int): speed of fish.
        count(int): count to bob.
    """
    def __init__(self, x, y, color, speed, count):
    #design fish
        self.fish_body = Oval(Point(x-30, y-20), Point(x+30, y+20))
        self.fish_body.setFill(color)
        self.fish_speed = speed
        self.count = count
        #adjust fish' tail and eye depending on its direction
        if self.fish_speed > 0: 
            self.fish_tail = Oval(Point(x-25,y-30), Point(x-15,y+30))
            self.fish_tail.setFill(color)
            self.fish_eye = Circle(Point(x+15,y-8), 3)
            self.fish_eye.setFill('white')
        else:
            
            self.fish_tail = Oval(Point(x+25,y-30), Point(x+15,y+30))
            self.fish_tail.setFill(color)
            self.fish_eye = Circle(Point(x-15,y-8), 3)
            self.fish_eye.setFill('white')
    
    #fish moves
    def move(self):
        #fish moves with bobbing
        if self.count < 10:
            self.fish_tail.move(self.fish_speed, 1)
            self.fish_body.move(self.fish_speed, 1)
            self.fish_eye.move(self.fish_speed, 1)
            self.count = self.count + 1
        elif self.count < 20:
            self.fish_tail.move(self.fish_speed, -1)
            self.fish_body.move(self.fish_speed, -1)
            self.fish_eye.move(self.fish_speed, -1)
            self.count = self.count + 1
        else:
            self.count = 0
        
        #fish wraps around
        if self.fish_body.getCenter().getX() > WINDOW_WIDTH:             
            self.fish_tail.move(-WINDOW_WIDTH, 0)
            self.fish_body.move(-WINDOW_WIDTH, 0)
            self.fish_eye.move(-WINDOW_WIDTH, 0)  
        elif self.fish_body.getCenter().getX() < 0:
            self.fish_tail.move(WINDOW_WIDTH, 0)
            self.fish_body.move(WINDOW_WIDTH, 0)
            self.fish_eye.move(WINDOW_WIDTH, 0)
    #draw fish   
    def draw(self, window):
        self.fish_tail.draw(window)
        self.fish_body.draw(window)
        self.fish_eye.draw(window)
    
#---------
# BUBBLE CLASS
#---------

class Bubble:
    """
    Bubble class.
    Create constructor's instance variables to make white bubbles.
    Create move method to make bubbles move and draw method to draw them.
    Make bubbles bob left and right when going up (use count).
    Bubbles go from bottom to top and goes back to bottom to restart after reaching the top of the screen.
    Parameters:
        x(int): X coordinate of the center of bubble
        y(int): Y coordinate of the center of bubble
        speed(int): speed of bubble
        count(int): count to make bubbles bob
    
    """
    def __init__(self, x, y, speed, count):
    #create bubble
        self.bubble = Circle(Point(x, y), 5)
        self.bubble.setFill('white')
        self.bubble_speed = speed
        self.count = count
    def move(self):
        #bubble wraps around
        if self.bubble.getCenter().getY() > 0:
            #bubbles moves with bobbing
            if self.count < 10:
                self.bubble.move(1, self.bubble_speed)
                self.count = self.count + 1
            elif self.count < 20:
                self.bubble.move(-1, self.bubble_speed)
                self.count = self.count + 1
            else:
                self.count = 0
                
        else:
            self.bubble.move(0, WINDOW_HEIGHT)      
    
    def draw(self, window):
        self.bubble.draw(window)
        
#------------------
# HELPER FUNCTIONS
#------------------

def setUpInput(win, point, text):
    '''
    creates an Entry box with a label
    
    Params:
    win (GraphWin): the window the Entry box and label with be drawn in.
    point (Point): the location od the center of the text label
    text (str): the words that will be used to label the Entry box
    
    Returns:
    the Entry object created
    '''
    winText = Text(point, text)
    winText.setSize(18)
    winText.draw(win)
    winBox = Entry(Point(point.getX() + 225, point.getY()), 5)
    winBox.setSize(18)
    winBox.draw(win)
    return winBox

def getInput(win):
    '''
    Allows the user to enter the number of fish and bubbles for the aquarium.
    If a value is not entered or an invalid value (like a letter) is entered,
    the default number is used for that value.
    
    Params:
    win (GraphWin): the window the Entry box is in
    
    Returns:
    the number of fish and number of bubbles that will be drawn in the aquarium
    as a tuple
    '''
    directions = Text(Point(WINDOW_WIDTH/2 , 400), 'Enter the number of fish and bubbles, then click in the window.')
    directions.draw(win)
    fishEntry = setUpInput(win, Point(300, 200), "Enter number of fish:")
    bubbleEntry = setUpInput(win, Point(300, 300), "Enter number of bubbles:")
    win.getMouse()
    if fishEntry.getText().isdigit() and int(fishEntry.getText()) >= 0:
        numFish = int(fishEntry.getText())
    else:
        numFish = DEFAULT_FISH_NUM
    if bubbleEntry.getText().isdigit() and int(bubbleEntry.getText()) >= 0:
        numBubbles = int(bubbleEntry.getText())
    else:
        numBubbles = DEFAULT_BUBBLE_NUM
    fishEntry.undraw()
    bubbleEntry.undraw()
    directions.undraw()
    cover = Rectangle(Point(0, 0), Point(WINDOW_WIDTH, WINDOW_HEIGHT))
    cover.setFill("cyan")
    cover.draw(win)
    return numFish, numBubbles

def randColor():
    '''
    Returns a random color created from randomly generated red, green, and blue values
    '''
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return color_rgb(red, green, blue)


def setupFish(numFish):
    '''
    Creates the list of fish with random position, color and speed
    
    Params:
    numFish (int): the number of fish to be added to the list
    
    Returns:
    the list of fish
    '''
    #add random fish with random starting location to the fish list
    fishList = []
    speed_range = [-5,-4,-3,-2,-1,1,2,3,4,5] #leave out zero
    for num in range(numFish):
        fish = Fish(random.randrange(WINDOW_WIDTH), random.randrange(WINDOW_HEIGHT), randColor(), random.choice(speed_range), random.randrange(0, 20))
        fishList.append(fish)
        
    return fishList

def setupBubbles(numBubbles):
    '''
    Creates the list of bubbles with random position and speed
    
    Params:
    numBubbles (int): the number of bubbles to be added to the list
    
    Returns:
    the list of bubbbles
    '''
    #add random bubble with random starting location into bubble list
    bubbleList = []
    for num in range(numBubbles):
        bubble = Bubble(random.randrange(WINDOW_WIDTH), random.randrange(WINDOW_HEIGHT), random.randrange(-5,0), random.randrange(0, 20))
        bubbleList.append(bubble)
    return bubbleList
#------
# MAIN
#------
def main():

    # make the graphics window (use autoflush=False to update more frequently)
    # makes the animation move more smoothly
    win = GraphWin("Swimming Fish", WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
    win.setBackground("cyan2")
    
    numFish, numBubbles = getInput(win)
                      
    # call helper functions to setup the fish and bubble lists
    fishList = setupFish(numFish)
    
    bubbleList = setupBubbles(numBubbles)
    
    # draw the fish and bubbles in their initial locations
    for fish in fishList:
        fish.draw(win)
    for bubble in bubbleList:
        bubble.draw(win)   
        
    # continue swimming until the user clicks
    keepSwimming = True
    
    while keepSwimming:
        # loop through all the fish, moving each a little bit
        for fish in fishList:
            fish.move()

        # loop through all the bubbles, moving each a little bit
        for bubble in bubbleList:
            bubble.move()
        # The bubble are after the fish so that the bubbles are drawn in front of the fish

        
        update(50) # call update to flush the window
        # if user clicks: stop swimming
        if win.checkMouse() != None:
            keepSwimming = False

    win.close()

if __name__ == '__main__':
    main()
