from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/english_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}


# ---------------------------- WORDS GENERATOR ------------------------------- #
def words_generate():
    global current_card, new_canvas
    window.after_cancel(new_canvas)
    current_card = random.choice(data_dict)
    current_word = current_card["English"]
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_word, fill="black")
    canvas.itemconfig(canvas_image, image=image)
    new_canvas = window.after(3000, change_canvas)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def change_canvas():
    global current_card
    canvas.itemconfig(title_text, text="Russian", fill="white")
    canvas.itemconfig(canvas_image, image=new_image)
    current_word = current_card["Russian"]
    canvas.itemconfig(word_text, text=current_word, fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #
def is_known():
    data_dict.remove(current_card)
    words_generate()
    to_learn_data = pandas.DataFrame(data_dict)
    to_learn_data.to_csv("data/words_to_learn.csv", index=False)


# ------------------------------ UI SETUP ----------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

new_canvas = window.after(3000, change_canvas)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=image)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=words_generate)
wrong_button.grid(column=0, row=1)

title_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))


new_image = PhotoImage(file="./images/card_back.png")

words_generate()



window.mainloop()
