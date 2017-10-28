from tkinter import *

root = Tk()

var1 = StringVar()
var1.set('Color')

opt1 = OptionMenu(root, var1, 'Rojo', 'Azul', 'Verde', 'Negro').pack(fill=X)

def state():
    print(var1.get())

Button(root, command=state, text='Ver Color').pack()

root.mainloop()