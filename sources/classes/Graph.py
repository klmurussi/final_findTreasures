from classes import Node, Connection, Treasure
import random
from tools import Sprites
from pythonds import PriorityQueue
from math import inf
import pygame as pg 

pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)

class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = {}
        self.qtd = 0
        self.treasures = {}
        #self.buttons = {}

    def add_node(self, num, x, y):
        empty_node = Node.Node(num, x, y)
        self.graph[empty_node] = []
        return empty_node

    def add_treasure(self, num, x, y, peso, premio):
        empty_node = Treasure.Treasure(num, x, y, peso, premio)
        self.treasures[empty_node] = []
        self.qtd = self.qtd + 1
        return empty_node

    def add_edge(self, src, dest, weight):
        if (dest in self.graph[src]):
            return
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        self.weights[(src.num, dest.num)] = weight
        self.weights[(dest.num, src.num)] = weight
        edge = Connection.Connection(
            (src.rect.x+16, src.rect.y+16), (dest.rect.x+16, dest.rect.y+16), weight)

    def dijkstra_end(self, start, end):
        distance = {node: inf for node in self.graph}
        visited = {node: False for node in self.graph}
        pq = PriorityQueue()
        distance[start] = 0
        pq.add((0, start))
        for next_node in self.graph[start]:
            initial_weight = self.weights[(start.num, next_node.num)]
            pq.add((initial_weight, next_node))
        while not pq.isEmpty():
            currentVert = pq.delMin()
            visited[currentVert] = True
            if (visited[end]):
                break
            for nextVert in self.graph[currentVert]:
                newDist = distance[currentVert] \
                    + self.weights[(currentVert.num, nextVert.num)]
                if newDist < distance[nextVert]:
                    distance[nextVert] = newDist
                    pq.decreaseKey(nextVert, newDist)
                    pq.add((newDist, nextVert))
        return distance[end]

    def draw (self, screen):
        for i in self.treasures:
            text = str(i.peso)
            textsurface = myfont.render(text, False, (255,255,255))
            posX = i.rect.x - 20
            posY = i.rect.y + 15
            screen.blit(textsurface, (posX, posY))

    def premio (self, screen):
        for i in self.treasures:
            text = str(i.premio)
            textsurface = myfont.render(text, False, (255,255,255))
            posX = i.rect.x - 20
            posY = i.rect.y + 15
            screen.blit(textsurface, (posX, posY))

    def buttons (self, pos, screen, color):
        for i in self.treasures:
            if i.button.collidepoint(pos):
                pg.draw.cicle(screen, color, pos, 20)

    def qtdTreasures (self):
        return self.qtd
