from tkinter import *
inp = "drawing"
window = Tk()

label = Label(window, text = f"{inp} board")
c = Canvas(window, width = 600, height = 600)

c.pack()
c.create_oval(10, 10, 590, 590, fill = "red", outline = "black", width = 5)
c.create_rectangle(100, 490, 490, 100, fill = "yellow",outline = "black", width = 5)
c.create_line(0, 0, 600, 600, width = 5, fill = "blue", dash = (4, 4))
c.create_line(0, 600, 600, 0, width = 5, fill = "red", dash = (4, 4))

label.pack()
mainloop()