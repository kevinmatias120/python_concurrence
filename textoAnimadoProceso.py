#Importa módulos para Interfaz Gráfica de usuario (tkinter)
import tkinter as tk
from tkinter import ttk
import time
import os
import multiprocessing


#Función que crea y posiciona el botón "Salir"
def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)

#Función que crea una etiqueta (label) de texto en la posición (x,y) de la pantalla.
def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label

#Función que crea una etiqueta (llamando a createLabel()) y luego anima texto dentro de la misma.
def crearAnimacion(a, b, char):
    #nombre = multiprocessing.current_process().name
    #procId = multiprocessing.current_process().pid
    #pprocId = os.getppid()

    mylabel = createLabel(a,b)
    texto=""
    retardo: float=0.25
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text = texto)
        main_window.update_idletasks()
        main_window.update()
    time.sleep(2)
    #print(f"Este es el proceso {nombre} con PID = {str(procId)} y PPID = {pprocId}")



#Ejecutando con proceso

if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title("Ejemplo")
    main_window.configure(width=350, height=200)

    p1 = multiprocessing.Process(target=crearAnimacion, args=(10, 10, 'X'))
    p2 = multiprocessing.Process(target=crearAnimacion, args=(10, 30, 'Y'))
    p3 = multiprocessing.Process(target=crearAnimacion, args=(10, 50, 'Z'))

    p1.start()
    p2.start()
    p3.start()

    opcionFinalizar()
    main_window.mainloop()
