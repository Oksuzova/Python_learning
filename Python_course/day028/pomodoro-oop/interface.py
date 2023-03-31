from tkinter import *
import tkinter.ttk as ttk



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


class PomodoroInterface:

    def __init__(self):

        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        self.label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
        self.label.grid(column=1, row=0)

        self.start_but = Button(text="Start", font=(FONT_NAME, 12), highlightthickness=0, command=self.start_timer)
        self.start_but.grid(column=0, row=2)

        self.reset_but = Button(text="Reset", font=(FONT_NAME, 12), highlightthickness=0, command=self.reset_timer)
        self.reset_but.grid(column=2, row=2)

        self.check = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
        self.check.grid(column=1, row=3)

        self.pb = ttk.Progressbar(self.window, mode="determinate")
        self.pb.grid(column=1, row=4)

        self.window.mainloop()

    def start_timer(self):
        pass

    def reset_timer(self):
        pass
