#!/usr/bin/env python
import Tkinter
import Snake
import random

EMPTY = 0
SNAKE = 1
WALL = -1
FOOD = 2

class Board:

	def __init__(self, length, height, window):
		self.length = length
		self.height = height
		self.board = [EMPTY for i in range(length*height)]

		self.snake = Snake.Snake((random.randint(0,height-1),random.randint(0,length-1)))
		for (x,y) in self.snake.getBody():
			self.board[x*self.length+y] = SNAKE
		self.putFood()

		self.cellSize = 15
		self.canvas = Tkinter.Canvas(window, height=self.cellSize*(self.length+2), width=self.cellSize*(self.height+2), bg="grey")
		self.draw()

	def putFood(self):
		emptyCells = [(i/self.height,i%self.height) for i in range(self.length*self.height) if self.board[i] == EMPTY]
		if emptyCells:
			self.food = random.choice(emptyCells)
			self.board[self.food[0]*self.length+self.food[1]] = FOOD
		else:
			self.food = None

	def draw(self):
		self.canvas.delete("all")
		size = self.cellSize
		for i, cell in enumerate(self.board):
			coords = [size+size*(i/self.height), size+size*(i%self.height)]
			if cell == EMPTY:
				self.canvas.create_rectangle(coords[1], coords[0], coords[1]+size, coords[0]+size, outline="black", fill="grey")
			elif cell == FOOD:
				self.canvas.create_rectangle(coords[1], coords[0], coords[1]+size, coords[0]+size, outline="black",fill="green")
			else:
				self.canvas.create_rectangle(coords[1], coords[0], coords[1]+size, coords[0]+size, outline="black",fill="yellow")
		
		self.canvas.create_line(size, size, size, size*(self.length+1))
		self.canvas.create_line(size, size*(self.length+1), size*(self.height+1), size*(self.length+1))
		self.canvas.create_line(size*(self.height+1), size, size*(self.height+1), size*(self.length+1))
		self.canvas.create_line(size, size, size*(self.height+1), size)
		
		self.canvas.pack()

tk = Tkinter.Tk()
game = Board(25,30,tk)
tk.mainloop()

		

	