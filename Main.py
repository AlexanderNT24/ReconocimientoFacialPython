#Librerias GUI
import tkinter 
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#Mis Modulos
import CapturarRostros
import EntrenandoReconocedor
import ReconocimientoFacial

import os

absPath = os.path.abspath(__file__)

path, nombreArchivo = os.path.split(absPath)

ventana=Tk()
ventana.geometry("800x500")
ventana.title("Reconocimiento")
ventana['bg'] = '#484644'

etiquetaTitulo = Label(ventana, text="Sistema de Reconocimiento Facial")
etiquetaTitulo.pack(fill="x",side="top")
etiquetaTitulo.config(fg="white",  bg="#0c2145", font=("Roboto",30),anchor="nw") 
     
etiquetaEntradasVideo = Label(ventana, text="Entradas de Video")
etiquetaEntradasVideo.place(x=200, y=100)
etiquetaEntradasVideo.config(bg="#484644",font=("Verdana",10)) 


def capturarNombre():  
    def capturar():
        nombre=cajaTextoNombre.get(1.0, tkinter.END+"-1c") 
        url=cajaTextoURL.get(1.0, tkinter.END+"-1c") 
        urlIP=cajaTextoURLIP.get(1.0, tkinter.END+"-1c") 
        iniciadorCapturador=CapturarRostros.CapturarRostros(format(radioValor.get()),nombre,url,urlIP)
    cajaTextoNombre =Text(ventana,width=20,height=1)
    cajaTextoNombre.place(x=150, y=100)
    botonCapturar=Button(ventana,text="Aceptar",command=capturar, bg="#484644",fg="white",activebackground="red").place(x=300, y=100)
   
def entrenar():
    iniciadorEntrenador=EntrenandoReconocedor.EntrenarRostros()

def reconocer():
    url=cajaTextoURL.get(1.0, tkinter.END+"-1c") 
    urlIP=cajaTextoURLIP.get(1.0, tkinter.END+"-1c") 
    iniciadorReconocedor=ReconocimientoFacial.ReconocerRostros(format(radioValor.get()),url,urlIP)

def mostrarCajaTextoURL():
    cajaTextoURLIP.place_forget() 
    cajaTextoURL.place(x=300, y=190)
    
def ocultarCajaTextoURL():
    cajaTextoURL.place_forget()
    cajaTextoURLIP.place_forget() 

def mostrarCajaTextoURLIP():
    cajaTextoURL.place_forget()
    cajaTextoURLIP.place(x=300, y=220)

imagenCapturar=PhotoImage(file=path+"\Imagenes\Camara.png")
imagenEntrenar=PhotoImage(file=path+"\Imagenes\Entrenar.png")
imagenReconocer=PhotoImage(file=path+"\Imagenes\Video.png")

cajaTextoURL =Text(ventana,width=20,height=1)
cajaTextoURLIP =Text(ventana,width=20,height=1)


#RadioButtons
radioValor=IntVar()

radioUnoCamaraTelefono=Radiobutton(ventana,text="Web Cam",variable=radioValor,value=1,bg="#484644",activebackground="#484644",command=ocultarCajaTextoURL).place(x=200, y=130)
radioDosWebCam=Radiobutton(ventana,text="Camara Telefono",variable=radioValor,value=2,bg="#484644",activebackground="#484644",command=ocultarCajaTextoURL).place(x=200, y=160)
radioTresStream=Radiobutton(ventana,text="Streaming",variable=radioValor,value=3, bg="#484644",activebackground="#484644",command=mostrarCajaTextoURL).place(x=200, y=190)
radioCuatroCamaraIP=Radiobutton(ventana,text="Camara IP",variable=radioValor,value=4,bg="#484644",activebackground="#484644",command=mostrarCajaTextoURLIP).place(x=200, y=220)

botonCapturar=Button(ventana,image=imagenCapturar,command=capturarNombre,relief="flat", bg="#484644",fg="white",activebackground="red").place(x=50, y=100)
botonEntrenar=Button(ventana,image=imagenEntrenar,command=entrenar,relief="flat", bg="#484644",fg="white",activebackground="red").place(x=50, y=200)
botonReconocer=Button(ventana,image=imagenReconocer,command=reconocer,relief="flat", bg="#484644",fg="white",activebackground="red").place(x=50, y=300)

ventana.mainloop()
