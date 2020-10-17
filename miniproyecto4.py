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
startBoard = np.matrix([[4,4,4,4,4,4,0],[4,4,4,4,4,4,0]])
#Code

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

#printBoard
#----------------------------------------
#MATRIX 2x7
# [[4,4,4,4,4,4,0],    PC
#  [4,4,4,4,4,4,0]]    User
#----------------------------------------
def printBoard(board):
    print('   ' + str(board.item((0,5))) + '  ' + str(board.item((0,4))) + '  ' + str(board.item((0,3))) + '  ' + str(board.item((0,2))) + '  ' + str(board.item((0,1))) + '  ' + str(board.item((0,0))))
    print(str(board.item((0,6))) + '                    ' + str(board.item((1,6))))
    print('   ' + str(board.item((1,0))) + '  ' + str(board.item((1,1))) + '  ' + str(board.item((1,2))) + '  ' + str(board.item((1,3))) + '  ' + str(board.item((1,4))) + '  ' + str(board.item((1,5))))
    print('   1  2  3  4  5  6  \n' + bcolors.ENDC)


def doMove(move, board, currentTurn):
    move = int(move)
    newBoard = np.copy(board)
    # print('\nTokkens in space ' +str(move+1) + ' are: ' + str(newBoard.item((1,move))))
    if currentTurn:
        nextTurn = False
        turn = 1
        actualturn = 1
        oponentTurn = 0

    if not currentTurn:
        nextTurn = True
        turn = 0
        actualturn = 0
        oponentTurn = 1

    moves =  newBoard.item((turn,move))
    newBoard.itemset((turn,move), 0)
    
    for movement in range(1, moves+1):
        if((movement + move) % 7 == 6):
            newBoard.itemset((turn, 6) , newBoard.item((turn, 6))+1)
            if (turn == 1):
                turn = 0
            else:
                turn = 1

        else:
            newBoard.itemset((turn,((move+movement) % 7)), newBoard.item((turn, ((move+movement) % 7))) + 1)
    
        #Condicion de robo
        if (movement == moves and turn == actualturn and newBoard.item((actualturn, ((move+movement) % 7))) == 1 and newBoard.item((actualturn, ((move+movement) % 7))) != newBoard.item((actualturn, 6)) and newBoard.item((oponentTurn, 6-(((move+movement)%7)+1))) != 0):
            #La casilla se queda 0 y se suma al banco de puntos
            newBoard.itemset((actualturn,((move+movement) % 7)), 0)
            #Le robo al opuesto
            if (actualturn == 0):
                stealingTurn = 1
            elif (actualturn == 1):
                stealingTurn = 0
            #Se le roba al otro
            stealPoints = newBoard.item((stealingTurn, 6-(((move+movement)%7)+1)))
            newBoard.itemset((stealingTurn, 6-(((move+movement)%7)+1)), 0)
            #Suma de puntos
            newBoard.itemset((actualturn, 6) , newBoard.item((actualturn, 6))+1+stealPoints)
        else:
            pass



    if(move+moves==6 and currentTurn):
        nextTurn = True

    elif(move+moves==6 and not currentTurn):
        nextTurn = False

    if currentTurn:
        if sum(newBoard[1][:6]) == 0:
            sumar_total = 0
            for i in range(len(newBoard[0]) - 1):
                sumar_total += newBoard.item((0, i))
                newBoard.itemset((0, i), 0)
            newBoard.itemset((1, 6), newBoard.item((1, 6)) + sumar_total)
            # print('TU TERMINASTE, ROBASTE:', sumar_total)
    else:
        if sum(newBoard[0][:6]) == 0:
            sumar_total = 0
            for i in range(len(newBoard[1]) - 1):
                sumar_total += newBoard.item((1, i))
                newBoard.itemset((1, i), 0)
            newBoard.itemset((0, 6), newBoard.item((0, 6)) + sumar_total)
            # print('CPU TERMINO, ROBO:', sumar_total)

    return newBoard, nextTurn, checkEnd(newBoard), WhoWin(newBoard)

