from io import BufferedRandom
from tkinter import *

from first import button

#from tkinter import messagebox

window = Tk()
window.title("Message Box")
window.geometry("500x500")
label = Label(window, text = "Message Box")

var = StringVar()
ent_var = StringVar()
def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window, textvariable= var, relief= RAISED, padx = 20, pady = 20)

entry = Entry(window, textvariable= ent_var)
button  = Button(window, text = "OK", command = insert)

message.pack()
entry.pack()
button.pack()



label.pack()

mainloop()
