from pila import Pila
# NO EJECUTAR ESTE CODIGO, tiene algun tipo de error, congela la pc

class misiones:
    def __init__(self, planeta, capturado, recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.recompensa = recompensa
    
    def __str__(self):
        return f'mision a {self.planeta} donde se capturo a {self.capturado} y se consigio {self.recompensa} de recompensa'
    
pila = Pila()
pilaux = Pila()

m1 = misiones('saturno','pepe',4500)
m2 = misiones('urano','el gallego',750)
m3 = misiones('la luna','han solo',6233)
m4 = misiones('el sol','fueguito',550)
m5 = misiones('venus','barbara',1800)

pila.push(m1)
pila.push(m2)
pila.push(m3)
pila.push(m4)
pila.push(m5)

# def barridopila():
#     while pila.size() > 0:
#         aux = pila.pop()
#         pilaux.push(aux)
#         print(aux)
    
#     while pilaux.size() > 0:
#         pila.push(pilaux.pop)

def recorrido():
    while pila.size()>0:
        aux = pila.pop()
        pilaux.push(aux)
        print(aux.planeta)

    while pilaux.size() > 0:
        pila.push(pilaux.pop)

def recaudado():
    total = 0
    while pila.size()>0:
        aux = pila.pop()
        pilaux.push(aux)
        total += aux.recompensa
    print(f'se recaudo en total {total} creditos galacticos')

    while pilaux.size() > 0:
        pila.push(pilaux.pop)

def hanso():
    mision = 0
    han = False
    while pila.size()>0:
        aux = pila.pop()
        mision += 1
        pilaux.push(aux)
        if aux.capturado == 'han solo':
            han = True
            break
    
    while pilaux.size() > 0:
        pila.push(pilaux.pop)

    if not han:
        print('en ninguna mision se capturo a han solo')
    else:
        print(f'han solo fue capturado en la mision numero {mision}, la cual fue en {aux.planeta}')

hanso()