'''
This program creates a game named "Dragon vs Spiders"
In this game:
    Use the dragon to spit fireballs at spiders. Move the dragon using the mouse clicking to direct.
    If the dragon destroys enough spiders before they escape, you win.
    For each spider getting by without being caught, you lose 1 point.
    If the dragon touches a spider, you lose.
'''
from graphics import *
import time
import random
import math
import sys

NUM_WIN = 25
FIREBALL_SPEED = -25
STALL_TIME = 0.05

def setup(win):
    """prompts player how to play and opt one out of 3 difficulty boxes, which will
    return the speed of the spiders and the speed of the dragon
    
    Parameters: win (GraphWin) for drawing the text and buttons
    """
    lobbyBackground = Image(Point(333,333), 'lobby_background.gif')
    lobbyBackground.draw(win)
    # Game prompts
    instructionBox = Rectangle(Point(80, 60), Point(580, 350))
    instructionBox.setOutline('black')
    textBox0 = Text(Point(333, 80), "INSTRUCTION")
    textBox1 = Text(Point(333, 111), "Shoot fireballs at the falling spiders and gain points.")
    textBox2 = Text(Point(333, 161), "Don't let them cross the bottom line or you will lose points!")
    textBox3 = Text(Point(333, 211), "If the spiders touch you, you lose! Click on the dragon to spit fireballs.")
    textBox4 = Text(Point(333, 261), "Click on the dragon's right side to move it right and its left side to move left.")
    textBox5 = Text(Point(333, 311), "When the dragon flies high and away upon winning, click to play again or to quit") 
    textBox0.setStyle('bold')
    textBox0.setSize(16)
    instructionBox.draw(win)
    textBox0.draw(win)
    textBox1.draw(win)
    textBox2.draw(win)
    textBox3.draw(win)
    textBox4.draw(win)
    textBox5.draw(win)
    
    # Difficulty selection
    difficultyText = Text(Point(333, 390), "SELECT THE LEVEL OF DIFFICULTY")
    difficultyText.setStyle("bold")
    difficultyText.setSize(16)
    difficultyText.setFace('courier')
    difficultyText.draw(win)
    
    # Level of Difficulty boxes
    easyBox = Rectangle(Point(66, 430), Point(166, 480))
    easyBox.setFill('lightgreen')
    easyText = Text(Point(116, 455), "Easy")
    easyText.setSize(14)
    easyText.setFace('courier')
    
    mediumBox = Rectangle(Point(283, 430), Point(383, 480))
    mediumBox.setFill('yellow')
    mediumText = Text(Point(333, 455), "Medium")
    mediumText.setSize(14)
    mediumText.setFace('courier')
    
    hardBox = Rectangle(Point(500, 430), Point(600, 480))
    hardBox.setFill('red')
    hardText = Text(Point(550, 455), "Hard")
    hardText.setSize(14)
    hardText.setFace('courier')
    
    easyBox.draw(win)
    easyText.draw(win)
    mediumBox.draw(win)
    mediumText.draw(win)
    hardBox.draw(win)
    hardText.draw(win)
    
    boxChoice = win.getMouse()
    SPIDER_SPEED = 0
    DRAGON_SPEED = 0
    
    while SPIDER_SPEED == 0:
        if 430 < boxChoice.getY() < 480:
            if 66 < boxChoice.getX() < 166:
                SPIDER_SPEED = 2
                DRAGON_SPEED = 50
            if 283 < boxChoice.getX() < 383:
                SPIDER_SPEED = 4
                DRAGON_SPEED = 40
            if 500 < boxChoice.getX() < 600:
                SPIDER_SPEED = 7
                DRAGON_SPEED = 30
        else:
            boxChoice = win.getMouse()
    boxChoice = win.checkMouse()
    return SPIDER_SPEED, DRAGON_SPEED

def distanceBetweenPoints(point1, point2):
    '''
    Calculates the distance between two points
    
    Paramêtrs:
    point1 (Point): the first point
    point2 (Point): the second point
    
    Returns:
    the distance between the two points
    '''
    p1x = point1.getX()
    p1y = point1.getY()
    p2x = point2.getX()
    p2y = point2.getY()
    return math.sqrt((p1x - p2x)*(p1x - p2x) + (p1y - p2y) * (p1y - p2y))


def isCloseEnough(aThing, spiderImg):
    '''
    Determines if the dragon and spider are close enough to say the dragon caught the spider
    
    Parameters:
    aThing (Image): the image of the dragon or the fireballs
    spiderImg (Image): the image of one particular spider
    
    Returns:
    True if distance between the center of the dragon or the fireballs and the center of the spider is less than a
    threshold to say the spider was caught. Otherwise, it returns False.
    '''
    threshold = aThing.getWidth() * 0.4 + spiderImg.getWidth() * 0.4
    distance = distanceBetweenPoints(aThing.getAnchor(), spiderImg.getAnchor())
    return distance < threshold


