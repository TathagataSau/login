from tkinter import *
window = Tk()
window.title("Hello Strange!")
window.geometry("600x800")
window.config(bg="white")
frame1 = Frame(window, bg = "orange", height = 300, width = 700 )
frame2 = Frame(window, bg = "green", height = 300, width = 700 )

inp = (Label(window,bg = "yellow", text = "Tathagata"))
frame1.pack(side = TOP)
frame2.pack(side = BOTTOM)
inp.pack()
window.mainloop()