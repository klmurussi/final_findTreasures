import random as rand
import pygame as pg
from tools import Images, Sprites
from classes import Graph

listPOS = []


def nodes(graph):
    number = rand.randint(3, 7)
    #number = 7
    print(number)
    num = 1
    while (num != (number+1)):
        x = rand.randint(120, 700)
        y = rand.randint(127, 500)
        pos = (x, y)
        mark = False
        for k in listPOS:
            if abs(k[0] - x) < 50 and abs(k[1] - y) < 50:
                mark = True
        if mark == False:
            listPOS.append((x,y))
            graph.add_treasure(num, x, y)
            num = num + 1

    number = rand.randint(10, 15)
    #number = 39
    print(number)
    num2 = num + 1
    start = graph.add_node(0, 45, 80)
    end = graph.add_node(21, 710, 540)
    while True:
        x = 0
        y = 0
        for i in range(12):
            for j in range(16):
                exist = rand.randint(1, 10)
                if (exist == 1 and (x > 120 or y > 127)):
                    pos = (x, y)
                    mark = False
                    for k in listPOS:
                        if pos == k:
                            mark = True
                    if mark == False:
                        graph.add_node(num, x, y)
                        num2 = num2 + 1
                        listPOS.append((x, y))
                        if num2 == number+ 1 + num:
                            return ((start, end))
                x = x + 50
            x = 0
            y = y + 50