def moveDragon(win, dragon, fireBallList, DRAGON_SPEED):
    '''
    Use mouse clicking to move the dragon left or right and to shoot the fireball. 
    
    Parameters:
    
    win (GraphWin): the window where the witch is drawn
    dragon (Image): the image of the dragon
    fireBallList (list): list of image of fireball can be shooted
    DRAGON_SPEED (variable): speed of dragon
    
    '''
    mouse = win.checkMouse()
    dragonX = dragon.getAnchor().getX()
    dragonY = dragon.getAnchor().getY()   
    if mouse == None:
        ''
    elif mouse.getX() < dragonX - 50:
        dragon.move(-DRAGON_SPEED, 0)
    elif mouse.getX() > dragonX + 50:
        dragon.move(DRAGON_SPEED, 0)
    elif mouse.getX() > dragonX - 50 and mouse.getX() < dragonX + 50 and mouse.getY() > dragonY - 52:
        shootFireball(win, dragon, fireBallList)

def addSpiderToWindow(win):
    '''
    Draws the spider at a random location just above the top of the window
    
    Parameters:
    win (GraphWin): the window the spider will be drawn in
    
    Returns:
    an Image object of the spider which includes its initital location
    '''
    startX = random.randrange(75,610)
    startY = 0
    spider = Image(Point(startX, startY), 'spider.gif')
    spider.draw(win)
    return spider

def moveSpiders(spiderImgList, SPIDER_SPEED):
    '''
    moves each spider image in a list of spider images
    returns none
    Parameters:
    spiderImgList (list): a list of images of spiders that are currently falling
    SPIDER_SPEED: speed of spiders
    '''
    for spider in spiderImgList:
        spider.move(0,SPIDER_SPEED)

def shootFireball(win, dragon, fireBallList):
    """
    creates a new fireball at the dragon's position and adds it to the list
    returns none
    
    Parameters:
    win (GraphWin)
    dragon (Image)
    fireBallList (list)
    """
    fireBall_type = ['fireball1.gif', 'fireball2.gif']
    fireBall = Image(Point(dragon.getAnchor().getX(), dragon.getAnchor().getY()), random.choice(fireBall_type))
    fireBallList.append(fireBall)
    fireBall.draw(win)

def moveFireball(fireBallList):
    """
    moves all fireballs on-screen
    returns none
    Parameters:
    fireBallList (list), contains all fireballs on-screen
    """
    for fireBall in fireBallList:
        fireBall.move(0, FIREBALL_SPEED)


def gameLoop(win, dragon, SPIDER_SPEED, DRAGON_SPEED):
    '''
    Loop continues to allow the spiders to fall and the dragon to shoot 'em
    until enough spiders escape or the dragon destroys enough spiders to
    end the game. Or the dragon touches a spider and flees to end (lose).
    
    win (GraphWin): the window where game play takes place
    dragon (Image): the dragon image
    SPIDER_SPEED (int): speed of spider
    DRAGON_SPEED (int): speed of dragon
    '''
    spiderList = []
    fireBallList = []
    score = 0
    scoreBox = Rectangle(Point(450, 30), Point(550,70))
    scoreBox.setOutline('black')
    scoreWord = Text(Point(500, 45), 'SCORE')
    scoreLabel = Text(Point(500, 60), '0')
    scoreBox.draw(win)
    scoreWord.draw(win)
    scoreLabel.draw(win)
    
    while score < NUM_WIN:
        if random.randrange(100) < 6:
            newSpider = addSpiderToWindow(win)
            spiderList.append(newSpider)

        moveSpiders(spiderList, SPIDER_SPEED)
        moveDragon(win, dragon, fireBallList, DRAGON_SPEED)
        
        for fireBall in fireBallList:
            moveFireball(fireBallList)
        for spider in spiderList:
            if spider.getAnchor().getY() > 700:
                spider.undraw()
                spiderList.remove(spider)
                score = score - 1
                scoreLabel.setText(str(score))
            if isCloseEnough(dragon, spider):
                for spider in spiderList:
                    spider.undraw()
                for fireBall in fireBallList:
                    fireBall.undraw()
                dragon.undraw()
                scoreLabel.undraw()
                scoreBox.undraw()
                scoreWord.undraw()
                
                #Generates a pointillism as a losing sight
                f_in = open('skybackground.art', 'r')
                gifWidth = int(f_in.readline())
                scale = 666 / gifWidth
                for line in f_in:
                    dataList = line.split()
                    circlePoint = Point(int(int(dataList[0]) * scale), int(int(dataList[1]) * scale))
                    circleRadius = dataList[2]
                    circleColor = color_rgb(int(dataList[3]), int(dataList[4]), int(dataList[5]))
                    circle = Circle(circlePoint, int(circleRadius))
                    circle.setFill(circleColor)
                    circle.setOutline(circleColor)
                    circle.draw(win)
                losingText=Text(Point(333, 333), 'Game over, you lost!')
                losingText.setSize(20)
                losingText.setStyle('bold')
                losingText.draw(win)
                time.sleep(3)
                sys.exit(1)
            # When fireballs hit spiders or hits none
            for fireBall in fireBallList:
                if isCloseEnough(fireBall, spider):
                    spiderList.remove(spider)
                    spider.undraw()
                    fireBallList.remove(fireBall)
                    fireBall.undraw()
                    score = score + 1
                    scoreLabel.setText(str(score))
                elif fireBall.getAnchor().getY() < 0:
                    fireBallList.remove(fireBall)
                    fireBall.undraw()           

        time.sleep(STALL_TIME)

    time.sleep(3)
    # When reaching the winning score
    for spider in spiderList:
        spider.undraw()
    for fireBall in fireBallList:
        fireBall.undraw()
    scoreLabel.undraw()
    scoreBox.undraw()
    scoreWord.undraw()
    gameWin(win, dragon)

