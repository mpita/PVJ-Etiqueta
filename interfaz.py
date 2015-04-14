import sys
from Tkinter import *
from pvj_iva import PvjMasIva

def holamundo():
    limpiar = Label(raiz, text=" ", width=100)
    limpiar.place(x = 250, y = 75, anchor = CENTER)
    precio = float(var_campo.get())
    pvj = PvjMasIva(precio)
    precio = pvj * 1.12
    etiqueta2 = Label(raiz, text="PVJUSTO "+str(round(pvj, 2))+" + IVA = Bs. "+str(round(precio, 2)), fg="blue", font=("Helvetica", 16))
    etiqueta2.place(x = 250, y = 75, anchor = CENTER)

def salir():
    raiz.destroy()

raiz = Tk()
var_campo = StringVar()
raiz.geometry('500x200+200+200')
raiz.title("Etiqueta de PVJ")
etiqueta = Label(raiz, text="Escriba el precio con IVA Incluido")
boton = Button(raiz, text="Generar", command = holamundo)
campo = Entry(raiz, textvariable=var_campo)
b_salir = Button(raiz, text="Salir", command = salir)

etiqueta.place(x = 30, y= 12.5)
campo.place(x = 250, y= 10)
boton.place(x = 15, y= 150)
b_salir.place(x = 430, y= 150)
raiz.mainloop()
