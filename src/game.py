import pygame
from const import *
from board import Board
from piece import *

class Game:
    def __init__(self):
        self.board = Board()

        #Show Methods
    def show_background(self, surface):
        """
        Shows the screen as a chessboard on the provided surface
        ---------
        :param surface: pygame.display Object, the surface on which the game will be displayed
            while it is being played
        """
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                   color = (234, 235, 200) # a light shade of green for a light-colored square
                else:
                   color = (119, 154, 88) # a dark shade of green for a dark-colored square
                
                rect = (col * sqsize, row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
         for row in range(rows):
            for col in range(cols):
                #check if there is a piece
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * sqsize + sqsize // 2, row * sqsize + sqsize // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)