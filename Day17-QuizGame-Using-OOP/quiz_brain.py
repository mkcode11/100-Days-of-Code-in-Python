class Quiz_brain:

    def __init__(self,q_list):

        self.q_num=0
        self.q_list=q_list
        self.score=0


    def still_has_question(self):
        return self.q_num<len(self.q_list)


    def next_question(self):

        current_question=self.q_list[self.q_num]
        self.q_num+=1
        user_answer=input(f'Q.{self.q_num} : {current_question.text} (True/False) : ')
        self.check_answer(user_answer,current_question.answer)



    def check_answer(self,user_answer,answer):

        if user_answer.lower()==answer.lower():
            self.score += 1
            print('You are Right!')
        else:
            print('That\'s wrong.')
        print(f'The correct answer is {answer}')
        print(f'Your current score is {self.score}/{self.q_num}\n')
