import random as rand
import pygame as pg
from tools import Images, Sprites
from classes import Graph

listPOS = []


def nodes(graph):
    number = rand.randint(10, 15)
    #number = 39
    print(number)
    num = 1
    start = graph.add_node(0, 45, 80)
    end = graph.add_node(21, 710, 540)
    while True:
        x = rand.randint(120, 700)
        y = rand.randint(127, 500)
        pos = (x, y)
        mark = False
        for k in listPOS:
            if abs(k[0] - x) < 70 and abs(k[1] - y) < 70:
                mark = True
        if mark == False:
            graph.add_node(num, x, y)
            num = num + 1
            listPOS.append((x, y))
            if num == number+ 1:
                return ((start, end))
