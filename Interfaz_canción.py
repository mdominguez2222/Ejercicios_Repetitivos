from tkinter import *
from tkinter import ttk

from pytube import YouTube

def descargaCancion():
    url = datos_Entrada.get()
    youtube = YouTube(url)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

'''
def descargarLista(url:str):
    playlist = Playlist(url)
    for cancion in playlist.videos:
        print (f"Descargando canción: {cancion.title}")
        #descagarCancion(cancion)         
        cancion.streams.get_audio_only().download("canciones/")
        print ("*************\n")
'''

#Programa principal


descargaCancion(url)




ventana = Tk()
ventana.title("Descargar música YouTube :)")
ventana.geometry("500x200")
ventana.resizable(False,False)
ventana.config(background="aquamarine")

datos_Entrada =ttk.Entry(ventana)
datos_Entrada.place(x=170, y=30)

boton_Descargar = ttk.Button(ventana, text="Descargar", command=descargaCancion)
boton_Descargar.place(x=210, y=60)

label_Titulo = ttk.Label(ventana, text="Introduce la url del video:")
label_Titulo.config(background="aquamarine", border=2, font=("Times New Roman",12))
label_Titulo.place(x=5 ,y=30)


ventana.mainloop()

