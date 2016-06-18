import Snake
import random


def isValide(point,size,previous=None):
	if 0 <= point < size*size:
		if previous:
			if (((previous+1)%size == 0 and point == previous+1) or
				(previous%size == 0 and point == previous-1)):
				return False
		return True
	else:
		return False

def isSnake(point,snake_body):
	return True if point in snake_body else False

def putDistance(snake,food,size):
	board =[99]*size*size 
	board[food] = 0
	surrounding = [-1,-size,1,size]
	found = False
	to_check = []
	checked = []
	to_check.append(food)

	while to_check:
		point = to_check.pop(0)

		for delta in surrounding:
			next_point = point + delta
			if next_point in to_check:
				continue
			if next_point == snake.getHead():
				found = True
			if isValide(next_point, size, point):
				if board[next_point] > board[point] + 1:
					board[next_point] = board[point] + 1
				if next_point not in checked:
					to_check.append(next_point)
		checked.append(point)
		#print(point)
		#printBoard(board,size)
	return found, board

def printBoard(board,size):
	for i in range(0,size):
		format_str = ('{:>5}'*size).format(*board[i*size:(i+1)*size])
		print(format_str)
	print('\n')

def moveToFood(board,snake,size):
	surrounding = [-1,-size,1,size]
	dis = 99999
	choice = None
	for delta in surrounding:
		point = snake.getHead() + delta
		if isValide(point,size,snake.getHead()) and not isSnake(point, snake.getBody()):
			if board[point] == -1:
				continue
			if board[point] < dis:
				choice = point
				dis = board[point]
	return choice


if __name__ == '__main__':
	size = 8
	food = random.choice(range(1,size*size))
	snake = Snake.Snake([0])
	found, board = putDistance(snake,food,size)
	printBoard(board,size)
	
	while snake.getHead() != food:
		choice = moveToFood(board,snake,size)
		snake.moveTo(choice)
		for part in snake.getBody():
			board[part] = -1
		
	printBoard(board,size)




