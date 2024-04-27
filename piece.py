import math
import os 
class piece:
    def __init__(self,name,color,value,texture=None,texture_rect=None) -> None:
        self.name=name
        self.color=color
        value_sign =1 if color =='white' else -1
        self.value=value*value_sign
        self.texture=texture
        self.set_texture()
        self.moves=[]
        self.moved=False
        self.texture_rect=texture_rect
    def set_texture(self,size=80):
        self.texture=os.path.join(f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
    def add_move(self,move):
        self.moves.append(move)
class Pawn(piece):
    def __init__(self, color):
        self.dir =-1 if color=='white' else 1
        super().__init__('pawn',color,1.0)



class Knight(piece):
    def __init__(self, color):
        super().__init__('knight',color,3.0)

class Bishop(piece):
    def __init__(self, color):
        super().__init__('bishop',color,3.001)

class Rook(piece):
    def __init__(self, color):
        super().__init__('rook',color,5.0)

class Queen(piece):
    def __init__(self, color):
        super().__init__('queen',color,9.0)
class King(piece):
    def __init__(self, color):
        super().__init__('king',color,100000000000000)
