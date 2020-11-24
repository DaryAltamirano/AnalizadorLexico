from tkinter import *



###METODOS DE APOYO

def getTextInput():
    texto= TextoCodigo.get(1.0,END)   
    print(texto)





####INICIO DE LA INTERFAZ
raiz =Tk()
raiz.title("Analizador sintáctico")
raiz.resizable(0,0)
# raiz.geometry("650x500")
# raiz.config(bg="lightblue")


miFrame=Frame(raiz,width="650",height="450",bg="lightblue")
miFrame.pack()
# 
Label(miFrame,text="Ingrese algo para el analisis",fg="red",bg="lightblue",font=("Comic Sans MS",22)).place(x=325, y=50, anchor="center")
# TEXTAREA
TextoCodigo=Text(raiz,width=70,height=15,padx=10,pady=10)
TextoCodigo.place(x=325, y=200, anchor="center")
# BOTONES
botonLexico=Button(raiz,text="Analizador Lexico",command=getTextInput).place(x=150,y=400)
botonSintactico=Button(raiz,text="Analizador Sintactico",command=getTextInput).place(x=400,y=400)

raiz.mainloop()


