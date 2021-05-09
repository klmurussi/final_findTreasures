import pygame
from tools import Sprites, Images

class Treasure(pygame.sprite.Sprite):
	def __init__(self, num, x, y):
		super().__init__()
		self.image = Images.treasure
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.num = num
		Sprites.node_list.add(self)
		Sprites.all_sprites_list.add(self)