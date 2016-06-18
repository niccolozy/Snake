#!/usr/bin/env python
import Tkinter
import snake
import random
import ai as AI

EMPTY = 99
SNAKE = -1
FOOD = 0

class Board:

	def __init__(self, height, length, window):
		self.length = length
		self.height = height

		self.snake = snake.Snake([random.randint(0,length*height)])
		#self.putSnake()
		self.putFood()
		self.found, self.board = AI.putDistance(self.snake, self.food, self.length) 

		self.cellSize = 20
		self.canvas = Tkinter.Canvas(window, height=self.cellSize*(self.height+2), width=self.cellSize*(self.length+2), bg="grey")
		self.draw()

	def putFood(self):
		emptyCells = [i for i in range(self.length*self.height) if i not in self.snake.getBody()]
		if emptyCells:
			self.food = random.choice(emptyCells)
		else:
			self.food = None

	def putSnake(self):
		for i, cell in enumerate(self.board):
			if cell == SNAKE:
				self.board[i] = EMPTY 
		for x in self.snake.getBody():
			self.board[x] = SNAKE

	def draw(self):
		self.canvas.delete("snake","food","empty")
		size = self.cellSize
		for i, cell in enumerate(self.board):
			coords = [size+size*(i/self.length), size+size*(i%self.length)]
			if i is self.food:
				self.canvas.create_rectangle(coords[1], coords[0], coords[1]+size, coords[0]+size, outline="grey",fill="green", tags="food")
			elif i in self.snake.getBody():
				self.canvas.create_rectangle(coords[1]+1, coords[0]+1, coords[1]+size-1, coords[0]+size-1, outline="black",fill="black",tags="snake")
			else:
				self.canvas.create_text(coords[1]+1, coords[0]+1, width=size, text=str(cell),tags="empty")
		
		self.canvas.create_line(size, size, size*(self.length+1), size)
		self.canvas.create_line(size*(self.length+1), size, size*(self.length+1), size*(self.height+1))
		self.canvas.create_line(size, size*(self.height+1), size*(self.length+1), size*(self.height+1))
		self.canvas.create_line(size, size, size, size*(self.height+1))
		self.canvas.pack()

	def keyMove(self,event):
		if event.keysym == 'Up':
			self.move(self.snake.getHead()-self.length)
		elif event.keysym == 'Down':
			self.move(self.snake.getHead()+self.length)
		elif event.keysym == 'Left':
			self.move(self.snake.getHead()-1)
		elif event.keysym == 'Right':
			self.move(self.snake.getHead()+1)
		else:
			return False

	def move(self,nextPoint):
		if 0 <= nextPoint < self.height*self.length:
			if nextPoint is self.food:
				self.snake.moveTo(nextPoint,True)
				self.putFood()
				#self.putSnake()
				self.found, self.board = AI.putDistance(self.snake,self.food,self.length)
				self.draw()
			elif nextPoint not in self.snake.getBody():
				self.snake.moveTo(nextPoint)
				#self.putSnake()
				self.draw()
		

		
	def consult(self):
		print('start')
		if self.found:
			choice = AI.moveToFood(self.board,self.snake,self.length)
			self.move(choice)
			print(choice)
		print('end')
		tk.after(60,game.consult)

tk = Tkinter.Tk()
game = Board(10,10,tk)
tk.bind_all('<Key>', game.keyMove)
tk.after(500,game.consult)
tk.mainloop()

		

	