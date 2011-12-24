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
RANDOM = 20 #值越大初始细胞越多
DAILY = 0.5 #演化间隔时间

REALIVE = 3 #周围细胞数等于本数，该细胞复活
MAX = 4 #周围细胞数大于等于本数，该细胞死亡
MIN = 1 #周围细胞数小于等于本数，该细胞死亡


ALIVE = 1
DEAD = 0

#生成随机的存活细胞
table = [([(ALIVE if randint(0,100) <= RANDOM else DEAD) for x in range(SIZE)]) for x in range(SIZE)]
    
def next():
    for x in range(SIZE):
        for y in range(SIZE):
            cell = table[x][y]
            livenum = -cell
            for m in (x+1,x,x-1):
                for n in (y-1,y,y+1):
                    livenum += table[m % SIZE][n % SIZE]

            if cell is ALIVE and (livenum <= MIN or livenum >= MAX):
                table[x][y] = DEAD
            elif livenum == REALIVE:
                table[x][y] = ALIVE

def show():
    for x in range(SIZE):
        for y in range(SIZE):
            if table[x][y] is ALIVE:
                print 'O',
            else:
                print ' ',
        print ''

while True:
    cls()
    show()
    next()
    sleep(DAILY)
