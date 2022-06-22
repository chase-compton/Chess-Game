import pygame
from const import *
from board import Board
from mover import Mover
from square import Square
from piece import *


class Game:
    def __init__(self):
        self.board = Board()
        self.mover=Mover()

    def show_background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                rect = (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    if piece is not self.mover.piece:
                        piece.set_image(size=80)
                        img = pygame.image.load(piece.image)
                        img_center = col*SQ_SIZE+SQ_SIZE//2, row*SQ_SIZE+SQ_SIZE//2
                        piece.image_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.image_rect)
