
from const import *
from square import Square 
class Board(object):
    def __init__(self):
        pass
    def create(self):
        self.squares=[[0,0,0,0,0,0,0,0]for col in range(COLS)]
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col]=  Square(row,col)

    def _add_piece(self,color):
        pass



