from question_module import Question
from data import question_data

import os
os.system("cls")

question_bank = []

for i in question_data:
    ques = i["text"]
    ans = i["answer"]
    new_ques = Question(ques, ans)
    question_bank.append(new_ques)
# print(question_bank)
# for question in question_bank:
#     print(question.display())