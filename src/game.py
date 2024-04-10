import pygame
from const import *

class Game:
    def __init__(self):
        pass

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