import pygame
import sys

from constants import *
from game import Game
from board import Board
from dragger import Dragger

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CheckMate!")
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // sq_size
                    clicked_column = dragger.mouseX // sq_size

                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_column].has_piece():
                        piece = board.squares[clicked_row][clicked_column].piece
                        # valid piece (color) ?
                        
                    
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                            # show methods
                        game.show_bg(screen)
                        game.show_pieces(screen)
                            

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // sq_size
                    motion_col = event.pos[0] // sq_size

                    

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // sq_size
                        released_column = dragger.mouseX // sq_size

                # Quit event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
