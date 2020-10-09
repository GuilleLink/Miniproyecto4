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
it = 0
startBoard = np.matrix([[4,4,4,4,4,0],[4,4,4,4,4,0]])
#Code


#printBoard
#----------------------------------------
#MATRIX 2x6
# [[4,4,4,4,4,0],    PC
#  [4,4,4,4,4,0]]    User
#----------------------------------------
def printBoard(board):
    print('   ' + str(board.item(0)) + '  ' + str(board.item(1)) + '  ' + str(board.item(2)) + '  ' + str(board.item(3)) + '  ' + str(board.item(4)))
    print(str(board.item((0,5))) + '                 ' + str(board.item((1,5))))
    print('   ' + str(board.item((1,0))) + '  ' + str(board.item((1,1))) + '  ' + str(board.item((1,2))) + '  ' + str(board.item((1,3))) + '  ' + str(board.item((1,4))))
    print('    1  2  3  4  5  ')



while cont:
    print('**************JUEGO DE MANCALA**************')
    print('Ingrese una opcion:')
    print('1. Jugar Facil\n2. Jugar Normal\n3. Jugar Dificil\n4. Salir')
    opt = input()
    if(opt=='1'):
        it = 0
        printBoard(startBoard)

    elif(opt=='2'):
        it = 500
        printBoard(startBoard)

    elif(opt=='3'):
        it = 10000
        printBoard(startBoard)

    elif(opt=='4'):
        print('Gracias por jugar!')
        cont = False
    
    else:
        print('Su opcion no es valida, intente nuevamente')
