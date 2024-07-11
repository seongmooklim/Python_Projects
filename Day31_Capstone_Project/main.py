from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=900, height=676)
card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(450,290, image=card_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0)

right_image = PhotoImage(file="images/right.png")
right_image_label = Label(window, image=right_image)
right_image_label.grid(column=0, row=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_image_label = Label(window, image=wrong_image)
wrong_image_label.grid(column=2, row=2)

window.mainloop()
