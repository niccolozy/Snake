#!/usr/bin/env python

class Snake:

	def __init__(self,body):
		self.body = []
		for i in body:
			self.body.append(i)

	def moveTo(self,position,food=False):
		self.body.append(position)
		if not food:
			self.body.pop(0)

	def getHead(self):
		return self.body[-1]

	def getTail(self):
		return self.body[0]

	def getBody(self):
		return self.body