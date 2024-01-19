from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
next_word ={}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_lean = original_data.to_dict("records")
else:
    to_lean = data.to_dict("records")


def next_word():
    global new_word
    global flip_timer
    windows.after_cancel(flip_timer)
    new_word = random.choice(to_lean)
    canvas.itemconfig(title_label, text = "French", fill="black")
    canvas.itemconfig(word_label, text = new_word["French"], fill="black")
    canvas.itemconfig(card_background, image = front_img)
    flip_timer = windows.after(3000, flip)
    

def flip():
    canvas.itemconfig(title_label, text = "English", fill="white")
    canvas.itemconfig(word_label, text = new_word["English"], fill="white")
    canvas.itemconfig(card_background, image = back_img)

def is_known():
    to_lean.remove(new_word)

    words_to_learn = pandas.DataFrame(to_lean)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_word()

# print(data_record)

windows = Tk()
windows.title("Flash Card")
windows.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = windows.after(3000, flip)

back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

title_label = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 253, text="word", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)
next_word()






windows.mainloop()