from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("\nYou've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
