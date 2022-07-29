# se importa la libreria de tkinder con todas sus funciones
from tkinter import *

#---------------------
#ventana principal
#---------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto TK()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Wendy Vanessa Vargas Corzo")

# establecer tamaño a la ventana
ventana_principal.geometry("800x500")

# icono de la ventana principal


# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la ventana principal
ventana_principal.config(bg="white")


#---------------------
#frame entrada
#---------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="yellow", width=780, height=240)
frame_entrada.place(x=10, y=10)
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue", width=780, height=120)
frame_entrada.place(x=10, y=250)
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=780, height=120)
frame_entrada.place(x=10, y=370)


#se ejecuta el metodo mainloop() de laclase Tk() a traves de instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuaro haga (click en boton,escribir, etc).cada accion del usuario se conoce como un evento. El metodo mainloop()es un bucle infinito.
ventana_principal.mainloop() 