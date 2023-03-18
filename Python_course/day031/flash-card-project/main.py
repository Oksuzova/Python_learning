from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("./data/english_words.csv")
data_dict = data.to_dict(orient="records")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# def count_down(count):
#     count_sec = 5
#     count_sec = "0" + str(count_sec)
#     canvas.itemconfig(timer_text, text=f"{count_sec}")
#     timer = window.after(1000, count_down, count - 1)



# ---------------------------- WORDS GENERATOR ------------------------------- #


def words_generate():
    english_word = random.choice(data_dict)
    current_word = english_word["English"]
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_word)


# ------------------------------ UI SETUP ----------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=image)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=words_generate)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=words_generate)
wrong_button.grid(column=0, row=1)

title_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))


new_image = PhotoImage(file="./images/card_back.png")

# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Ariel", 35, "bold"))


words_generate()

window.mainloop()
