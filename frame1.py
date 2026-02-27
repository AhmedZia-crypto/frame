from tkinter import *

window = Tk()
window.title("sample frame")
window.geometry("600x400")

f1 = Frame(master=window, bg = 'green', height = '300', width = '500')
f1.pack()
f1.pack.propargate(False)


btn = Button(master=f1, text = "click here", fg = 'red ')
btn.pack()


f2 = Frame(master=window, bg = 'yellow', height = '100', width = '200')
f2.pack()
f2.pack.propargate(False)

btn1 = Button(master=f2, text = "click here", fg = 'brown ')
btn1.pack()

window.mainloop()