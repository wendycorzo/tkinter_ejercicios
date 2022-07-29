from tkinter import *
#---------------------
#frame entrada
#---------------------
ventana_kuban = Tk()
ventana_kuban.title("kuban")
ventana_kuban.geometry("800x500")
ventana_kuban.resizable(0,0)
ventana_kuban.config(bg="white")
frame_entrada = Frame(ventana_kuban)
frame_entrada.config(bg="purple", width=780, height=155)
frame_entrada.place(x=10, y=10)
frame_entrada = Frame(ventana_kuban)
frame_entrada.config(bg="violetred3", width=780, heigh=155)
frame_entrada.place(x=10, y=155)
frame_entrada = Frame(ventana_kuban)
frame_entrada.config(bg="green", width=780, heigh=155)
frame_entrada.place(x=10, y=300)
ventana_kuban.mainloop()
