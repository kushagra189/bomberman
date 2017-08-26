class WallStructure:

    def makeWall(self, Matrix):
        for i in range(2):
            for j in range(84):
                Matrix[i][j] = 'X'

        for i in range(40, 42):
            for j in range(84):
                Matrix[i][j] = 'X'

        for i in range(2, 40):
            for j in range(4):
                Matrix[i][j] = 'X'

        for i in range(2, 40):
            if i % 4 == 2 or i % 4 == 3:
                pass
            else:
                for j in range(4, 80):
                    if j % 8 == 0 or j % 8 == 1 or j % 8 == 2 or j % 8 == 3:
                        Matrix[i][j] = 'X'
                    else:
                        pass

        for i in range(2, 40):
            for j in range(80, 84):
                Matrix[i][j] = 'X'
        return Matrix


class position:

    def checker(self, i, j, array):
        if(array[i][j] == 1):
            return 1
        else:
            return 0
