"""

Problem represents a randomly generated arithmetic problem with a whole number
answer. 

"""

import random

class Problem:
    """
    Represents one problem in our simple arithmetic quiz.
    The problems must be created so that the answers are always
    positive whole numbers (ie. 0, 1, 2, 3)
    
    instance variables:
    operand1 (int): the number left of the operation symbol
    operand2 (int): the number right of the operation symbol
    answer (int): the answer to the problem
    operation (str): the symbol for the operation ('+','-','*', '/')
    """
    def __init__(self):
        self.operand1 = 1
        self.operand2 = 1
        self.operation = '+'
        self.answer = 2
        
    def getOperand1(self):
        return self.operand1    
    def getOperand2(self):
        return self.operand2    
    def getAnswer(self):
        return self.answer    
    def getOperation(self):
        return self.operation
    
    def __addition(self):
        self.operand1 = random.randrange(0, 11)
        self.operand2 = random.randrange(0, 11)
        self.answer = self.operand1 + self.operand2
    def __subtraction(self):
        self.operand2 = random.randrange(11)        
        self.answer = random.randrange(11)
        self.operand1 = self.operand2 + self.answer
    def __multiplication(self):
        self.operand1 = random.randrange(0, 11)
        self.operand2 = random.randrange(0, 11)
        self.answer = self.operand1 * self.operand2
    def __division(self):
        self.operand2 = random.randrange(1,11)
        self.answer = random.randrange(11)
        self.operand1 = self.operand2 * self.answer
    
    def createNewProblem(self):
        operation_list = ['+', '-', '*', '/']
        self.operation = random.choice(operation_list)
        if self.operation == '+':
            self.__addition()
        elif self.operation == '-':
            self.__subtraction()
        elif self.operation == '*':
            self.__multiplication()
        else:
            self.__division()
    
    def __str__(self):
        return str(self.operand1) + ' ' + self.operation + ' ' + str(self.operand2) + ' = ' + str(self.answer)
    

    
def main():
    prob1 = Problem()
    print(prob1)
    print('Operand1:', prob1.getOperand1())
    print('Operand2:', prob1.getOperand2())
    print('Answer:', prob1.getAnswer())
    print('Operation:', prob1.getOperation())  
    print()
    
    for count in range(25):
        prob1.createNewProblem()
        print(prob1)
        
if __name__ == '__main__':
    main()
        