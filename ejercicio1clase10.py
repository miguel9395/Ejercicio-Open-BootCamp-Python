######## Ejercicio 10 - 2 Miguel Zabala #########

import tkinter
from tkinter import ttk

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

root = tkinter.Tk()
opcion = tkinter.StringVar()
opcion.set(None)
tkinter.Radiobutton(root, text="Opcion 1", variable=opcion, 
            value='Opcion 1', command=seleccionar).pack()

tkinter.Radiobutton(root, text="Opcion 2", variable=opcion, 
            value='Opcion 2', command=seleccionar).pack()
tkinter.Radiobutton(root, text="Opcion 3", variable=opcion,   
            value='Opcion 3', command=seleccionar).pack()
tkinter.Radiobutton(root, text="Opcion 4", variable=opcion,   
            value='Opcion 4', command=seleccionar).pack()

monitor = tkinter.Label(root)
monitor.pack( )
tkinter.Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()