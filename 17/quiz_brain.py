class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_num = self.question_number
        target_quiz = self.question_list[question_num]
        self.question_number += 1
        target_quiz_question = target_quiz.text
        user_answer = input(
            f"{self.question_number}. {target_quiz_question} (True/False)\nanswer: "
        )

        self.check_answer(user_answer, target_quiz.answer)

    def check_answer(self, user_answer: str, correct_answer:str):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong...")
            print(f'The correct answer is {correct_answer}.')
        
        print(f'{self.score}/{self.question_number}')
