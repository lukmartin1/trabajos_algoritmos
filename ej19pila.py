from pila import Pila

pila = Pila()
estreno_2014 = [] #lista donde se guardarán los nombres de las peliculas estrenadas en 2014
contpelis_2018 = 0 #suma de las peliculas estrenadas en 2018
marvel = Pila() # esta pila guarda los diccionarios completos de las peliculas de marvel del 2016

for i in range(5): #solo modificando el range() se puede modificar la cantidad de peliculas a cargar, no altera el resto del codigo
    peliculas = {}
    peliculas['nombre'] = input('ingrese el nombre de la pelicula ')
    peliculas['estudio'] = input('ingrese el estudio que hizo la pelicula ')
    peliculas['anio'] = input('ingrese el anio que se lanzo la pelicula ')
    pila.push(peliculas)
    
while pila.size()> 0:
    aux = pila.pop()
    if aux['anio'] == '2014':
        estreno_2014.append(aux['nombre'])
    elif aux['anio'] == '2018':
        contpelis_2018 += 1
    elif (aux['anio'] == '2016' and aux['estudio'] == 'marvel'):
        marvel.push(aux)

print()
print('las peliculas estrenadas en 2014 son: ')
print(estreno_2014)
print('el total de peliculas estrenadas en 2018 es de: ',contpelis_2018)

if marvel.size()>0: # elegí una pila para las peliculas de marvel por si se quisiera mostrar toda la informacion de sus peliculas
    print('las peliculas de marvel estrenadas en 2016 fueron:')
    while marvel.size() > 0:
        auxiliar = marvel.pop()
        print(auxiliar['nombre'])
else:
    print('no se registraron peliculas de marvel estrenadas en el año 2016')

