import pygame
from tools import Sprites


class Connection(pygame.sprite.Sprite):
    def __init__(self, src, dest, weight):
        super().__init__()
        Sprites.line_list.append((src, dest, weight))