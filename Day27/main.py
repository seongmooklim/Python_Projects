import tkinter
from playground import add
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)

#Label
my_label = tkinter.Label(text="I am a Label", font = ('Arial', 24, "italic"))
my_label.pack()

print(f"sum is {add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")








window.mainloop()
#End of Program
