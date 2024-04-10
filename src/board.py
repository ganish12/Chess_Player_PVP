from const import *
from square import Square
from piece import *

class Board:

    def __init__(self):
        """
        Creating the game board object for the game to be played on. This is overlayed on the pygame 
        display so there is accurate visual feedback. Initializes the board with 8 arrays of zeros
        to fill the game board with zeros.
        """

        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(cols)]

        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

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
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

        #adding the row of pawns
        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        #adding the knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        #adding the rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        
        #adding the bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        #adding the queens
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        #adding the kings
        self.squares[row_other][4] = Square(row_other, 4, King(color))

        
        