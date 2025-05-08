import numpy as np,random,Clases,time

def CrearTablero():
   tablero = np.full((10,10),"_")
   return tablero
  
def controlColisiones(coordenadas,listaCoordenadasBarcos):

   
    if np.any([np.array_equal(barco, coord) for barco in coordenadas for coord in listaCoordenadasBarcos]):
        return True
    else:
        if coordenadas not in listaCoordenadasBarcos:
            listaCoordenadasBarcos.append(coordenadas)
        return listaCoordenadasBarcos

def generarPartida(barcos,barcosMaquina,tablero1,tablero2,contador):
    while contador <2:

        barco = Clases.Barcos(list(input("Primera posicioncoordenadas?")),input("direccion?"),int(input("longitud?")))
        coordenada1 = random.randint(0,9)
        coordenada2 = random.randint(0,9)
        direccionesListaMaquina = ["arriba","abajo","izquierda","derecha"]
        direccionMaquina = random.choice(direccionesListaMaquina)
        longitudMaquina = random.randint(1,4)

        barcoMaquina = Clases.Barcos(list((coordenada1,coordenada2)),direccionMaquina,int(longitudMaquina))
        
        barcosMaquina.append(barcoMaquina)
        barcos.append(barco)

        tablero1 = ColocarBarcos(barcos,tablero1)
        tablero2 = ColocarBarcos(barcosMaquina,tablero2)
        contador +=1
    return(tablero1,tablero2)

def ColocarBarcos(barcos,tablero): #pasarle lista de barcos, para recorrer todos los barcos
    
    for barco in barcos: # igual meto en otra funcion esta funcionalidad
        i,j = barco.posicion
        i = int(i)
        j = int(j)
        tablero[i,j] = "o"

    posicioni = i
    posicionj = j   

    lista_coordenada_barco = []
  

    if barco.direccion == "abajo":

        for i in range(posicioni,posicioni + barco.longitud):

            nueva_coordenada = [i,j]
            
            #lista_coordenada_barco = controlColisiones(nueva_coordenada,lista_coordenada_barco) 
            #print(lista_coordenada_barco)

            if lista_coordenada_barco == True:
                break
                
            try:
                tablero[i,j] = "o"
            except:
                print("fuera de rango")
                break   


    elif barco.direccion == "arriba": 
        for i in range(posicioni ,(posicioni - barco.longitud),-1):
            try: 
                #aqui abriaque acer un apend de cada posicion i,j que recorre  a longitud_lista_barco, y llamar a a funcion controlarcolisiones
                tablero[i,j] = "o"
            except:
                print("fuera de rango")
                break    

    elif barco.direccion == "derecha":

        for j in range(posicionj , posicionj + barco.longitud):
            try:
             tablero[i,j] = "o"
            except:
                print("fuera de rango")
                break   


    elif barco.direccion == "izquierda": #pendiente

        for j in range(posicionj,(posicionj - barco.longitud),-1):
            try:
                tablero[i,j] = "o"
            except:
                print("fuera de rango")  
                break 
    else:
        print("La direccion", barco.longitud ,"que has introducido, es erronea") 
        tablero[i,j] = "_"    
    return tablero

def disparo(tablero,coordenadasDisparo1,coordenadasDisparo2):
    
    if tablero[coordenadasDisparo1,coordenadasDisparo2] == "o":
        tablero[coordenadasDisparo1,coordenadasDisparo2] = "x"
        acierto = True

    elif tablero[coordenadasDisparo1,coordenadasDisparo2] == "_":
        tablero[coordenadasDisparo1,coordenadasDisparo2] = "#"    
        acierto = False
    else:
        acierto = False
    return tablero ,acierto   
        
def controladorTurnos(turno,tablero1,tablero2):

    if turno == True:
        print("***-----------------***")
        print("Turno del jugador")
        print("***-----------------***")
    else:
        print("***-----------------***")
        print("Turno de la maquina") 
        print("***-----------------***")

    if turno == True:
        coordenadas_disparo1 = int(input("mete la fila"))
        coordenadas_disparo2 = int(input("mete la columna"))

        tablero2,turno = disparo(tablero2,coordenadas_disparo1,coordenadas_disparo2)
          
        
    else:
        
        coordenadas_disparo1_maquina = random.randint(0,9)
        coordenadas_disparo2_maquina = random.randint(0,9)

        tablero1,acierto = disparo(tablero1,coordenadas_disparo1_maquina,coordenadas_disparo2_maquina)
    
        if acierto == True:
             turno = False
        else:
             turno = True
    return turno         

def RevisionEstadoPartida(tablero1,tablero2):

    tablero1 = np.where(tablero1 == 'o', 0, -1)
    tablero2 = np.where(tablero2 == 'o', 0, -1)
    tiene_cero = np.any(tablero1 == 0) and np.any(tablero2 == 0)    

    if np.any(tablero2 == 0) == False:
        print("Ha ganado el usuario")
    else:
        print("ha ganado la maquina")    
    return tiene_cero

def partida(tablero1,tablero2):

    print("***-----------------***")
    print("tablero de la maquina")
    print("***-----------------***")
    print(tablero2)
    time.sleep(3)
    print("***-----------------***")
    print("tablero del jugador")
    print("***-----------------***")
    print(tablero1)
    try:
        seguir = input("Desea seguir?-->")
    except:
        print("Mete un valor correcto, si o no para proceder con el juego")    
    return seguir

"""

arreglar prints

"""