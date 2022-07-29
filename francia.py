#se importa la libreria tkinter con todas sus funcines
from tkinter import *
 
#-----------------
# ventana principal
#------------------
 
#se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto tk()
ventana_principal = Tk()
 
# titulo de la ventana
ventana_principal.title("liseth dayana correa galvis")
 
# establecer tamaño a la ventana
ventana_principal.geometry("800x500")
 
#icono de la ventana
#ventana_principal.icobitmap("")
 
# deshabilitar boton de maximar
ventana_principal.resizable(0,0)
 
#color de fondo de la ventana principal
ventana_principal.config(bg="white")
 
frane_entrada= Frame(ventana_principal)
frane_entrada.config(bg='white',width=280,height=1000)
frane_entrada.place(x=250,y=0)
frane_entrada2= Frame(ventana_principal)
frane_entrada2.config(bg='blue',width=250,height=900)
frane_entrada2.place(x=0,y=0)
frane_entrada3= Frame(ventana_principal)
frane_entrada3.config(bg='red',width=280,height=900)
frane_entrada3.place(x=520,y=0)
 
 
# se ejecuta el metodo mainloop() de la clase tk() a traves de la instancia ventana_principal. este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton,escribir, etc). cada accion del usuario se conoce como un evento. el metodo mainloop()es un bucle infinito.
ventana_principal.mainloop()
