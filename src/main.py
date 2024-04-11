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
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_background(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)
            #quitting game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #click down
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // sqsize
                    clicked_col = dragger.mouseX // sqsize

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(screen)

                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
            

            pygame.display.update()        
        
     

main = Main()
main.mainloop()