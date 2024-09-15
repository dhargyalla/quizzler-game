from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self, quiz_brain:QuizBrain ):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzeller")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Label
        self.score_label = Label(text=f"Score:{self.score}", fg="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150,125, text="Helow this is samplle text and can be delete later", width=280, fill=THEME_COLOR,
                                font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Button
        self.button = Button()
        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.correct)
        self.right_button.grid(row=2, column=1)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of the quiz.")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def correct(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)
    def wrong(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):

        if answer:
            self.canvas.config(background="green")
        else:

            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)




