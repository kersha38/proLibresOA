from Tkinter import *
i=0
arreglo=['a','b','c','d']

def addrow(arr):
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, arr[j])
Titulos=['Nombre del OA','Descripcion','Autor','Intitucion','Fecha de creacion',
         'Palabras clave','Tamaño del archivo','tipo de archivo',
         'fecha de ingreso al repositorio']

addrow()
mainloop()