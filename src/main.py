import pygame
import sys

from const import *
from game import Game


class Main:
    def __init__(self):
        """
        Initialize the main method and create the game screen
        
        Initializes:
        
        :param screen: set the game screen to the size of (width, height) using the pygame.display function
        """

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainloop(self):
        """
        Loop the game state to allow for the game to run until a player wins via checkmate
        
        Initializes:

        Quitting method: When the event is considered a quit, the function will update the display
            and quit the game both via pygame and sys
        """

        game = self.game
        screen = self.screen
        while True:
            game.show_background(screen)
            #game.show_pieces(screen)
            #quitting game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            pygame.display.update()        
        
     

main = Main()
main.mainloop()