import random

tematica_comida=["SANDWHICH","SOPA","PASTA","HAMBURGUESA", "ENSALDA", "TACOS", "PIZZA","SUSHI","JUGO", "MOFONGO", "MANGU"]
tematica_marcas=["MICROSOFT","APPEL","GOOGLE","SAMSUNG", "ANDROID", "OPENAI", "META","CISCO","AMAZON", "BLUEOCEAN", "INTEL"]
tematica_entretenimiento=["MARVEL","DISNEY","NETFLIX","NINTENDO", "FACEBOOK", "INSTAGRAM", "ACTIVISION","BLIZZARD","OVERWATCH", "WARNER", "FOX"]
abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
coordenadas_ocupadas=[]
coordenada_principal = [] # Variable para guardar las coordenadas de las letras principales

def elegir_palabras(tematica, cantidad, tamano, palabras_elegidas):
    contador=0
    while contador<cantidad:
        indice=random.randint(0,tamano-1)
        if (tematica[indice] not in palabras_elegidas):
            contador+=1
            palabras_elegidas.append(str(tematica[indice]))

def rellenar_sopa(Matriz, tamano):
    lista_temporal=[]
    for i in range(0, tamano):
        for j in range(0,tamano):
            indice = random.randint(0, 25)
            lista_temporal.append(abecedario[indice])
        Matriz.append(list(lista_temporal))
        lista_temporal.clear()

def imprimirmatriz(M1, tamano, longitudmaxima):
    j=0
    print("  1  2  3  4  5  6  7  8")
    for fila in M1:
        j+=1
        print(str(j), end="")
        for i in range(0,tamano):
            print(str(fila[i]).rjust(longitudmaxima), end=" ")
        print()

def esconder_palabras(sopa, tamano, palabras):
    for palabra in palabras:
        x=random.randint(1,tamano-1)
        y=random.randint(1,tamano-1)
        while([x,y] in coordenadas_ocupadas):
            x=random.randint(1,tamano-1)
            y=random.randint(1,tamano-1)
        coordenadas_ocupadas.append([x,y])
        sopa[x][y]=palabra[0]
        print("La palabra "+palabra+" está en "+str(x+1)+", "+str(y+1))
        coordenada_principal.append([x+1,y+1]) # Añade la coordenada de la primera letra a la variable
        for i in range(1, len(palabra)):
            coordenadas_temp=elegir_direccion(x, y)
            while(coordenadas_temp[0]==-1 or coordenadas_temp[1]==-1 or (coordenadas_temp in coordenadas_ocupadas)):
                coordenadas_temp=elegir_direccion(x, y)
            coordenadas_ocupadas.append(coordenadas_temp)
            print("La letra "+palabra[i]+" está en ")
            print(coordenadas_temp)
            x=coordenadas_temp[0]
            y=coordenadas_temp[1]
            sopa[x][y]=palabra[i]

def elegir_direccion(fila,columna):
    #1:Arriba
    #2:Abajo
    #3:Derecha
    #4:Izquierda
    #5:Diagonal arriba derecha
    #6:Diagonal arriba izquierda
    #7:Diagonal abajo derecha
    #8:Diagonal abajo izquierda
    direccion=random.randint(1,8)
    if(direccion==1 and (fila-1)>=0):
        return [fila-1,columna]
    elif(direccion==2 and (fila+1)<8):
        return [fila+1,columna]
    elif(direccion==3 and (columna+1)<8):
        return [fila,columna+1]
    elif(direccion==4 and (columna-1)>=0):
        return [fila,columna-1]
    elif(direccion==5 and (columna+1)<8 and (fila-1)>=0):
        return [fila-1,columna+1]
    elif(direccion==6 and (columna-1)>=0 and (fila-1)>=0):
        return [fila-1,columna-1]
    elif(direccion==7 and (columna+1)<8 and (fila+1)<8):
        return [fila+1,columna+1]
    elif(direccion==8 and (columna-1)>=0 and (fila+1)<8):
        return [fila+1,columna-1]
    else:
        return [-1,-1]

palabras=[]
elegir_palabras(tematica_comida,4,10, palabras)
#print(palabras)
sopa=[]
rellenar_sopa(sopa,8)
esconder_palabras(sopa,8,palabras)
imprimirmatriz(sopa,8,2)

# Pide al usuario que ingrese la coordenada de la letra principal de una palabra
intentos = 3 # Número de intentos permitidos
ganador = False # Variable para indicar si el usuario ganó o no
while intentos > 0 and not ganador:
    coordenada = input("Ingrese la coordenada de la letra principal de una palabra: ") # Ejemplo: 3,4
    coordenada = list(map(int, coordenada.split(","))) # Convierte el input en una lista de dos números enteros
    for i in range(len(coordenada_principal)): # Recorre la lista de coordenadas principales
        if coordenada == coordenada_principal[i]: # Si hay una coincidencia
            print("¡Felicidades! Has encontrado la palabra " + palabras[i]) # Felicita al usuario y muestra la palabra
            ganador = True # Cambia la variable a True para terminar el juego
            break # Sale del bucle for
    if not ganador: # Si no hay una coincidencia
        intentos -= 1 # Reduce el número de intentos en uno
        print("Lo siento, esa no es la coordenada correcta. Te quedan " + str(intentos) + " intentos.") # Informa al usuario y muestra los intentos restantes

if not ganador: # Si se acaban los intentos y el usuario no ganó
    print("Has perdido el juego. Las palabras eran: " + ", ".join(palabras)) # Muestra un mensaje de derrota y las palabras ocultas

