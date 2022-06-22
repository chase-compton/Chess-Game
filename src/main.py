import pygame
import sys
from const import *
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess Game')
        self.game = Game()

    def mainloop(self):
        game = self.game
        screen = self.screen
        mover=self.game.mover
        board=self.game.board

        while True:
            game.show_background(screen)
            game.show_pieces(screen)

            if mover.moving:
                mover.update_blit(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mover.update_mouse(event.pos)
                    clicked_row=mover.mouseY//SQ_SIZE
                    clicked_col=mover.mouseX//SQ_SIZE
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece=board.squares[clicked_row][clicked_col].piece
                        mover.save_initial(event.pos)
                        mover.move_piece(piece)

                elif event.type == pygame.MOUSEMOTION:
                    if mover.moving:
                        mover.update_mouse(event.pos)
                        game.show_background(screen)
                        game.show_pieces(screen)
                        mover.update_blit(screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    mover.stop_move()

                # QUIT
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


main = Main()
main.mainloop()
