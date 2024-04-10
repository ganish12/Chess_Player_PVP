

class Square:

    def __init__(self, row, col, piece = None):
        """
        Creates a square object to be placed on the board at row, col.
        -------
        :param row: int, row for where the square object will be placed
        :param col: int, col for where the square object will be placed
        :param piece: object, default = None. Defines what piece is in the square object
        """
        self.row = row
        self.col = col 
        self.piece = piece
    
    def has_piece(self):
        return self.piece != None
