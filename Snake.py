#!/usr/bin/env python

class Snake:

	def __init__(self,head):
		self.body = []
		self.body.append(head)
		self.direction = 'Up'

	def moveTo(self,position,food=False):
		self.body.append(position)
		if self.body[-1][0] == self.body[-2][0]:
			self.direction = 'Left' if self.body[-1][1] == self.body[-2][1] -1 else 'Right'
		if self.body[-1][1] == self.body[-2][1]:
			self.direction = 'Up' if self.body[-1][0] == self.body[-2][0] -1 else 'Down'
		if not food:
			self.body.pop(0)
		print(self.direction)

	def getHead(self):
		return self.body[-1]

	def getTail(self):
		return self.body[0]

	def getBody(self):
		return self.body