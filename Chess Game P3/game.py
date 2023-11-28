import pygame
from constants import *
from board import Board
from square import Square
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(rows):
            for column in range(columns):
                if (row + column) % 2 == 0:
                    color = (150, 75, 0)
                else:
                    color = (245, 245, 220)

                rect = (column * sq_size, row * sq_size, sq_size, sq_size)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(rows):
            for column in range(columns):
                if self.board.squares[row][column].has_piece():
                    piece = self.board.squares[row][column].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)

                        img = pygame.image.load(piece.texture)
                        img = pygame.transform.scale(img, (sq_size, sq_size))

                        img_center = (
                            column * sq_size + sq_size // 2,
                            row * sq_size + sq_size // 2
                        )

                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    


