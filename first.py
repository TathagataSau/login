from tkinter import *
window = Tk()
window.title("Hello Stranger!")
window. geometry("600x890")
window.configure(bg="light blue")
inp = Label(window, text= "Hello World", bg = "blue", fg = "white" )
inp1 = Label(window, text= "Hello mice", bg = "black", fg = "white" )
inp2 = Label(window, text= "Hello cat", bg = "cyan", fg = "red" )

def log_entry():
    print("logged in")

button = Button(window, text = "Log In", command= log_entry, bg= "orange", fg = "white", font = ("bold", 40), activebackground = "light blue", activeforeground= "black")

inp.pack(side = TOP, fill = X, expand = False)
inp1.pack(side = LEFT, fill = Y, expand = False)
inp2.pack(side = RIGHT, fill = Y, expand = False)
button.pack()
window.mainloop()