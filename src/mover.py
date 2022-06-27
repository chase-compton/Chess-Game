import pygame
from const import *


class Mover:
    def __init__(self):
        self.piece = None
        self.moving = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_col = 0
        self.initial_row = 0

    def update_blit(self, surface):
        self.piece.set_image(size=128)
        image = self.piece.image
        img = pygame.image.load(image)
        img_center = (self.mouseX, self.mouseY)
        self.piece.image_rect = img.get_rect(center=img_center)
        surface.blit(img,self.piece.image_rect)

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initial_row = pos[1]//SQ_SIZE
        self.initial_col = pos[0]//SQ_SIZE

    def move_piece(self, piece):
        self.piece = piece
        self.moving = True

    def stop_move(self):
        self.piece = None
        self.moving = False
