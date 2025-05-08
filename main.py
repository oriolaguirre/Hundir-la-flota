import utils

barcos = []
barcosMaquina = []
tablero1 =utils.CrearTablero()
tablero2 =utils.CrearTablero()
contador = 0 
turno = True

tablero1,tablero2 =utils.generarPartida(barcos,barcosMaquina,tablero1,tablero2,contador)

while True:

    seguir = utils.partida(tablero1,tablero2)

    if seguir.lower() == "no":
        print("Game over")
        break

    turno = utils.controladorTurnos(turno,tablero1,tablero2)
    fin_partida = utils.RevisionEstadoPartida(tablero1,tablero2)


    if fin_partida == False:
        print("Game over")
        break
    