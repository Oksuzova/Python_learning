from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import string
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    user_search = entry_web.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if user_search in data:
            email_data = data[user_search]["email"]
            password_data = data[user_search]["password"]
            messagebox.showinfo(title=user_search, message=f"Email: {email_data}\nPassword: {password_data}")
            pyperclip.copy(password_data)
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {user_search} exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    if len(entry_pass.get()) == 0:
        entry_pass.insert(END, string=password)
    else:
        entry_pass.delete(0, END)
        entry_pass.insert(END, string=password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = entry_web.get()
    login_data = entry_log.get()
    pass_data = entry_pass.get()
    new_data = {
        website_data: {
            "email": login_data,
            "password": pass_data,
        }
    }

    if website_data == "" or pass_data == "":
        messagebox.showinfo(title="Oops", message="Please, don`t left any field empty")
    else:

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            entry_pass.delete(0, END)
            entry_web.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

label_web = Label(text="Website:", font=("Arial", 10))
label_web.grid(column=0, row=1)
label_login = Label(text="Email/Username:")
label_login.grid(column=0, row=2)
label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3)

entry_web = Entry()
entry_web.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_web.focus()
entry_log = Entry(width=42)
entry_log.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_log.insert(0, "example@gmail.com")
entry_pass = Entry(width=24)
entry_pass.grid(column=1, row=3, sticky="EW")


gen_pass_button = Button(text="Generate Password", command=generate_pass)
gen_pass_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()
