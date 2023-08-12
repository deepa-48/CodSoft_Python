import tkinter as tk

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x500")  # Set window size

        self.questions = [
            {
                "question": "Total Keyword in Python?",
                "choices": [33,35,30,32],
                "correct_choice": 0,
            },
            {
                "question": "Output of 2**3?",
                "choices": [8,6,12,9],
                "correct_choice": 0,
            },
            {
                "question": "Output of np.arange(1,5)?",
                "choices": [[1,2,3,4,5],[0,1,2,3,4],[1,2,3,4,5],[1,2,3,4]],
                "correct_choice": 3,
            },
            {
                "question": "Which Keyword is used to declare function?",
                "choices": ["define","def","none","push"],
                "correct_choice": 1,
            },
            {
                "question": "Output of 2*12?",
                "choices": [22,26,24,28],
                "correct_choice": 2,
            },
        ]
        self.score = 0
        self.question_index = 0

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.question_label = tk.Label(
            root, text="", font=("Helvetica", 14, "bold"), wraplength=380
        )
        self.question_label.pack(pady=10)

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(
                root,
                text="",
                font=("Helvetica", 12),
                command=lambda idx=i: self.check_answer(idx),
                width=30,
            )
            self.choice_buttons.append(button)
            button.pack(pady=5)

        self.play_again_button = tk.Button(
            root, text="Play Again", font=("Helvetica", 12), command=self.play_again
        )

        self.next_question()

    def next_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            self.question_label.config(text=question["question"])
            for i in range(4):
                self.choice_buttons[i].config(text=question["choices"][i])
            self.question_index += 1
        else:
            self.display_final_score()
            self.play_again_button.pack(pady=20)  # Show the Play Again button

    def check_answer(self, user_choice):
        question = self.questions[self.question_index - 1]
        if user_choice == question["correct_choice"]:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

    def display_final_score(self):
        self.final_score_label = tk.Label(
            self.root,
            text=f"Quiz completed!\nYour final score: {self.score} out of {len(self.questions)}",
            font=("Helvetica", 14),
            wraplength=380,
        )
        self.final_score_label.pack(pady=20)

    def play_again(self):
        self.score = 0
        self.question_index = 0
        self.score_label.config(text="Score: 0")
        self.final_score_label.pack_forget()  # Hide the final score label
        self.play_again_button.pack_forget()  # Hide the Play Again button
        self.next_question()


if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGameGUI(root)
    root.mainloop()
