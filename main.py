
import pygame 
import sys
from const import *
from game import Game

class main:
    def __init__(self):
        pygame.init()
        self.game=Game()
        
        self.screen= pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Chess game")
  
    def mainloop(self):
        game =self.game
        screen=self.screen
        dragger =self.game.dragger
        board = self.game.board

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            #pygame.event.pump()
            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                #click 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row=dragger.mouseY //SQSIZE
                    clicked_col= dragger.mouseX // SQSIZE
                    print (dragger.mouseY , clicked_row)
                    print (dragger.mouseX , clicked_col)
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece =board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                #mousemotion 
                elif event.type== pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                #click release 
                elif event.type== pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                #quit game 
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

main =main()
main.mainloop()
