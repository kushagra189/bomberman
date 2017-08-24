class Bomb:
	def makeBomb(self,x,y,Matrix):
		for i in range(x,x+2):
			for j in range(y,y+4):
				Matrix[i][j]='O'

	def bombExplode(self,array,Matrix,array1):
		x=array[0]
		y=array[1]
		fl=0
		fl1=0
		if array[2]>1:
			for i in range(x,x+2):
				for j in range(y,y+4):
					Matrix[i][j]=chr(47+array[2])
			array[2]=array[2]-1
		elif array[2]==1:
			#print("ok")
			for i in range(x,x+2):
				for j in range(y,y+4):
					Matrix[i][j]=' '

			for i in range(x,x+2):
				for j in range(y-4,y):
					if Matrix[i][j]=='/':
						fl1=1
						Matrix[i][j]=' '
					elif Matrix[i][j]=='E':
						Matrix[i][j]=' '
						fl=1
			if fl==1:
				array[3]=array[3]+100
				array1.remove([x,y-4])
				fl=0

			if fl1==1:
				array[3]=array[3]+20
				fl1=0

			for i in range(x,x+2):
				for j in range(y+4,y+8):
					if Matrix[i][j]=='/':
						fl1=1
						Matrix[i][j]=' '
					elif Matrix[i][j]=='E':
						Matrix[i][j]=' '
						fl=1

			if fl==1:
				array[3]=array[3]+100
				array1.remove([x,y+4])
				fl=0

			if fl1==1:
				array[3]=array[3]+20
				fl1=0

			for i in range(x-2,x):
				for j in range(y,y+4):
					if Matrix[i][j]=='/':
						fl1=1
						Matrix[i][j]=' '
					elif Matrix[i][j]=='E':
						Matrix[i][j]=' '
						fl=1

			if fl==1:
				array[3]=array[3]+100
				array1.remove([x-2,y])
				fl=0

			if fl1==1:
				array[3]=array[3]+20
				fl1=0

			for i in range(x+2,x+4):
				for j in range(y,y+4):
					if Matrix[i][j]=='/':
						fl1=1
						Matrix[i][j]=' '
					elif Matrix[i][j]=='E':
						Matrix[i][j]=' '
						fl=1

			if fl==1:
				array[3]=array[3]+100
				array1.remove([x+2,y])
				fl=0

			if fl1==1:
				array[3]=array[3]+20
				fl1=0

			array[2]=array[2]-1