def gameWin(win, dragon):
    """
    the dragon flies away and informs that the player has won
    returns none
    
    Parameters:
    win (GraphWin)
    dragon (Image)
    """
    dragonX = dragon.getAnchor().getX()
    fly = 0
    while fly != 666:
        if dragonX > 333:
            dragon.move(-2, 0)
        elif dragonX < 333:
            dragon.move(2, 0)
        dragon.move(0, -2)
        time.sleep(.01)
        fly = fly + 1
        
    dragon.undraw()
    winningText = Text(Point(333, 180), 'You have defeated all the enemies. YOU WON!')
    winningText.setSize(20)
    winningText.setStyle('bold')
    winningText.draw(win)
    time.sleep(1)

def playAgain(win):
    """
    Prompts the player to play again or stop
    returns True if they click on yes, False if they
    click no
    
    Parameters:
    win (GraphWin)
    """
    againText = Text(Point(333, 280), "Begin another journey?")
    againText.setFill('black')
    againText.setSize(18)
    againText.setStyle('bold')
    againText.draw(win)
    
    yesBox = Rectangle(Point(172, 318), Point(272, 368))
    yesBox.setFill('lightgreen')
    yesText = Text(Point(222, 343), "YES")
    yesText.setStyle('bold')
    yesBox.draw(win)
    yesText.draw(win)
    
    noBox = Rectangle(Point(394, 318), Point(494, 368))
    noBox.setFill('red')
    noText = Text(Point(444, 343), "NO")
    noText.setStyle('bold')
    noBox.draw(win)
    noText.draw(win)
    boxChoice = win.getMouse()
    playerInput = ''
    while playerInput == '':
        if 318 < boxChoice.getY() < 368:
            if 172 < boxChoice.getX() < 272:
                playerInput = True
            elif 394 < boxChoice.getX() < 494:
                playerInput = False
        else:
            boxChoice = win.getMouse()
    boxChoice = win.checkMouse()
    return playerInput

def main():
    # setup the game 
    win = GraphWin("Arachnophobia!!!", 666,666)
    win.setBackground("white")
    SPIDER_SPEED, DRAGON_SPEED = setup(win)
    gameBackground = Image(Point(333,333), 'skybackground.gif')
    gameBackground.draw(win)
    dragon = Image(Point(333,580), "dragon.gif")
    dragon.draw(win)
    gameLoop(win, dragon, SPIDER_SPEED, DRAGON_SPEED)
    playerChoice = playAgain(win)
    while playerChoice:
        SPIDER_SPEED, DRAGON_SPEED = setup(win)
        gameBackground.undraw()
        gameBackground.draw(win)
        dragon = Image(Point(333,580), "dragon.gif")
        dragon.draw(win)
        gameLoop(win, dragon, SPIDER_SPEED, DRAGON_SPEED)
        playerChoice = playAgain(win)
    endText = Text(Point(333,100), "COME BACK SOON, WARRIOR!")
    endText.setSize(20)
    endText.setStyle('bold')
    endText.draw(win)
    time.sleep(2)
    sys.exit(1)    

if __name__ == "__main__":
    main()
    

