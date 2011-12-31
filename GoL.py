#coding=utf-8

from random import randint
import os
import platform
from time import sleep
cls = lambda :os.system("cls") if platform.system() == 'Windows' else os.system("clear")
ALIVE = 1
DEAD = 0

SIZE = 30 #表的长.
RANDOM = 50 #值越大初始细胞越多
DAILY = 0.5 #演化间隔时间

REALIVE = 3 #周围细胞数等于本数，该细胞复活
MAX = 4 #周围细胞数大于等于本数，该细胞死亡
MIN = 1 #周围细胞数小于等于本数，该细胞死亡

assert 8>=MAX>=REALIVE>=MIN>=0

#生成随机的存活细胞
table = [([(ALIVE if randint(0,100) <= RANDOM else DEAD) for x in xrange(SIZE)]) for x in xrange(SIZE)]

def next():
    for x in xrange(SIZE):
        for y in xrange(SIZE):
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
    for x in xrange(SIZE):
        for y in xrange(SIZE):
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
