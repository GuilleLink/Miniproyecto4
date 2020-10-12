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


def doMove(move, board, currentTurn):
    move = int(move)
    newBoard = np.copy(board)
    # print('\nTokkens in space ' +str(move+1) + ' are: ' + str(newBoard.item((1,move))))
    if currentTurn:
        nextTurn = False
        turn = 1

    if not currentTurn:
        nextTurn = True
        turn = 0

    moves =  newBoard.item((turn,move))
    newBoard.itemset((turn,move), 0)
    
    for movement in range(1, moves+1):
        if((movement + move) % 6 == 5):
            newBoard.itemset((turn, 5) , newBoard.item((turn, 5))+1)
            if (turn == 1):
                turn = 0
            else:
                turn = 1

        else:
            newBoard.itemset((turn,((move+movement) % 6)), newBoard.item((turn, ((move+movement) % 6))) + 1)
    
    if(move+moves==5 and currentTurn):
        nextTurn = True

    elif(move+moves==5 and not currentTurn):
        nextTurn = False

    return newBoard, nextTurn, checkEnd(newBoard), WhoWin(newBoard)

def checkEnd(board):
    if board.item((0, 5)) + board.item((1, 5)) == 40:
        return True
    else:
        return False

def WhoWin(board):
    if board.item((0, 5)) > board.item((1, 5)):
        return 0
    elif board.item((0, 5)) < board.item((1, 5)):
        return 1
    else:
        return -1

def calcular_movimiento(variables):
    calculos = {}

    for casilla, datos in variables.items():
        if datos['elegidos'] != 0:
            calculos[casilla] = datos['exitos'] / datos['elegidos']

    print(calculos)
    if len(calculos.values()) == 0:
        return random.choice(list(variables.keys()))

    max_value = max(list(calculos.values()))
    max_keys = [k for k, v in calculos.items() if v == max_value]

    return random.choice(max_keys)

def checkPossibleMoves(turn, board):
    if (sum(board[turn]) - (board.item((turn, 5))) == 0):
        return False
    else:
        return True

def start_simulation(iteraciones, board):
    variables = {
        0: {
            'exitos': 0,
            'elegidos': 0
        },
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
        }
    }

    for i in range(iteraciones):
        board_temp = np.copy(board)
        turno = False
        correct = False

        if checkPossibleMoves(0, board_temp):
            while not correct:
                eleccion_inicial = random.randint(0, 4)
                if board_temp.item((0, eleccion_inicial)) != 0:
                    correct = True
        else:
            eleccion_inicial = random.randint(0, 4)
        
        variables[eleccion_inicial]['elegidos'] += 1
        board_temp, turno, end, win = doMove(eleccion_inicial, board_temp, turno)

        while not end:
            correct = False

            if checkPossibleMoves(0, board_temp):
                while not correct:
                    eleccion = random.randint(0, 4)
                    if board_temp.item((0, eleccion)) != 0:
                        correct = True
            else:
                eleccion = random.randint(0, 4)

            board_temp, turno, end, win = doMove(eleccion, board_temp, turno)

        if win == 0:
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
        play = False
        printBoard(startBoard)
        actualboard = np.copy(startBoard)
        while not play:
            while nextTurn:
                if (checkPossibleMoves(nextTurn, actualboard) == False):
                    nextTurn = False
                else:
                    pass
                print('*********HUMAN TURN*********')
                move = input('Ingrese su movimiento (1-5): ')
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5'):
                    if(actualboard.item((1, int(move)-1)) != 0):
                        actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)   
                        printBoard(actualboard)
                    else:
                        print('NO PUEDE SELECCIONAR CASILLAS CON 0')
                else:
                    print('NO ES UN TIRO VALIDO')

            while not nextTurn:
                print('*********COMPUTER TURN*********')
                move = start_simulation(it, actualboard) + 1
                move = str(move)
                print('Movimiento de PC:', move)
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5'):
                    actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)
                    printBoard(actualboard)
                else:
                    print('NO ES UN TIRO VALIDO')
        if winner == 1:
            print('GANASTEEE :)')
        elif winner == 0:
            print('PERDISTE :(')
        else:
            print('EMPATARON :o')


    elif(opt=='2'):
        nextTurn = True
        it = 500
        play = False
        printBoard(startBoard)
        actualboard = np.copy(startBoard)
        while not play:
            while nextTurn:
                if (checkPossibleMoves(nextTurn, actualboard) == False):
                    nextTurn = False
                else:
                    pass
                print('*********HUMAN TURN*********')
                move = input('Ingrese su movimiento (1-5): ')
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5'):
                    if(actualboard.item((1, int(move)-1)) != 0):
                        actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)   
                        printBoard(actualboard)
                    else:
                        print('NO PUEDE SELECCIONAR CASILLAS CON 0')
                else:
                    print('NO ES UN TIRO VALIDO')

            while not nextTurn:
                print('*********COMPUTER TURN*********')
                move = start_simulation(it, actualboard) + 1
                move = str(move)
                print('Movimiento de PC:', move)
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5'):
                    actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)
                    printBoard(actualboard)
                else:
                    print('NO ES UN TIRO VALIDO')
        if winner == 1:
            print('GANASTEEE :)')
        elif winner == 0:
            print('PERDISTE :(')
        else:
            print('EMPATARON :o')

    elif(opt=='3'):
        nextTurn = True
        it = 10000
        play = False
        printBoard(startBoard)
        actualboard = np.copy(startBoard)
        while not play:
            while nextTurn:
                if (checkPossibleMoves(nextTurn, actualboard) == False):
                    nextTurn = False
                else:
                    pass
                print('*********HUMAN TURN*********')
                move = input('Ingrese su movimiento (1-5): ')                
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5'):
                    if(actualboard.item((1, int(move)-1)) != 0):
                        actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)   
                        printBoard(actualboard)
                    else:
                        print('NO PUEDE SELECCIONAR CASILLAS CON 0')
                else:
                    print('NO ES UN TIRO VALIDO')

            while not nextTurn:
                print('*********COMPUTER TURN*********')
                move = start_simulation(it, actualboard) + 1
                move = str(move)
                print('Movimiento de PC:', move)
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5'):
                    actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)
                    printBoard(actualboard)
                else:
                    print('NO ES UN TIRO VALIDO')
        if winner == 1:
            print('GANASTEEE :)')
        elif winner == 0:
            print('PERDISTE :(')
        else:
            print('EMPATARON :o')

    elif(opt=='4'):
        print('Gracias por jugar!')
        cont = False
    
    else:
        print('Su opcion no es valida, intente nuevamente')
