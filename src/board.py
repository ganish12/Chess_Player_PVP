from const import *
from square import Square

class Board:

    def __init__(self):
        """
        Creating the game board object for the game to be played on. This is overlayed on the pygame 
        display so there is accurate visual feedback. Initializes the board with 8 arrays of zeros
        to fill the game board with zeros.
        """

        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(cols)]

    def _create(self):
        """
        Replaces the zeros in each "square" on the board with a Square object, allowing for pieces
        to be placed in the _add_pieces method.
        """
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        """
        Adds the pieces to the board object at each square object.
        """
        pass