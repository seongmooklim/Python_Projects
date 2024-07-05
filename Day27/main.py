from tkinter import *
from playground import add
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result_label.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height = 200)

miles_input = Entry(width=10)
miles_input.place(x=100, y=50)

Miles_label = Label(text = 'Miles', font = ('Arial', 10, "italic"))
Miles_label.place(x=175, y=50)

is_equal_label = Label(text = 'is equal to', font = ('Arial', 10, "italic"))
is_equal_label.place(x=25, y=75)

km_label = Label(text = 'Km', font = ('Arial', 10, "italic"))
km_label.place(x=225, y=75)

result_label = Label(font = ('Arial', 10, "italic"))
result_label.place(x=175, y=75)

button = Button(text='Calculate', command=miles_to_km)
button.place(x=100, y=100)

# #Label
# my_label = Label(text="I am a Label", font = ('Arial', 24, "italic"))
# my_label.pack()
#
# print(f"sum is {add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")
#
# my_label['text'] = "New Text"
#
#
# def button_clicked():
#     #print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
# button = Button(text='Click Me', command=button_clicked)
# button.pack()
#
# input = Entry(width=10)
# input.pack()
#
# new_button = Button(text="New Button")
# new_button.grid(column=10, row=10)
# #Entry
#
#

window.mainloop()
#End of Program
