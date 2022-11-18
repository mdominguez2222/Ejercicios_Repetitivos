from tkinter import *
from tkinter import ttk

#Generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("250x300")
ventana.resizable(width=False,height=False)
ventana.config(background="aquamarine")
ventana.iconbitmap("")

#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()


#Componentes Label y Button
LabelTexto = ttk.Label(frm, text="Hola Tkinter")
LabelTexto.config(background="yellow", border=2, font=("Times New Roman",15))
LabelTexto.pack()

ttk.Button(frm, text="Salir", command=ventana.destroy).pack()


ventana.mainloop()