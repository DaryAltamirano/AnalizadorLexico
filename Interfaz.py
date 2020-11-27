from tkinter import *
from lexicoProyecto import analizarLex
from sintacticoProyecto import analizarSin


###METODOS DE APOYO

def getTextInputLex():
     texto= TextoCodigo.get(1.0,END)
     LabelResultado["text"]= analizarLex(texto)

def getTextInputSin():
     texto = TextoCodigo.get(1.0, END)
     LabelResultado["text"] = analizarSin(texto)

####INICIO DE LA INTERFAZ
raiz =Tk()
raiz.title("Analizador sintáctico")
raiz.resizable(0,0)
# FrameInicio(raiz)
# raiz.geometry("650x500")
# raiz.config(bg="lightblue")
miFrame = Frame(raiz, width="650", height="700", bg="lightblue")
miFrame.pack()
#
Label(miFrame, text="Ingrese algo para el analisis", fg="red", bg="lightblue",font=("Comic Sans MS", 22)).place(x=325, y=50, anchor="center")
# TEXTAREA
TextoCodigo = Text(miFrame, width=70, height=15, padx=10, pady=10)
TextoCodigo.place(x=325, y=200, anchor="center")
LabelResultado=Label(miFrame, text="Aqui ira el resultado del analisis", fg="red", bg="lightblue",font=("Arial Novas", 18))
LabelResultado.place(x=325, y=500, anchor="center")
# BOTONES
botonLexico = Button(miFrame, text="Analizador Lexico",command=getTextInputLex).place(x=150, y=600)
botonSintactico = Button(miFrame, text="Analizador Sintactico",command=getTextInputSin).place(x=400, y=600)


raiz.mainloop()
