from tkinter import *

window = Tk()
window.title("Challenge")
window.minsize(width=300, height=170)
window.config(padx=10, pady=10)


def converter():
    data = round(int(entry.get()) * 1.60934)
    convert.config(text=data)


label = Label(text="                         ")
label.grid(column=1, row=1)

entry = Entry(width=10)
entry.grid(column=2, row=1)
entry.insert(END, string="0")

miles = Label(text="Miles", font=("Arial", 14))
miles.grid(column=3, row=1)
miles.config(padx=10, pady=10)

equal = Label(text="is equal to", font=("Arial", 14))
equal.grid(column=1, row=2)
equal.config(padx=10, pady=10)

convert = Label(text="0", font=("Arial", 14))
convert.grid(column=2, row=2)
convert.config(padx=10, pady=10)

km = Label(text="Km", font=("Arial", 14))
km.grid(column=3, row=2)
km.config(padx=10, pady=10)

button = Button(text="Calculate", font=("Arial", 14), command=converter)
button.grid(column=2, row=3)
convert.config()

window.mainloop()
