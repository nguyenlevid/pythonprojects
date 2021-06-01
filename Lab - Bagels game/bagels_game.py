'''
This program plays the game of "Bagels" where the user tries to guess a number.
After each guess the user is given clues:
    "fermi" for correct digit in the correct position
    "pico" for correct digit is the wrong position
    "bagels" when every digit is incorrect
When the user guesses the number, the user is asked whether they want to play again.

    
'''
import random
NUM_DIGITS = 3    # number of digits in the number to be guessed

def intro():
    '''
    Introduces the game and explains the clues
    '''
    print('Welcome to Bagels!')
    print()
    print("I'm thinking of a", NUM_DIGITS, "digit number. Each digit is between")
    print("1 and 9. Try to guess my number.")
    print()
    print("I'll say \"fermi\" for each correct digit in the correct position.")
    print("I'll say \"pico\" for each correct digit in the wrong position.")
    print("I'll say \"bagels\" if all of the digits are wrong.")
  
  
def getClues(secretList, guessList):
    """
    Creates the clues for the user depending on how of the user's guess match the secret number to be guessed.
    
    Params:
    secretList: The number to be guessed as a list of characters
    guessList: The number guessed by the user as a list of characters
    
    Returns:
    a string of clues
    """
    # make copies so the parameter lists are not altered
    secretCopy = list(secretList)
    guessCopy = list(guessList)
    clues = ''
    
    # check for any correct digits in the correct position
    for index in range(NUM_DIGITS):
        if guessCopy[index] == secretCopy[index]:
            clues = clues + 'fermi '
            guessCopy[index] = 'X'
            secretCopy[index] = 'Y'
    
    # check for any correct digits in the wrong position
    for index in range(NUM_DIGITS):
        for index2 in range(NUM_DIGITS):
            if secretCopy[index] == guessCopy[index2]:
                clues = clues + 'pico '
                guessCopy[index2] = 'X'
   
    # if clues is '' then there were no correct digits
    if clues == '':
        clues = 'bagels'
        
    return clues


def getSecretList():
    '''
    Randomly generates the number the user will guess stored as a list of str digits.
    Each digit must be 1-9 inclusive
    
    Returns:
    a list of digits stored as strings for example ['1','3','5','5']
    '''
    import random
    secretlist = []
    for i in range(NUM_DIGITS):
        num = str(random.randrange(1,10))
        secretlist.append(num)
    return secretlist

def isGuessValid(guess):
    """
    Determines if the guess is valid. To be valid, it must have NUM_DIGIT characters,
    each character must be a digit, and none of the characters can be a '0'.
    
    Param:
    guess (str): the guess made by the user
    Returns:
    True if the guess is valid; False otherwise
    """
    length = len(guess)
    if length == NUM_DIGITS:
        if guess.isdigit():
            for num in range(length):
                if guess[num] == '0':
                    return False
            return True 
        else: 
            return False
    else:
        return False


def getUserGuessList():
    '''
    This function repeatedly asks the user to make a guess until the guess is valid.
    
    Returns:
    The valid guess entered by the user as a list of characters for example ['1', '3', '4', '7']
    '''
    guess = input('Your guess: ')
    while not isGuessValid(guess):
        print(f'You must enter {NUM_DIGITS} digits with no zeros. Try again.')
        guess = input('Your guess: ')
    guess = list(guess)
    return(guess)
    
def playOneRound():
    """
    Plays one round from generating the number to be guessed until the user guesses the number.
    When the user guesses the number, the number of guesses it took is displayed.
    """
    secretList = getSecretList()
    print(secretList)
    guessList = getUserGuessList()
    numTime = 1
    while secretList != guessList:
        print(getClues(secretList, guessList))
        guessList = getUserGuessList()
        numTime = numTime + 1
    if numTime == 1:
        print(f'You got it in 1 guess')
    else:
        print(f'You got it in {numTime} guesses')
        
        
def playAgain():
    """
    The function asks the user if they want to play again until
    the user answers 'y' or 'n', upper or lower case.
    
    Returns:
    the lowercase version of the user's y/n response lower case
    """
    answer = input('Do you want to play again (y/n)? ')
    answer = answer.lower()
    while answer != 'y':
        if answer != 'n':
            print('You must answer y or n. Try again.')
            answer = input('Do you want to play again (y/n)? ')
        else:
            return answer
    return answer
          

    
                
    
    

def main():
   intro()  
   response = 'y'
   while response =='y':
       print()
       playOneRound()
       print()
       response = playAgain()
           
if __name__ == '__main__':
   main()    
    
    
    
    
    
    