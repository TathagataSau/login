from tkinter import *
from tkinter import messagebox

window = Tk()

messagebox.showerror("INFO", "Time is running out!")
robot = messagebox.askyesnocancel("Human!", " are you a robot?")

if robot == True:
    print("You can not get through")
elif robot ==  False:
    print("Go human!")
elif robot is None:
    print("cancelled")
mainloop()