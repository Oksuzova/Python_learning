from tkinter import *

window = Tk()
window.title("Challenge")
window.minsize(width=300, height=200)
window.config(padx=50, pady=70)

label = Label(text="Label", font=("Arial", 24, "bold"))
label.grid(column=1, row=1)
label.config(padx=20, pady=30)

button = Button(text="Button")
button.grid(column=2, row=2)

new_button = Button(text="New Button")
new_button.grid(column=3, row=1)

entry = Entry(width=10)
entry.grid(column=4, row=3)
entry.insert(END, string="Entry")







window.mainloop()
