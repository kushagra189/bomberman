from __future__ import print_function
import signal
import copy
import sys
import time
import os
from random import randint
from walls import *
from person import *
from bomberman import *
from bomb import *
from bricks import *
from board import *
from enemy import *
from alarmexception import *
from getchunix import *
from time import time
getch = GetchUnix()

BoardArray = [[' ' for x in range(84)] for y in range(42)]
CheckArray = [[0 for x in range(84)] for y in range(42)]
pointer = []


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    #    print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

intialX = 2
initialY = 4
bombPosition = [0 for i in range(4)]
Board = WallStructure()
b = Board.makeWall(BoardArray)
enemies = Enemy()
enemies.generateEnemy(BoardArray, pointer)
caller = bomberman()
BOMB = Bomb()
caller.makeBomber(intialX, initialY, CheckArray)
obs = Bricks()
obs.makeBricks(CheckArray, BoardArray)
printer = BoardMaker()
print("Game Controls")
print("w -> move up")
print("s -> move down")
print("a -> move left")
print("d -> move right")
print("b -> plant bomb")
print("press 'q' to quit!")
print()
printer.printMatrix(BoardArray, CheckArray)
p = bomberman()
save = time()
life = 3

while True:
    curr = time()
    if (curr - save) >= 1:
        enemies.move(pointer, BoardArray)
        save = curr
    move = input_to()
    if move == 's':
        if p.moveDown(intialX, initialY, CheckArray, BoardArray) == 1:
            intialX = intialX + 2

    elif move == 'w':
        if p.moveUp(intialX, initialY, CheckArray, BoardArray) == 1:
            intialX = intialX - 2

    elif move == 'd':
        if p.moveRight(intialX, initialY, CheckArray, BoardArray) == 1:
            initialY = initialY + 4

    elif move == 'a':
        if p.moveLeft(intialX, initialY, CheckArray, BoardArray) == 1:
            initialY = initialY - 4

    elif move == 'b' and bombPosition[2] == 0:
        bombPosition[0] = intialX
        bombPosition[1] = initialY
        bombPosition[2] = 4
        BOMB.makeBomb(bombPosition[0], bombPosition[1], BoardArray)
        # os.system("tput reset")

    elif move == 'q':
        break

    if bombPosition[0] != 0:
        # enemies.destroy(bombPosition,pointer,BoardArray)
        if p.destroySelf(bombPosition, BoardArray, CheckArray):
            life = life - 1
            initialY = 4
            intialX = 2
        BOMB.bombExplode(bombPosition, BoardArray, pointer)

    if enemies.destroyBomber(pointer, CheckArray, BoardArray):
        life = life - 1
        initialY = 4
        intialX = 2

    os.system("tput reset")
    print("Game Controls")
    print("w -> move up")
    print("s -> move down")
    print("a -> move left")
    print("d -> move right")
    print("b -> plant bomb")
    print("press 'q' to quit!")
    print()
    printer.printMatrix(BoardArray, CheckArray)
    BOMB.patternRemover(BoardArray, bombPosition[0], bombPosition[1])
    print("Lives " + str(life))
    print("Score " + str(bombPosition[3]))

    if(len(pointer) == 0):
        print("You win")
        break

    if life == 0:
        print("you Lose")
        break
