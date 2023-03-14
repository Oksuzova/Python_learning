from tkinter import *
import math
import tkinter.ttk as ttk
import threading


# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = None
p_value = 0


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, mark

    window.after_cancel(timer)
    label.config(text="Timer", font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
    mark = ""
    check.config(text=mark)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    pb['value'] = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps, mark, p_value
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps > 8:
        reset_timer()

    elif reps == 8:
        pb['value'] = 0
        mark += "✓"
        check.config(text=mark)
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
        p_value = long_break_sec
        threading.Thread(target=progress).start()
        window.attributes('-topmost', 1)

    elif reps % 2 == 0:
        pb['value'] = 0
        mark += "✓"
        check.config(text=mark)
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
        p_value = short_break_sec
        window.attributes('-topmost', 1)

    else:
        pb['value'] = 0
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
        window.attributes('-topmost', 0)
        p_value = work_sec




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        threading.Thread(target=progress).start()
    else:
        start_timer()


# ---------------------------- PROGRESSBAR ------------------------------- #


def progress():
    pb['value'] += 100/p_value


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

start_but = Button(text="Start", font=(FONT_NAME, 12), highlightthickness=0, command=start_timer)
start_but.grid(column=0, row=2)

reset_but = Button(text="Reset", font=(FONT_NAME, 12), highlightthickness=0, command=reset_timer)
reset_but.grid(column=2, row=2)

check = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

pb = ttk.Progressbar(window, mode="determinate")
pb.grid(column=1, row=4)


window.mainloop()
