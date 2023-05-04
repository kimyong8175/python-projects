from data import question_data
from questiion_model import Question
from quiz_brain import QuizBrain


def main():
    question_bank = []

    for q in question_data:
        text = q["text"]
        answer = q["answer"]
        question_bank.append(Question(text, answer))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()


if __name__ == "__main__":
    main()
