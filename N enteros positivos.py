from tkinter import *
from tkinter import messagebox

#---------------------
# Ventana Principal
#---------------------

#Se declara una varaiable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("wendy vargas")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x500")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="snow")

#---------------------
# Variables Globales
#---------------------  
x=StringVar()
z=IntVar()

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    z=int(x.get())*(int(x.get())+1)/2
    t_resultado.insert(INSERT, "Resultados:\n La suma de los primeros "+x.get()+" enteros positivos es : "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()


#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=780, height=240)
frame_entrada.place(x=10,y=10)

#Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Ejercicio 4")
titulo.config(bg="green yellow", fg="black" , font=("Arial", 20))
titulo.place(x=290, y=10)

#Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada,  text='Especialidad en Sistemas')
subtitulo.config(bg="azure", fg="grey1" , font=("Arial", 13))
subtitulo.place(x=290, y=50)

#Etiqueta para subtitulo2 de la app
subtitulo2 = Label(frame_entrada,  text="Enteros positivos")
subtitulo2.config(bg="slategray2", fg="black" , font=("Arial", 15))
subtitulo2.place(x=290, y=80)

logo= PhotoImage(file="uihola.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)

etiq_a=Label(frame_entrada, text="Número N = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=145)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=140)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="ivory2", width=780, height=120)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="Sumar.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)


bt_bor= PhotoImage(file="Borrar.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)


bt_sal= PhotoImage(file="Salir.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=585, y=7)


#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="pink", fg="grey1", font=("Courier", 12))
t_resultado.pack(expand=True)


ventana_principal.mainloop()