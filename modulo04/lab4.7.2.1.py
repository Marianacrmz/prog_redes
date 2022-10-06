'''
Descripción: PROYECTO: TIC-TAC-TOE
Autor: Mariana Canchola Ramírez
Fecha: 04 octubre 2022
'''


from random import randrange

def DisplayBoard(board):
# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.

	print("+-------" * 3,"+",sep="")
	for row in range(3):
		print("|       " * 3,"|",sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def EnterMove(board):
# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
	ok = False	
	while not ok:
		move = input("Ingresa tu movimiento en un rango del 1 - 9:") 
		ok = len(move) == 1 and move >= '1' and move <= '9' 
		if not ok:
			print("Repite tu turno") 
			continue
		move = int(move) - 1 
		row = move // 3 	
		column = move % 3		
		sign = board[row][column]
		ok = sign not in ['O','X'] 
		if not ok:	
			print("Esta fila está ocupada, ingresa otro número: ")
			continue
	board[row][column] = 'O' 	

def MakeListOfFreeFields(board):
# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
	free = []	
	for row in range(3):
		for column in range(3): 
			if board[row][column] not in ['O','X']: 
				free.append((row,column)) 
	return free


def VictoryFor(board,sgn):
# La función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

	if sgn == "X":
		who = 'computadora'	
	elif sgn == "O": 
		who = 'tú'	
	else:
		who = None	
	sim1 = sim2 = True 
	for rowcol in range(3):
		if board[rowcol][0] == sgn and board[rowcol][1] == sgn and board[rowcol][2] == sgn:	
			return who
		if board[0][rowcol] == sgn and board[1][rowcol] == sgn and board[2][rowcol] == sgn:
			return who
		if board[rowcol][rowcol] != sgn: 
			sim1 = False
		if board[2 - rowcol][2 - rowcol] != sgn: 
			sim2 = False
	if sim1 or sim2:
		return who
	return None

def DrawMove(board):
 # La función dibuja el movimiento de la máquina y actualiza el tablero.
	free = MakeListOfFreeFields(board) 
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt)
		row, column = free[this]
		board[row][column] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
board[1][1] = 'X'
free = MakeListOfFreeFields(board)
persona = True 
while len(free):
	DisplayBoard(board)
	if persona:
		EnterMove(board)
		victory = VictoryFor(board,'O')
	else:	
		DrawMove(board)
		victory = VictoryFor(board,'X')
	if victory != None:
		break
	persona = not persona	
	free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victory == 'tú':
	print("¡¡¡Ganaste!!!")
elif victory == 'yo':
	print("Perdiste :(")
else:
	print("Empate!")