import pygame
from tools import Sprites, Images

class Treasure(pygame.sprite.Sprite):
	def __init__(self, num, x, y, peso, premio):
		super().__init__()
		self.image = Images.treasure
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.pos = (x+10, y+20)
		self.num = num
		self.peso = peso
		self.premio = premio
		self.button = pygame.Rect(x, y, 50, 50)
		self.print = False
		Sprites.treasure_list.add(self)
		#Sprites.node_list.add(self)
		#Sprites.all_sprites_list.add(self)