from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

question_bank=[]

for data in question_data:
    question_bank.append(Question(data['question'],data['correct_answer']))
    
quiz=Quiz_brain(question_bank)

while quiz.still_has_question():

    quiz.next_question()

print('You\'ve completed the Quiz! ')
print(f'Your Final score is {quiz.score}/{len(question_bank)}')