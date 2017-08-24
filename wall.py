from __future__ import print_function
import random
from termcolor import colored

class WallStructure:
	def makeWall(self,Matrix):
		for i in range(2):
			for j in range(84):
				Matrix[i][j]='X'

		for i in range(40,42):
			for j in range(84):
				Matrix[i][j]='X'

		for i in range(2,40):
			for j in range(4):
				Matrix[i][j]='X'

		for i in range(2,40):
			if i%4==2 or i%4==3:
				pass
			else:
				for j in range(4,80):
					if j%8==0 or j%8==1 or j%8==2 or j%8==3:
						Matrix[i][j]='X'
					else:
						pass

		for i in range(2,40):
			for j in range(80,84):
				Matrix[i][j]='X'
		return Matrix

	def printMatrix(self,Matrix,array):
		#print("Start Game")
		for i in range(42):
			for j in range(84):
				if(array[i][j]==1 and Matrix[i][j]==' '):
					Matrix[i][j]='B'
				if Matrix[i][j]=='B':
					print(colored(Matrix[i][j],'blue'),end='')
				elif Matrix[i][j]=='/':
					print(colored(Matrix[i][j],'grey'),end='')
				elif Matrix[i][j]=='E':
					print(colored(Matrix[i][j],'red'),end='')
				elif(Matrix[i][j]=='O' or Matrix[i][j]=='1' or Matrix[i][j]=='2' or Matrix[i][j]=='3'):
					print(colored(Matrix[i][j],'magenta'),end='')
				else:
					print(Matrix[i][j],end='')
			print()

class position:
	def checker(self,i,j,array):
		if(array[i][j]==1):
			return 1
		else:
			return 0