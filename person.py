from __future__ import print_function
import random

class person:
	def checkRight(self,x,y,Matrix):
		for i in range(x,x+2):
			for j in range(y+4,y+8):
				if Matrix[i][j]=='X' or Matrix[i][j]=='/' or Matrix[i][j]=='O':
					return 0
				elif Matrix[i][j]=='E':
					return 2
				elif Matrix[i][j]=='B':
					return 3
		return 1

	def checkLeft(self,x,y,Matrix):
		for i in range(x,x+2):
			for j in range(y-4,y):
				if Matrix[i][j]=='X' or Matrix[i][j]=='/' or Matrix[i][j]=='E' or Matrix[i][j]=='O':
					return 0
		return 1

	def checkDown(self,x,y,Matrix):
		for i in range(x+2,x+4):
			for j in range(y,y+4):
				if Matrix[i][j]=='X' or Matrix[i][j]=='/' or Matrix[i][j]=='E' or Matrix[i][j]=='O':
					return 0
		return 1

	def checkUp(self,x,y,Matrix):
		for i in range(x-2,x):
			for j in range(y,y+4):
				if Matrix[i][j]=='X' or Matrix[i][j]=='/' or Matrix[i][j]=='E' or Matrix[i][j]=='O':
					return 0
		return 1

	def moveRight(self,x,y,array,Matrix):
		if  self.checkRight(x,y,Matrix):
			for i in range(x,x+2):
				for j in range(y,y+4):
					array[i][j]=0
					if Matrix[i][j]=='B':
						Matrix[i][j]=' '

			for i in range(x,x+2):
				for j in range(y+4,y+8):
					array[i][j]=1
			return 1
		else:
			return 0

	def moveLeft(self,x,y,array,Matrix):
		if  self.checkLeft(x,y,Matrix):
			for i in range(x,x+2):
				for j in range(y,y+4):
					array[i][j]=0
					if Matrix[i][j]=='B':
						Matrix[i][j]=' '

			for i in range(x,x+2):
				for j in range(y-4,y):
					array[i][j]=1
			return 1
		else:
			return 0

	def moveUp(self,x,y,array,Matrix):
		if  self.checkUp(x,y,Matrix):
			for i in range(x,x+2):
				for j in range(y,y+4):
					array[i][j]=0
					if Matrix[i][j]=='B':
						Matrix[i][j]=' '

			for i in range(x-2,x):
				for j in range(y,y+4):
					array[i][j]=1
			return 1
		else:
			return 0

	def moveDown(self,x,y,array,Matrix):
		if  self.checkDown(x,y,Matrix):
			#print(1)
			for i in range(x,x+2):
				for j in range(y,y+4):
					array[i][j]=0
					if Matrix[i][j]=='B':
						Matrix[i][j]=' '

			for i in range(x+2,x+4):
				for j in range(y,y+4):
					array[i][j]=1
			return 1
		else:
			return 0
