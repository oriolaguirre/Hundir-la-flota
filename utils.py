import numpy as np,random,Clases,time

def CrearTablero():#Esta función genera los tableros
   tablero = np.full((10,10),"_")
   return tablero
  
def controlColisiones(coordenadas,listaCoordenadasBarcos):#funcion incompleta

   
    if np.any([np.array_equal(barco, coord) for barco in coordenadas for coord in listaCoordenadasBarcos]):
        return True
    else:
        if coordenadas not in listaCoordenadasBarcos:
            listaCoordenadasBarcos.append(coordenadas)
        return listaCoordenadasBarcos

def generarPartida(barcos,barcosMaquina,tablero1,tablero2,contador):#funcion que va generando turnos entre el usuario y la maquina para ir posicionando los barcos
    while contador <2:

        barco = Clases.Barcos(list(input("Primera posicioncoordenadas?-->")),input("direccion?-->"),int(input("longitud?-->")))
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

def ColocarBarcos(barcos,tablero): #Funcion que coloca los barcos en funcin del punto inicial, direccion y longitud
    
    for barco in barcos: 
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

def disparo(tablero,coordenadasDisparo1,coordenadasDisparo2): #funcion que cambia los caracteres del tablero en funcion del acierto o no en los disparos
    
    if tablero[coordenadasDisparo1,coordenadasDisparo2] == "o":
        tablero[coordenadasDisparo1,coordenadasDisparo2] = "x"
        acierto = True

    elif tablero[coordenadasDisparo1,coordenadasDisparo2] == "_":
        tablero[coordenadasDisparo1,coordenadasDisparo2] = "#"    
        acierto = False
    else:
        acierto = False
    return tablero ,acierto   
        
def controladorTurnos(turno,tablero1,tablero2):#funcion que controla los turnos, tambienen funcion del acierto o no de los jugadores

    if turno == True:
        print("***-----------------***")
        print("Turno del jugador")
        print("***-----------------***")
    else:
        print("***-----------------***")
        print("Turno de la maquina") 
        print("***-----------------***")

    if turno == True:
        try:
            coordenadas_disparo1 = int(input("mete la fila-->"))
            coordenadas_disparo2 = int(input("mete la columna-->"))
        except:
            print("mete una coordenada valida")    

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

def RevisionEstadoPartida(tablero1,tablero2):#funcion que evalua si alguien ha derribado todos los barcos o no

    tablero1 = np.where(tablero1 == 'o', 0, -1)
    tablero2 = np.where(tablero2 == 'o', 0, -1)
    tiene_cero = np.any(tablero1 == 0) and np.any(tablero2 == 0)    

    if np.any(tablero2 == 0) == False:
        print("Ha ganado el usuario")

    elif np.any(tablero1 == 0) == False:
        print("ha ganado la maquina")    
    return tiene_cero

def partida(tablero1,tablero2):#funcionde iteracion entre el usuario y la termninal

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

