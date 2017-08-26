from __future__ import print_function
import random
from person import *


class Enemy(person):

    def makeEnemy(self, x, y, Matrix, array):
        flag = 0
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                temp = Matrix[i][j]
                if temp == 'X' and temp == '/' and temp == 'E' and temp == 'B':
                    flag = 1
                    break
                else:
                    pass
                if flag == 1:
                    break
                else:
                    pass

        if flag == 1:
            x = random.randint(1, 20) * 2
            y = random.randint(1, 20) * 4
            makeEnemy(x, y, Matrix, array)
        else:
            array.append([x, y])
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    Matrix[i][j] = 'E'

    def generateEnemy(self, Matrix, array):
        count = 0
        while count < 4:
            eX = random.randint(2, 38)
            eY = random.randint(4, 76)
            if (eX % 4 == 0 and eY % 8 == 4) or (eX % 4 == 2 and eY % 4 == 0):
                # print("yeaaaaaaaaaaaaaaaaaaa")
                self.makeEnemy(eX, eY, Matrix, array)
                count = count + 1
            else:
                pass

    def moveRight(self, array, Matrix):
        x = array[0]
        y = array[1]
        if self.checkR(x, y, Matrix) == 1 or self.checkR(x, y, Matrix) == 3:
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    # array[i][j]=0
                    Matrix[i][j] = ' '

            for i in range(x, x + 2):
                for j in range(y + 4, y + 8):
                    Matrix[i][j] = 'E'
            array[1] = array[1] + 4
            return 1
        else:
            return 0

    def moveLeft(self, array, Matrix):
        x = array[0]
        y = array[1]
        if self.checkL(x, y, Matrix) == 1 or self.checkR(x, y, Matrix) == 3:
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    Matrix[i][j] = ' '

            for i in range(x, x + 2):
                for j in range(y - 4, y):
                    Matrix[i][j] = 'E'
            array[1] = array[1] - 4
            return 1
        else:
            return 0

    def moveUp(self, array, Matrix):
        x = array[0]
        y = array[1]
        if self.checkU(x, y, Matrix) == 1 or self.checkR(x, y, Matrix) == 3:
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    Matrix[i][j] = ' '

            for i in range(x - 2, x):
                for j in range(y, y + 4):
                    Matrix[i][j] = 'E'
            array[0] = array[0] - 2
            return 1
        else:
            return 0

    def moveDown(self, array, Matrix):
        x = array[0]
        y = array[1]
        if self.checkD(x, y, Matrix) == 1 or self.checkR(x, y, Matrix) == 3:
            # print(1)
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    # array[i][j]=0
                    Matrix[i][j] = ' '

            for i in range(x + 2, x + 4):
                for j in range(y, y + 4):
                    Matrix[i][j] = 'E'
            array[0] = array[0] + 2
            return 1
        else:
            return 0

    def move(self, array, Matrix):
        p = len(array)
        for i in range(p):
            while True:
                mover = random.randint(1, 4)
                if mover == 1:
                    if self.moveRight(array[i], Matrix) == 1:
                        break

                elif mover == 2:
                    if self.moveLeft(array[i], Matrix) == 1:
                        break

                elif mover == 3:
                    if self.moveUp(array[i], Matrix) == 1:
                        break

                elif mover == 4:
                    if self.moveDown(array[i], Matrix) == 1:
                        break

    def destroyBomber(self, array, array1, Matrix):
        p = len(array)
        for i in range(p):
            x = array[i][0]
            y = array[i][1]
            if array1[x][y] == 1:
                for i in range(2):
                    for j in range(4):
                        array1[i + 2][j + 4] = 1
                        array1[x + i][y + j] = 0
                        Matrix[x + i][y + j] = ' '
                return 1
        return 0
