
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
        while True:
            game.show_bg(screen)
            #pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

main =main()
main.mainloop()
