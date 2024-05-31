import tkinter as tk
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize quiz
quiz = QuizBrain(question_bank)

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg="#d35400")

        self.window.geometry("500x550")

        self.score_label = tk.Label(text="Score: 0", fg="white", bg="#d35400", font=("Arial", 14, "bold"))
        self.score_label.grid(row=0, column=1)

        self.timer_label = tk.Label(text="Time: 10", fg="white", bg="#d35400", font=("Arial", 14, "bold"))
        self.timer_label.grid(row=0, column=0)

        self.canvas = tk.Canvas(width=460, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            230,
            150,
            width=440,
            text="Question",
            fill="#d35400",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_button = tk.Button(text="True", command=self.true_pressed, width=15, height=3, bg="#27ae60", fg="white", font=("Arial", 12, "bold"))
        self.true_button.grid(row=2, column=0, pady=20)

        self.false_button = tk.Button(text="False", command=self.false_pressed, width=15, height=3, bg="#c0392b", fg="white", font=("Arial", 12, "bold"))
        self.false_button.grid(row=2, column=1, pady=20)

        self.score = 0
        self.timer = None
        self.time_left = 10
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.timer:
            self.window.after_cancel(self.timer)
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        if q_text is None:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.time_left = 10
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.timer = self.window.after(1000, self.countdown)
        else:
            self.give_feedback(False)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


if __name__ == "__main__":
    quiz_ui = QuizInterface(quiz)
