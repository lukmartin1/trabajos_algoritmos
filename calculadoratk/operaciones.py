import tkinter as tk


def clicknum(label,valor):

    current_text = label.cget('text')
    simbol = current_text[-1] if current_text else ""
    new_text = current_text + valor
    

    if len(current_text) == 0:
        if valor not in ('/','*'):   #agregar potencia
            label.config(text=new_text) 

    elif (simbol not in ('+', '-','/','*')) or (valor not in ('+', '-','/','*')) :
        label.config(text=new_text)      
        
    if simbol == '/' and valor == '0':
        label.after(100, lambda:deletes(label))
        error(label)
        

def deletes(label):
    current_text = label.cget('text')
    deltext = current_text[:len(current_text)-1]
    label.config(text=deltext)

def deleteall(label):
    label.config(text='')
       
def error(label):   
    label.config(bg='red')
    label.after(1000, lambda: label.config(bg='white'))

def operar(label):
    current_text = label.cget('text')
    simbol = current_text[-1] if current_text else ""
    if len(current_text) > 0 and simbol not in ('+', '-','/','*'):
        label.config(text=str(eval(current_text)))
