from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pw_symbols + pw_numbers + pw_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # with open("data.txt", "r") as file:
    #     lines = file.readlines()
    #     with open("data.txt", "w") as file_data:
    #         for line in lines:
    #             if website and email not in line:
    #                 file_data.write(line)
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Do not leave any of the fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\n\nEmail: {email}\nPassword:"
                                               f" {password}\n\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
gui = Tk()
gui.title("Password Manager")
gui.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="E-mail/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "guerrerom90@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)

password_btn = Button(text="Generate Password", command=generate_pw)
password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=35, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)

gui.mainloop()
