import random

tematica_comida=["SANDWHICH","SOPA","PASTA","HAMBURGUESA", "ENSALDA", "TACOS", "PIZZA","SUSHI","JUGO", "MOFONGO", "MANGU"]
tematica_entretenimiento = ["NETFLIX", "HBO", "DISNEY", "PIXAR", "MARVEL", "DC", "PARAMOUNT", "LIONSGATE", "MGM", "SONY"]
tematica_tecnologia = ["APPLE", "MICROSOFT", "GOOGLE", "AMAZON", "FACEBOOK", "TWITTER", "IBM", "INTEL", "TESLA", "SPACEX"]
abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
coordenadas_ocupadas=[]
palabras_encontradas = []

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
            
def jugar():
    while True:
        entrada = input("Introduce las coordenadas o 'EXIT' para salir: ")
        if entrada.upper() == "EXIT":
            break
        else:
            coordenadas = entrada.split(",")
            x = int(coordenadas[0]) - 1
            y = int(coordenadas[1]) - 1
            for palabra in palabras:
                if sopa[x][y] == palabra[0] and [x, y] in coordenadas_ocupadas:
                    print("¡Has encontrado la palabra " + palabra + "!")
                    palabras_encontradas.append(palabra)
                    if set(palabras_encontradas) == set(palabras):
                        print("¡Felicidades! Has encontrado todas las palabras.")
                        break


palabras=[]
elegir_palabras(tematica_comida,4,10, palabras)
#print(palabras)
sopa=[]
rellenar_sopa(sopa,8)
esconder_palabras(sopa,8,palabras)
imprimirmatriz(sopa,8,2)

jugar ()