from tkinter import *
from tkinter import ttk

def saludar():
    texto = campoTexto.get()
    textoLabel.set(texto)


#Generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("250x300")
ventana.resizable(width=False,height=False)
ventana.config(background="aquamarine")


#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()


#Componentes Label y Button
textoLabel = StringVar()
textoLabel.set("Hola Tkinter")
LabelTexto = ttk.Label(frm, textvariable=textoLabel)
LabelTexto.config(background="yellow", border=2, font=("Times New Roman",15))
LabelTexto.pack()

#Componente cuadro de texto
campoTexto = ttk.Entry(frm)
campoTexto.pack()



ttk.Button(frm, text="Saludos", command=saludar).pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()



ventana.mainloop()