#coding=utf-8

from random import randint
import os
import platform
from time import sleep

if platform.system() == 'Windows':
    def cls():
        os.system("cls")
else:
    def cls():
        os.system("clear")

SIZE = 30 #表的边长.
RANDOM = 10 #值越大初始细胞越多
DAILY = 0.5 #演化间隔时间

REALIVE = 3 #周围细胞数等于本数，该细胞复活
MAX = 4 #周围细胞数大于等于本数，该细胞死亡
MIN = 1 #周围细胞数小于等于本数，该细胞死亡


ALIVE = 1
DEAD = 0

table = []
#创建细胞表
for x in range(SIZE):
    row = []
    for y in range(SIZE):
        row.append(DEAD)
    table.append(row)
#生成随机的存活细胞
for x in range(SIZE):
    for y in range(SIZE):
        table[x][y] = ALIVE if randint(0,100) <= RANDOM else DEAD

def next():
    for x in range(SIZE):
        for y in range(SIZE):
            cell = table[x][y]
            livenum = 0
            livenum += table[(x + 1) % SIZE][(y - 1) % SIZE]
            livenum += table[(x + 1) % SIZE][y]
            livenum += table[(x + 1) % SIZE][(y + 1) % SIZE]
            livenum += table[x][(y - 1) % SIZE]
            livenum += table[x][(y + 1) % SIZE]
            livenum += table[(x - 1) % SIZE][(y - 1) % SIZE]
            livenum += table[(x - 1) % SIZE][y]
            livenum += table[(x - 1) % SIZE][(y + 1) % SIZE]

            if cell is ALIVE:
                if livenum <= MIN or livenum >= MAX:
                    table[x][y] = DEAD
            elif livenum == REALIVE:
                table[x][y] = ALIVE

def show():
    result = ''
    for x in range(SIZE):
        for y in range(SIZE):
            result += 'O ' if table[x][y] is ALIVE else '  '
        result += '\n'
    print result

while True:
    cls()
    show()
    next()
    sleep(DAILY)
