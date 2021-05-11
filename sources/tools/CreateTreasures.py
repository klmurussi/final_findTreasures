import random as rand
import pygame as pg
from tools import Images, Sprites
from classes import Graph

listPOS = []


def treasures(graph):
    number = rand.randint(5, 10)
    #number = 7
    print(number)
    num = 1
    while (num != (number+1)):
        x = rand.randint(50, 700)
        y = rand.randint(200, 500)
        pos = (x, y)
        mark = False
        for k in listPOS:
            if abs(k[0] - x) < 70 and abs(k[1] - y) < 70:
                mark = True
        if mark == False:
            listPOS.append((x,y))
            graph.add_treasure(num, x, y, rand.randint(10, 20), rand.randint(50, 100))
            num = num + 1