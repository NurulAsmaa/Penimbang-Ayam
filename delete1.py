from tkinter import *

root = Tk()

txt = Text(root, font=('Verdana', 8))
txt.pack()

btn = Button(root, text='Delete', command=lambda: txt.delete(1.0,END))
btn.pack()

root.mainloop()
