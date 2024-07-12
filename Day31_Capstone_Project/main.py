from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

all_Data = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    all_data = original_data.to_dict(orient="records")
else:
    all_data = data.to_dict(orient="records")
current_card = {}
def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(all_data)
    canvas.itemconfig(card_title, text="French",fill='black')
    canvas.itemconfig(card_word, text=current_card["French"],fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    all_data.remove(current_card)
    print(len(all_data))
    data = pandas.DataFrame(all_data)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)

card_title = canvas.create_text(400,150, text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel",60,"bold"))

unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image = unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
