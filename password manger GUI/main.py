import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def  generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + [random.choice(symbols) for char in range(nr_symbols)] + [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password =''.join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_text = web_entry.get()
    username_text = username_entry.get()
    pass_text = pass_entry.get()

    if len(web_text) == 0 or len(pass_text) == 0:
        messagebox.showinfo(title="oops!", message="please don't leave any of the fields empty")
    else:
        is_okay = messagebox.askokcancel(title=web_text, message=f"These are the details entered \nEmail: {username_text} \nPassword: {pass_text} \nIs it ok to save?")
        if is_okay:
            with open("data.txt", 'a') as password_file:
                password_file.write(f"{web_text} | {username_text} | {pass_text}\n")
                web_entry.delete(0, tk.END)
                pass_entry.delete(0, tk.END)
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = tk.Canvas(width=200, height=200)
padlock_img = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

web_label = tk.Label(text="Website")
web_label.grid(row=1, column=0)

username_label = tk.Label(text="Email/Username")
username_label.grid(row=2, column=0)

pass_label = tk.Label(text="Password")
pass_label.grid(row=3, column=0)


web_entry = tk.Entry(width=53)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=3)

username_entry = tk.Entry(width=53,)
username_entry.insert(0, string="succoth@pypi.org")
username_entry.grid(row=2, column=1, columnspan=2)

pass_entry = tk.Entry(width=35,)
pass_entry.grid(row=3, column=1)


generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)


add_button = tk.Button(text="Add", width=45, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()