from tkinter import CENTER
import pygame
from const import *
from board import Board
from mover import Mover
from square import Square
from piece import *
from config import Config


class Game:
    def __init__(self):
        self.next_player = 'white'
        self.board = Board()
        self.mover = Mover()
        self.config = Config()

    def show_background(self, surface):
        theme = self.config.theme

        for row in range(ROWS):
            for col in range(COLS):
                color = theme.bg.light if (row+col) % 2 == 0 else theme.bg.dark
                rect = (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, color, rect)

                if col == 0:
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    label=self.config.font.render(str(ROWS-row),1,color)
                    label_pos=(5,5+row*SQ_SIZE)
                    surface.blit(label,label_pos)
                if row == 7:
                    color = theme.bg.dark if (row+col) % 2 == 0 else theme.bg.light
                    label=self.config.font.render(Square.get_alphacol(col),1,color)
                    label_pos=(col*SQ_SIZE+SQ_SIZE-20,HEIGHT-20)
                    surface.blit(label,label_pos)

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

    def show_moves(self, surface):
        theme = self.config.theme
        if self.mover.moving:
            piece = self.mover.piece

            for move in piece.moves:
                color = theme.moves.light if (
                    move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                rect = (move.final.col*SQ_SIZE, move.final.row *
                        SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                color = theme.trace.light if (
                    pos.row+pos.col) % 2 == 0 else theme.trace.dark
                rect = (pos.col*SQ_SIZE, pos.row*SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)

    def change_theme(self):
        self.config.change_theme()

    def sound_effect(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()
    def reset(self):
        self.__init__()

    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'
    def show_end(self,type,surface):
        color = '#000000'
        label=self.config.endFont.render(type,1,color)
        label_pos=(290,425)
        surface.blit(label,label_pos)
