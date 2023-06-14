from lista import Lista
from cola import Cola

class personajes:
    def __init__(self, nombresuper, anio, nombreper=None, grupo=None):
        self.nombresuper = nombresuper
        self.nombreper = nombreper
        self.grupo = grupo
        self.anio = anio
    
    def __str__(self):
        if self.nombreper == None and self.grupo == None:
            return f'el superheroe {self.nombresuper} que aparecio en {self.anio}'
        elif self.nombreper == None:
            return f'el superheroe {self.nombresuper}, que pertenece a {self.grupo} aparecio en {self.anio}'
        elif self.grupo == None:
            return f'el superheroe {self.nombresuper}, llamado {self.nombreper}, aparecio en {self.anio}'
        else:
            return f'el superheroe {self.nombresuper}, llamado {self.nombreper}, que pertenece a {self.grupo} aparecio en {self.anio}'

lista = Lista()
cola = Cola()
colaux = Cola()
listaux = Lista()

p1 = personajes('carlosman', 1980,'carlos')        
p2 = personajes('hulk',1962,'bruce banner','marvel')
p3 = personajes('spiderman',1962,grupo='marvel')
p4 = personajes('capitan america',1941,'steve rogers','marvel')
p5 = personajes('wolverine',1974,'logan')
p6 = personajes('vlanck widow',1964,grupo='marvel')
p7 = personajes('doctor strange',1963)
p8 = personajes('superman',1938,'clark kent','DC')
p9 = personajes('batman',1939,'bruce wayne','DC')
p10 = personajes('flash',1956,grupo='DC')
p11 = personajes('wonder woman',1941,'diana prince')
p12 = personajes('star lord',1976,'peter quill','guardianes de la galaxia')
p13 = personajes('gamora',1975,grupo='guardianes de la galaxia')
p14 = personajes('groot',1960)
p15 = personajes('kick ass',2008)
p16 = personajes('joel',1988,grupo='cuatro fantasticos')

p17 = personajes('black cat', 1955,'jorgelina')
p18 = personajes('loki',1987)
p19 = personajes('hulk',1962,'bruce banner','marvel')
p20 = personajes('rocket raccon',1990)

listaux.insert(p17,'nombresuper')
listaux.insert(p18,'nombresuper')
listaux.insert(p19,'nombresuper')
listaux.insert(p20,'nombresuper')

lista.insert(p1,'nombresuper')
lista.insert(p2,'nombresuper')
lista.insert(p3,'nombresuper')
lista.insert(p4,'nombresuper')
lista.insert(p5,'nombresuper')
lista.insert(p6,'nombresuper')
lista.insert(p7,'nombresuper')
lista.insert(p8,'nombresuper')
lista.insert(p9,'nombresuper')
lista.insert(p10,'nombresuper')
lista.insert(p11,'nombresuper')
lista.insert(p12,'nombresuper')
lista.insert(p13,'nombresuper')
lista.insert(p14,'nombresuper')
lista.insert(p15,'nombresuper')
lista.insert(p16,'nombresuper')

def buscasuper(superh): #A     esta funcion sirve para buscar cualquier super, se podría buscar a la capitana marvel
    encontrado = lista.search(superh,'nombresuper')
    if encontrado is not None:
        print(f'se encontro a {lista.get_element_by_index(encontrado).nombresuper} en la posicion {encontrado}')
    else: print('no se encontro')

def guardaguardianes(): #B
    for i in range(lista.size()):
        if lista.get_element_by_index(i).grupo == 'guardianes de la galaxia':
            cola.arrive(lista.get_element_by_index(i))

def barridocola(): # barrido de cola para verificar 
    tamanio = cola.size()
    while cola.size() > 0:
        pers = cola.atention()
        print(pers)
        colaux.arrive(pers)

    print(f'suman un total de {tamanio} elementos en la cola') 
    while colaux.size() > 0:
        cola.arrive(colaux.atention())   

def descendente(): #C
    lista.order_by('nombresuper',True)
    for i in range(lista.size()):
        if lista.get_element_by_index(i).grupo == 'cuatro fantasticos' or lista.get_element_by_index(i).grupo == 'guardianes de la galaxia':
            print(lista.get_element_by_index(i))
    lista.order_by('nombresuper')

def los_60teros():#D
    for i in range(lista.size()):
        if lista.get_element_by_index(i).nombreper is not None and lista.get_element_by_index(i).anio > 1960:
            print(lista.get_element_by_index(i))

def blackw(): #E
    bpos = lista.search('vlanck widow','nombresuper')
    if bpos is not None:
        lista.get_element_by_index(bpos).nombresuper = 'black widow'

    lista.order_by('nombresuper')                                       #luego de corregir el nombre reordena 

def faltantes(): #F
    for i in range(listaux.size()):
        pers = listaux.get_element_by_index(i).nombresuper
        print(pers)
        buscado = lista.search(pers,'nombresuper')
        
        if buscado == None:
            lista.insert(listaux.get_element_by_index(i),'nombresuper')

def cps():  #G
    for i in range(lista.size()):
        inicial =lista.get_element_by_index(i).nombresuper[0]
        if inicial == 'c' or inicial == 'p' or inicial == 's':
            print(lista.get_element_by_index(i))


# a partir de aqui llame a las funciones necesarias para verificar
# realice una funcion para cada ejercicio porque se me hace mas comodo para hacer pruebas :)

# barridocola()

#buscasuper(')
#guardaguardianes()
#descendente()
#los_60teros
#blackw()
#faltantes()
#cps()
