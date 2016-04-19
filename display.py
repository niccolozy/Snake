#!/usr/bin/env python
import Tkinter
import Snake
import random

EMPTY = 0
SNAKE = 1
WALL = -1
FOOD = 2

class Board:

	def __init__(self, height, length, window):
		self.length = length
		self.height = height
		self.board = [EMPTY for i in range(length*height)]

		self.snake = Snake.Snake((random.randint(0,height-1),random.randint(0,length-1)))
		self.putSnake()
		self.putFood()

		self.cellSize = 15
		self.canvas = Tkinter.Canvas(window, height=self.cellSize*(self.height+2), width=self.cellSize*(self.length+2), bg="grey")
		self.draw()

	def putFood(self):
		emptyCells = [(i/self.length,i%self.length) for i in range(self.length*self.height) if self.board[i] == EMPTY]
		if emptyCells:
			self.food = random.choice(emptyCells)
			self.board[self.food[0]*self.length+self.food[1]] = FOOD
		else:
			self.food = None

	def putSnake(self):
		for i, cell in enumerate(self.board):
			if cell == SNAKE:
				self.board[i] = EMPTY 
		for (x,y) in self.snake.getBody():
			self.board[x*self.length+y] = SNAKE

	def draw(self):
		self.canvas.delete("snake","food")
		size = self.cellSize
		for i, cell in enumerate(self.board):
			coords = [size+size*(i/self.length), size+size*(i%self.length)]
			if cell == FOOD:
				self.canvas.create_rectangle(coords[1], coords[0], coords[1]+size, coords[0]+size, outline="grey",fill="green", tags="food")
			elif cell == SNAKE:
				self.canvas.create_rectangle(coords[1], coords[0], coords[1]+size, coords[0]+size, outline="black",fill="black",tags="snake")
		
		self.canvas.create_line(size, size, size*(self.length+1), size)
		self.canvas.create_line(size*(self.length+1), size, size*(self.length+1), size*(self.height+1))
		self.canvas.create_line(size, size*(self.height+1), size*(self.length+1), size*(self.height+1))
		self.canvas.create_line(size, size, size, size*(self.height+1))
		
		self.canvas.pack()

	def keyMove(self,event):
		if event.keysym == 'Up' and self.snake.direction != "Down":
			self.snake.direction = event.keysym
		elif event.keysym == 'Down' and self.snake.direction != "Up":
			self.snake.direction = event.keysym
		elif event.keysym == 'Left' and self.snake.direction != "Right":
			self.snake.direction = event.keysym
		elif event.keysym == 'Right' and self.snake.direction != "Left":
			self.snake.direction = event.keysym
		else:
			return False
		
	def autoMove(self):
		if self.snake.direction == 'Up':
			nextPoint = (self.snake.getHead()[0]-1,self.snake.getHead()[1])
		elif self.snake.direction == 'Down':
			nextPoint = (self.snake.getHead()[0]+1,self.snake.getHead()[1])
		elif self.snake.direction == 'Left':
			nextPoint = (self.snake.getHead()[0],self.snake.getHead()[1]-1)
		elif self.snake.direction == 'Right':
			nextPoint = (self.snake.getHead()[0],self.snake.getHead()[1]+1)
		self.move(nextPoint)
		self.canvas.after(100,self.autoMove)

	def move(self,nextPoint):
		if 0 <= nextPoint[0] < self.height and 0 <= nextPoint[1] < self.length:
			if self.board[nextPoint[0]*self.length + nextPoint[1]] == FOOD:
				self.snake.moveTo(nextPoint,True)
				self.putFood()
			else:
				self.snake.moveTo(nextPoint)

		self.putSnake()
		self.draw()

tk = Tkinter.Tk()
game = Board(20,30,tk)
tk.bind_all('<Key>', game.keyMove)
tk.after(100,game.autoMove)
tk.mainloop()

		

	