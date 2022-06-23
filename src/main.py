import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess Game')
        self.game = Game()

    def mainloop(self):
        game = self.game
        screen = self.screen
        mover = self.game.mover
        board = self.game.board

        while True:
            game.show_background(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if mover.moving:
                mover.update_blit(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mover.update_mouse(event.pos)
                    clicked_row = mover.mouseY//SQ_SIZE
                    clicked_col = mover.mouseX//SQ_SIZE
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col)
                            mover.save_initial(event.pos)
                            mover.move_piece(piece)
                            game.show_background(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                elif event.type == pygame.MOUSEMOTION:
                    if mover.moving:
                        mover.update_mouse(event.pos)
                        game.show_background(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        mover.update_blit(screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if mover.moving:
                        mover.update_mouse(event.pos)
                        released_row = mover.mouseY//SQ_SIZE
                        released_col = mover.mouseX//SQ_SIZE

                        initial = Square(mover.initial_row, mover.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(mover.piece, move):
                            captured=board.squares[released_row][released_col].has_piece()
                            board.move(mover.piece, move)
                            game.sound_effect(captured)
                            game.show_background(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            game.next_turn()

                    mover.stop_move()
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_t:
                        game.change_theme()
                    if event.key==pygame.K_r:
                        game.reset()
                        game = self.game
                        screen = self.screen
                        mover = self.game.mover
                        board = self.game.board

                # QUIT
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


main = Main()
main.mainloop()
