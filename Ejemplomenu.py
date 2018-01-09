from Tkinter import *
from tkFileDialog import askopenfilename
import os
import intCargar


def NewFile():
    #root.iconify()
    app=intCargar.cargar()
    print "New File!"



def OpenFile():
    name = askopenfilename()
    print name
    os.system(name)


def About():
    print "Repositorio de Objetos de Aprendizaje"


root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Objeto Aprendizaje", menu=filemenu)
filemenu.add_command(label="Guardar OA", command=NewFile)
filemenu.add_command(label="Abrir OA", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Ayuda", menu=helpmenu)
helpmenu.add_command(label="Acerca...", command=About)

mainloop()