def checkEnd(board):
    if board.item((0, 6)) + board.item((1, 6)) == 48:
        return True
    else:
        return False

def WhoWin(board):
    if board.item((0, 6)) > board.item((1, 6)):
        return 0
    elif board.item((0, 6)) < board.item((1, 6)):
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
    if (sum(board[turn]) - (board.item((turn, 6))) == 0):
        return False
    else:
        return True

def getPossibleMoves(turn, board):
    possible = []
    for i in range(len(board[turn]) - 1):
        if board.item((turn, i)) != 0:
            possible.append(i)

    return possible

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
        },
        5: {
            'exitos': 0,
            'elegidos': 0
        }
    }

    for i in range(iteraciones):
        board_temp = np.copy(board)
        turno = False

        possible_moves = getPossibleMoves(0, board_temp)
        eleccion_inicial = 0
        if possible_moves:
            eleccion_inicial = random.choice(possible_moves)

        variables[eleccion_inicial]['elegidos'] += 1
        board_temp, turno, end, win = doMove(eleccion_inicial, board_temp, turno)

        while not end:
            if turno:
                turno_num = 1
            else:
                turno_num = 0
            
            possible_moves = getPossibleMoves(turno_num, board_temp)
            eleccion = 0
            if possible_moves:
                eleccion = random.choice(possible_moves)

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
                if play:
                    break

                if (checkPossibleMoves(1, actualboard) == False):
                    nextTurn = False
                    break
                else:
                    pass

                print(bcolors.OKGREEN + '*********HUMAN TURN*********')
                move = input('Ingrese su movimiento (1-6): ')
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6'):
                    if(actualboard.item((1, int(move)-1)) != 0):
                        actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)   
                        printBoard(actualboard)
                    else:
                        print('NO PUEDE SELECCIONAR CASILLAS CON 0')
                else:
                    print('NO ES UN TIRO VALIDO')

            while not nextTurn:
                if play:
                    break

                print('*********COMPUTER TURN*********')
                move = start_simulation(it, actualboard) + 1
                move = str(move)
                print('Movimiento de PC:', move)
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6'):
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
                if play:
                    break

                if (checkPossibleMoves(1, actualboard) == False):
                    nextTurn = False
                    break
                else:
                    pass

                print(bcolors.OKGREEN + '*********HUMAN TURN*********')
                move = input('Ingrese su movimiento (1-6): ')
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6'):
                    if(actualboard.item((1, int(move)-1)) != 0):
                        actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)   
                        printBoard(actualboard)
                    else:
                        print('NO PUEDE SELECCIONAR CASILLAS CON 0')
                else:
                    print('NO ES UN TIRO VALIDO')

            while not nextTurn:
                if play:
                    break

                print('*********COMPUTER TURN*********')
                move = start_simulation(it, actualboard) + 1
                move = str(move)
                print('Movimiento de PC:', move)
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6'):
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
                if play:
                    break

                if (checkPossibleMoves(1, actualboard) == False):
                    nextTurn = False
                    break
                else:
                    pass

                print(bcolors.OKGREEN + '*********HUMAN TURN*********')
                move = input('Ingrese su movimiento (1-6): ')                
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6'):
                    if(actualboard.item((1, int(move)-1)) != 0):
                        actualboard, nextTurn, play, winner = doMove(int(move)-1, actualboard, nextTurn)   
                        printBoard(actualboard)
                    else:
                        print('NO PUEDE SELECCIONAR CASILLAS CON 0')
                else:
                    print('NO ES UN TIRO VALIDO')

            while not nextTurn:
                if play:
                    break
                
                print('*********COMPUTER TURN*********')
                move = start_simulation(it, actualboard) + 1
                move = str(move)
                print('Movimiento de PC:', move)
                if(move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6'):
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
