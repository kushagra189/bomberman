from __future__ import print_function
from termcolor import colored


class BoardMaker:

    def printMatrix(self, Matrix, array):
        # print("Start Game")
        for i in range(42):
            for j in range(84):
                temp = Matrix[i][j]
                if(array[i][j] == 1 and temp == ' '):
                    temp = 'B'
                if temp == 'B':
                    print(colored(temp, 'blue'), end='')
                elif temp == '/':
                    print(colored(temp, 'yellow'), end='')
                elif temp == 'E':
                    print(colored(temp, 'red'), end='')
                elif temp == 'e':
                    print(colored(temp, 'cyan'), end='')
                elif(temp == 'O' or temp == '1' or temp == '2' or temp == '3'):
                    print(colored(temp, 'magenta'), end='')
                else:
                    print(temp, end='')
            print()
