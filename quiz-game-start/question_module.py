from data import question_data

class Question:
    
    def __init__(self, ques, ans):
        self.ques = ques
        self.ans = ans

    def display(self):
        return f"Q: {self.ques}\nA: {self.ans}"
    
    def question(self):
        return f"{self.ques}"
    def answer(self):
        return f"{self.ans}"