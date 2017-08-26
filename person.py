from __future__ import print_function
import random


class person:

    def checkR(self, x, y, Matrix):
        for i in range(x, x + 2):
            for j in range(y + 4, y + 8):
                temp = Matrix[i][j]
                if temp == 'X' or temp == '/' or temp == 'O':
                    return 0
                elif temp == 'E':
                    return 2
                elif temp == 'B':
                    return 3
        return 1

    def checkL(self, x, y, Matrix):
        for i in range(x, x + 2):
            for j in range(y - 4, y):
                temp = Matrix[i][j]
                if temp == 'X' or temp == '/' or temp == 'E' or temp == 'O':
                    return 0
        return 1

    def checkD(self, x, y, Matrix):
        for i in range(x + 2, x + 4):
            for j in range(y, y + 4):
                temp = Matrix[i][j]
                if temp == 'X' or temp == '/' or temp == 'E' or temp == 'O':
                    return 0
        return 1

    def checkU(self, x, y, Matrix):
        for i in range(x - 2, x):
            for j in range(y, y + 4):
                temp = Matrix[i][j]
                if temp == 'X' or temp == '/' or temp == 'E' or temp == 'O':
                    return 0
        return 1

    def moveRight(self, x, y, array, Matrix):
        if self.checkR(x, y, Matrix):
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    array[i][j] = 0
                    if Matrix[i][j] == 'B':
                        Matrix[i][j] = ' '

            for i in range(x, x + 2):
                for j in range(y + 4, y + 8):
                    array[i][j] = 1
            return 1
        else:
            return 0

    def moveLeft(self, x, y, array, Matrix):
        if self.checkL(x, y, Matrix):
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    array[i][j] = 0
                    if Matrix[i][j] == 'B':
                        Matrix[i][j] = ' '

            for i in range(x, x + 2):
                for j in range(y - 4, y):
                    array[i][j] = 1
            return 1
        else:
            return 0

    def moveUp(self, x, y, array, Matrix):
        if self.checkU(x, y, Matrix):
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    array[i][j] = 0
                    if Matrix[i][j] == 'B':
                        Matrix[i][j] = ' '

            for i in range(x - 2, x):
                for j in range(y, y + 4):
                    array[i][j] = 1
            return 1
        else:
            return 0

    def moveDown(self, x, y, array, Matrix):
        if self.checkD(x, y, Matrix):
            # print(1)
            for i in range(x, x + 2):
                for j in range(y, y + 4):
                    array[i][j] = 0
                    if Matrix[i][j] == 'B':
                        Matrix[i][j] = ' '

            for i in range(x + 2, x + 4):
                for j in range(y, y + 4):
                    array[i][j] = 1
            return 1
        else:
            return 0
