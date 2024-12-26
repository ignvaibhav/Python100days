import os
os.system("cls")
from main import *

class Quiz:
    def __init__(self):
        print("Let's begin the quiz!")
        print("\n")
        
    def questionPrint(self, currentQues):
        self.currentQues = currentQues
        answer = input(f"Q{currentQues+1}: {question_bank[currentQues].question()}. (True/False)? : ")
        tempAnswer = question_bank[currentQues].answer()

    def questionCheck(self):
        if answer != tempAnswer:
            return "wrong answer"
            
    
    
print("Let's begin the quiz!")
print("\n")
currentQues = 0

question1 = Quiz()

while currentQues < len(question_bank):
    question1.questionPrint(currentQues)
    question1.questionCheck()
    
    currentQues += 1