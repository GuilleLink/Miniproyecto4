#Universidad del Valle de Guatemala
#Modelacion y simulacion
#Miniproyecto4
#Hector Javier Carpio - 17077
#Juan Guillermo Sandoval - 17577

#Imports
import numpy as np
import random

#Variables
cont = True
startBoard = np.matrix([[4,4,4,4,4,0],[4,4,4,4,4,0]])
#Code


#printBoard
#----------------------------------------
#MATRIX 2x6
# [[4,4,4,4,4,0],    PC
#  [4,4,4,4,4,0]]    User
#----------------------------------------
def printBoard(board):
    print('   ' + str(board.item((0,4))) + '  ' + str(board.item((0,3))) + '  ' + str(board.item((0,2))) + '  ' + str(board.item((0,1))) + '  ' + str(board.item((0,0))))
    print(str(board.item((0,5))) + '                 ' + str(board.item((1,5))))
    print('   ' + str(board.item((1,0))) + '  ' + str(board.item((1,1))) + '  ' + str(board.item((1,2))) + '  ' + str(board.item((1,3))) + '  ' + str(board.item((1,4))))
    print('   1  2  3  4  5  \n')


def doMove(move, board):
    newBoard = board
    print('\nTokkens in space ' +str(move+1) + ' are: ' + str(board.item((1,move))))
    moves =  board.item((1,move))
    board.itemset((1,move), 0)
    turn = 1
    nextTurn = False
    for movement in range(1, moves+1):
        if(movement + move > 5):
            if (turn == 0):
                turn = 1
            else:
                turn = 0
            
        board.itemset((turn,((move+movement) % 6)), board.item((turn, ((move+movement) % 6))) + 1)
    
    if(move+movement==5):
        nextTurn = True

    return newBoard, nextTurn

def do_move(board, pos, jugador):
    return board, random.randint(0, 1), random.randint(0, 1)

def calcular_movimiento(variables):
    calculos = {}

    for casilla, datos in variables.items():
        if datos['exitos'] != 0:
            calculos[casilla] = datos['elegidos'] / datos['exitos']

    if len(calculos.values()) == 0:
        return random.choice(list(variables.keys()))

    max_value = max(list(calculos.values()))
    max_keys = [k for k, v in calculos.items() if v == max_value]

    return random.choice(max_keys)

def start_simulation(iteraciones, board):
    board_temp = np.copy(board)

    variables = {
        1: {
            'exitos': 0,
            'elegidos': 0
        },
        2: {
            'exitos': 0,
            'elegidos': 0
        },
        3: {
            'exitos': 0,
            'elegidos': 0
        },
        4: {
            'exitos': 0,
            'elegidos': 0
        },
        5: {
            'exitos': 0,
            'elegidos': 0
        }
    }

    for i in range(iteraciones):
        eleccion_inicial = random.randint(1, 5)
        
        variables[eleccion_inicial]['elegidos'] += 1
        turno = 0
        board_temp, end, win = do_move(board_temp, eleccion_inicial, turno)

        while not end:
            turno = (turno + 1) % 2
            eleccion = random.randint(1, 5)

            board_temp, end, win = do_move(board_temp, eleccion, turno)

        if win:
            variables[eleccion_inicial]['exitos'] += 1

    return calcular_movimiento(variables)        


while cont:
    print('**************JUEGO DE MANCALA**************')
    print('Ingrese una opcion:')
    print('1. Jugar Facil\n2. Jugar Normal\n3. Jugar Dificil\n4. Salir')
    opt = input()
    if(opt=='1'):
        nextTurn = True
        it = 0
        play = True
        printBoard(startBoard)
        actualboard = startBoard
        while play:
            while nextTurn:
                move = input('Ingrese su movimiento (1-5)')
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5'):
                    actualboard, nextTurn = doMove(int(move)-1, actualboard)   
                    printBoard(actualboard)

    elif(opt=='2'):
        it = 500
        printBoard(startBoard)
        move = start_simulation(it, startBoard)

    elif(opt=='3'):
        it = 10000
        printBoard(startBoard)
        move = start_simulation(it, startBoard)

    elif(opt=='4'):
        print('Gracias por jugar!')
        cont = False
    
    else:
        print('Su opcion no es valida, intente nuevamente')
