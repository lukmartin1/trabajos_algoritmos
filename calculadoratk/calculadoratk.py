import tkinter as tk
from tkinter import ttk
from operaciones import clicknum, operar, deletes, deleteall

ventana = tk.Tk()
ventana.geometry("360x400")
ventana.title("calculadora")
labres = tk.Label(ventana,pady=15, fg='black', relief='raised',width=10)


labres.grid(row=1,column=1,columnspan=4,sticky="nsew")


boton0 = tk.Button(ventana, text="0", pady=20,command=lambda:clicknum(labres,'0'))
boton1 = tk.Button(ventana, text="1",padx=30, pady=30,command=lambda:clicknum(labres,'1'))
boton2 = tk.Button(ventana, text="2",padx=30, pady=30,command=lambda:clicknum(labres,'2'))
boton3 = tk.Button(ventana, text="3",padx=30, pady=30,command=lambda:clicknum(labres,'3'))
boton4 = tk.Button(ventana, text="4",padx=30, pady=30,command=lambda:clicknum(labres,'4'))
boton5 = tk.Button(ventana, text="5",padx=30, pady=30,command=lambda:clicknum(labres,'5'))
boton6 = tk.Button(ventana, text="6",padx=30, pady=30,command=lambda:clicknum(labres,'6'))
boton7 = tk.Button(ventana, text="7",padx=30, pady=30,command=lambda:clicknum(labres,'7'))
boton8 = tk.Button(ventana, text="8",padx=30, pady=30,command=lambda:clicknum(labres,'8'))
boton9 = tk.Button(ventana, text="9",padx=30, pady=30,command=lambda:clicknum(labres,'9'))

botonplus = tk.Button(ventana, text="+",padx=20, pady=30,command=lambda:clicknum(labres,'+'))
botonminus = tk.Button(ventana, text="-",padx=20, pady=30,command=lambda:clicknum(labres,'-'))
botondiv = tk.Button(ventana, text="/",padx=20, pady=20,command=lambda:clicknum(labres,'/'))
botoneq = tk.Button(ventana, text="=",padx=20, pady=20,command=lambda:operar(labres))
botonmult = tk.Button(ventana,text="X",padx=30, pady=30,command=lambda:clicknum(labres,'*'))

botonC = tk.Button(ventana,text="C",padx=20, pady=30,command=lambda:deletes(labres))
botonCE = tk.Button(ventana,text="CE",padx=20, pady=30,command=lambda:deleteall(labres))

boton0.grid(row=5,column=1,columnspan=2,sticky="nsew")
boton1.grid(row=2,column=1,sticky="nsew")
boton2.grid(row=2,column=2,sticky="nsew")
boton3.grid(row=2,column=3,sticky="nsew")
boton4.grid(row=3,column=1,sticky="nsew")
boton5.grid(row=3,column=2,sticky="nsew")
boton6.grid(row=3,column=3,sticky="nsew")
boton7.grid(row=4,column=1,sticky="nsew")
boton8.grid(row=4,column=2,sticky="nsew")
boton9.grid(row=4,column=3,sticky="nsew")

botonminus.grid(row=2,column=4,sticky="nsew")
botonplus.grid(row=3,column=4,sticky="nsew")
botoneq.grid(row=5,column=4,sticky="nsew")
botondiv.grid(row=5,column=3,sticky="nsew")
botonmult.grid(row=4,column=4,sticky="nsew")
botonC.grid(row=1,column=5,sticky="nsew")
botonCE.grid(row=2,column=5,sticky="nsew")

ventana.mainloop()