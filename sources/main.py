import pygame as pg
import random as rand
import sys
from tools import Images, Settings, Sprites, CreateGraph, CreateEdges, CreateTreasures
from classes import Graph, InputBox
from math import inf

pg.init()
pg.mouse.set_visible(1)
pg.display.set_icon(Images.icon)
pg.display.set_caption(Settings.TITLE)
screen = pg.display.set_mode((Settings.windowSizeX, Settings.windowSizeY))
clock = pg.time.Clock()

pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)

graph = Graph.Graph()
(start, end) = CreateGraph.nodes(graph)
CreateTreasures.treasures(graph)

CreateEdges.edges(graph, start, end)
distance = graph.dijkstra_end(start, end)
while distance == inf:
    CreateEdges.edges(graph, start, end)
    distance = graph.dijkstra_end(start, end)

#print("distancia", distance)
qtd = graph.qtdTreasures()

input_box1 = InputBox.InputBox(0, 550, 140, 32)
input_boxes = [input_box1]
done = False
done1 = False
done2 = False

weight = str(rand.randint(30, 50))

while done == False:
    screen.fill(Settings.BLACK)
    screen.blit (Images.bau, (0, 0))
    text = "Bem vindo ao Run Away 2"
    textsurface = myfont.render(text, False, (255, 255, 255))
    posX = 370
    posY = 20
    screen.blit(textsurface, (posX, posY))
    text = "Agora você tem a chance de conseguir prêmios!"
    textsurface = myfont.render(text, False, (255, 255, 255))
    posX = 280
    posY = 70
    screen.blit(textsurface, (posX, posY))
    text = "Sua mala pesa: " + weight
    textsurface = myfont.render(text, False, (255, 255, 255))
    posX = 280
    posY = 90
    screen.blit(textsurface, (posX, posY))
    
    while done1 == False:
        text = "Confirmar"
        textsurface = myfont.render(text, False, (255, 255, 255))
        posX = 690
        posY = 560
        confirmar = pg.Rect(posX, posY, 150, 30)
        screen.blit(textsurface, (posX, posY))
        for i in graph.treasures:
            if i.print == True:
                pg.draw.circle(screen, Settings.BLUE, i.pos, 40)
        Sprites.treasure_list.draw(screen)
        graph.draw(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if confirmar.collidepoint(event.pos):
                    done1 = True
                for i in graph.treasures:
                    if i.button.collidepoint(event.pos):
                        if (i.print == True):
                            i.print = False
                        else:
                            i.print = True
        pg.display.update()

    while done2 == False:
        screen.fill(Settings.BLACK)
        Sprites.treasure_list.draw(screen)
        graph.premio(screen)
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONUP:
                    done = True

        pg.display.update()

while True:
    #RUN
    screen.fill(Settings.WHITE)
    x = 0
    y = 0

    for i in range(20):
        for j in range(27):
            if i == 0 and j == 0:
                screen.blit(Images.initial, (x, y))
            elif i > 17 and j > 23:
                screen.blit(Images.city, (x, y))
            elif i > 3 or j > 2:
                screen.blit(Images.tree, (x, y))
            x = x + 30
        x = 0
        y = y + 30

    for i in Sprites.line_list:
        if i[0][0] < i[1][0]:
            xMenor = i[0][0]
            xMaior = i[1][0]
        else:
            xMenor = i[1][0]
            xMaior = i[0][0]

        if i[0][1] < i[1][1]:
            yMenor = i[0][1]
            yMaior = i[1][1]
        else:
            yMenor = i[1][1]
            yMaior = i[0][1]

        pg.draw.line(screen, Settings.BLACK, i[0], i[1])
        text = str(i[2])
        textsurface = myfont.render(text, False, (0, 0, 0))
        posX = ((xMaior - xMenor)/2) + xMenor
        posY = ((yMaior - yMenor)/2) + yMenor
        screen.blit(textsurface, (posX, posY))

    Sprites.all_sprites_list.draw(screen)
    #graph.draw(screen, start, end)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        for box in input_boxes:
            box.handle_event(event, distance, screen)


    for box in input_boxes:
        box.update()

    #screen.fill((30, 30, 30))
    for box in input_boxes:
        box.draw(screen)

    pg.display.update()