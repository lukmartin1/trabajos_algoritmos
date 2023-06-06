from cola import Cola
from pila import Pila
from datetime import time
import os

def limpiar_consola():          #funcion para limpiar la consola
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

cola = Cola()
cola_aux = Cola()
pilatime = Pila()

horain = time(11, 43, 00)        
horafin = time(15,57,00)
n = 3

def limpiatodo():                #funcion que inicializa las estructuras a utilizar
    while cola.size()>0:
        cola.atention()
    while cola_aux.size()>0:
        cola_aux.atention()
    while pilatime.size()>0:
        pilatime.pop()       
    
def notiface(limite):
    for i in range(limite):
        auxate = cola.atention()
        if auxate["aplicacion"] != "facebook":
            cola_aux.arrive(auxate)

    while cola_aux.size()>0:
        cola.arrive(cola_aux.atention())

def twitter(limite):
    for i in range(limite):
        auxatev2 = cola.atention()             
        if auxatev2["aplicacion"] == "twitter":
            palabras = auxatev2["mensaje: "].split() 
            if "python" in palabras:  
                print(auxatev2)  

        cola_aux.arrive(auxatev2)      

    for i in range(cola_aux.size()):
        cola.arrive(cola_aux.atention())  


def ranghora(limite):                              #carga en la pila las notificaciones que cumplen el rango horario
    for i in range(limite):
        auxora = cola.atention()
        if horain <= auxora["hora: "] <= horafin:
            pilatime.push(auxora)
        cola_aux.arrive(auxora)

    while cola_aux.size()>0:
        cola.arrive(cola_aux.atention())

def mostrarnotora():                               #muestra las notificaciones de la pila
    print(f"las notificaciones entre las 11:43 y las 15:57 fueron: {pilatime.size()}, a continuacion las notificaciones:")
    while pilatime.size() >0:
        aux = pilatime.pop()
        aplicacion = aux["aplicacion"]
        horas = aux["hora: "].strftime("%H:%M")
        mensaje = aux["mensaje: "]
        print(f"notificacion de la aplicacion {aplicacion} con el mensaje: {mensaje} a la hora: {horas}")

def barrido(limite):
    for i in range(limite):
        aux = cola.atention()
        aplicacion = aux["aplicacion"]
        horas = aux["hora: "].strftime("%H:%M")
        mensaje = aux["mensaje: "]
        print(f"notificacion de la aplicacion '{aplicacion}' con el mensaje: '{mensaje}' a la hora: {horas}")
        cola_aux.arrive(aux)
    
    while cola_aux.size()>0:
        cola.arrive(cola_aux.atention())
        
def menu():
    seguir = 'y'
    while seguir == 'y':
        lim = cola.size()
        print('-----------------------------------')
        print('para eliminar las notificaciones de facebook ingrese 1')
        print('para mostrar las notificaciones de twitter en la que se mencione Python ingrese 2')
        print('para mostrar las notificaciones entre las 11:43 y las 15:57 ingrese 3')
        print('para mostrar el listado de las notificaciones ingrese 4')
        print('para finalizar ingrese 5')
        res = input('ingrese su respuesta aqui: ')
        if res == '1':
            limpiar_consola()
            notiface(lim)
            print('se eliminaron las notificaciones de facebook')
        elif res == '2':
            limpiar_consola()
            twitter(lim)
        elif res == '3':
            limpiar_consola()
            ranghora(lim)
            mostrarnotora()
        elif res == '4':
            limpiar_consola()
            barrido(lim)
        elif res == '5':
            print('fin del programa')
            seguir = 'n'
        else:
            limpiar_consola()
            print('respuesta invalida')

limpiatodo()

for i in range (n):
    noti = {"hora: ": "", "aplicacion": "", "mensaje: ": ""}
    noti["hora: "] = input("ingrese la hora de la notificacion con el formato HH:MM : ")
    noti["mensaje: "] = input("ingrese el mensaje que emitio la aplicacion: ")
    noti["aplicacion"] = input("ingrese la aplicacion que la emitio: ")
    limpiar_consola()

    hora, minuto = map(int, noti["hora: "].split(':'))
    noti["hora: "] = time(hora, minuto, 00)

    cola.arrive(noti)

menu()




    






    