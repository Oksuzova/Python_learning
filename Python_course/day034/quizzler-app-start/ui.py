from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=30)
        self.question_text = self.canvas.create_text(150, 125, text="question", width=250, font=("Arial", 20, "italic"))

        self.score = Label(text="Score: 0", font=("ariel", 14), fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, padx=50, pady=50, command=self.true_pressed)
        self.right_button.grid(column=0, row=2, padx=30, pady=30)

        self.wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, padx=50, pady=50, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2, padx=30, pady=30)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your current score is: {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



