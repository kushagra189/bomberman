from __future__ import print_function
from person import *
import random


class bomberman(person):

    def makeBomber(self, x, y, array):
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                array[i][j] = 1

    def destroySelf(self, array, Matrix, array1):
        x = array[0]
        y = array[1]
        # if array1[x][y]==1 and array[2]==1:
        # 	for i in range(2):
        # 		for j in range(4):
        # 			array1[i+2][j+4]=1
        # 			array1[x+i][y+j]=0
        # 			Matrix[x+i][y+j]=' '
        # 	return 1

        if array1[x + 2][y] == 1 and array[2] == 1:
            for i in range(2):
                for j in range(4):
                    array1[i + 2][j + 4] = 1
                    array1[x + 2 + i][y + j] = 0
                    Matrix[x + 2 + i][y + j] = ' '
            return 1

        elif array1[x - 2][y] == 1 and array[2] == 1:
            for i in range(2):
                for j in range(4):
                    array1[i + 2][j + 4] = 1
                    array1[x - 2 + i][y + j] = 0
                    Matrix[x - 2 + i][y + j] = ' '
            return 1

        elif array1[x][y + 4] == 1 and array[2] == 1:
            for i in range(2):
                for j in range(4):
                    array1[i + 2][j + 4] = 1
                    array1[x + i][y + 4 + j] = 0
                    Matrix[x + i][y + 4 + j] = ' '
            return 1

        elif array1[x][y - 4] == 1 and array[2] == 1:
            for i in range(2):
                for j in range(4):
                    array1[i + 2][j + 4] = 1
                    array1[x + i][y - 4 + j] = 0
                    Matrix[x + i][y - 4 + j] = ' '
            return 1

        else:
            return 0
