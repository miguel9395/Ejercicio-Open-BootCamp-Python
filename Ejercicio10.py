import tkinter
from tkinter import ttk


window = tkinter.Tk()
elemento = tkinter.StringVar()
listbox = tkinter.Listbox(window)

for item in ["Estados Unidos", "Mexico", "Colombia", "Peru", "Venezuela", "Bolivia", "Canada", "Argentina"]:

 listbox.insert(tkinter.END, item)

listbox.pack()

label = tkinter.Label(text="Seleccione su pais")
label.pack()
window.mainloop()

