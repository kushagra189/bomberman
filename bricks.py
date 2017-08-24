from __future__ import print_function
import random

class Bricks:
	def makeBricks(self,array,Matrix):
		counter=0
		temp=0
		while(counter<21):
			x = random.randint(2,36)
			y = random.randint(4,76)
			if array[x][y]==0 and Matrix[x][y]==' ' and ((x%4==0 and y%8==4) or (x%4==2 and y%4==0)) :
			#     temp=0
			#     for i in range(x,x+2):
			#         for j in range(y,y+4):
			#             if Matrix[i][j]=='X' or array[i][j]==1 or Matrix[i][j]=='/':
			#                 temp=1
			#                 break
			#         if temp==1:
			#             break
			# if temp==1:
			#     continue
			# else:
				for i in range(x,x+2):
					for j in range(y,y+4):
						Matrix[i][j]='/'
				counter=counter+1
