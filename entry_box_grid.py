from tkinter import *
window = Tk()
window.title("Hello Stranger!")
window.geometry("250x50")
label1 = Label(window, text = "Email: ")
label2 = Label(window, text = "Password:")
en1 = Entry(window, width = 15, borderwidth= 5)
en2 = Entry(window, width = 15, borderwidth= 5)

label1.grid(row = 0, column = 1)
label2.grid(row = 1, column = 1)
en1.grid(row = 0, column = 2)
en2.grid(row = 1, column = 2)

window.mainloop()