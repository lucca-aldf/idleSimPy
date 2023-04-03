# IdleSim

import sys
import threading
import time
import pygame as pg
import math
from core import *


def main():
    
    # Initialize pygame

    # Clock set-up
    CLOCK = pg.time.Clock()

    # Display

    # Game loop
    running = True

    # Screen setting
    pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 0)


    # Title and Icon
    #pg.display.set_caption("gfx/Race Works")
    #icon = pg.image.load("gfx/RaceWorksIcon.png")
    #pg.display.set_icon(icon)

    #track = pg.image.load(f"gfx/{track_name} Mask.png")
    #SCREEN.blit(track, (0, 0))
    pg.display.update()
    GAME_TICK = 0

    dict_trackers = Tracker.todos_trackers
    tela_aventura = Display("AVENTURA")
    tela_historia = Display("HISTÓRIA")
    tela_historia = Display("PLACEHOLDER")

    tela_aventura.add_elemento("VidaJogadorTexto"   , \
                       Tracker("VidaJogadorTexto"   , "Vida do Personagem" , (105, 220)))
    tela_aventura.add_elemento("VidaJogadorNumero"  , \
                       Tracker("VidaJogadorNumero"  , 100                  , (105, 240)))
    
    tela_aventura.add_elemento("NomeInimigo"        , \
                       Tracker("NomeInimigo"        , ""                   , (130, 290)))
    tela_aventura.add_elemento("NomeJogador"        , \
                       Tracker("NomeJogador"        , "Héroi"              , (130, 320)))
    

    threads = list()
    running = True
    Display.get_tela().fill((185, 110, 194))

    while running:
        #CLOCK.tick(60)
        #game_tick += 1

        
        dificuldade = 0
        personagem_jogador = Player.gerar()
        dict_trackers["NomeJogador"].update_valor(personagem_jogador.nome)

        minha_aventura = threading.Thread(
                target=aventura, args=(personagem_jogador, dificuldade), daemon=True)

        minha_aventura.start()
        while personagem_jogador.vida > 0:
            for event in pg.event.get():
                if event.type == pg.QUIT: # Sair do jogo 
                    pg.quit()
                    sys.exit()
                    
                elif event.type == pg.KEYDOWN: # Input do teclado
                    if event.key == pg.K_ESCAPE: # Sair do jogo (teclado)
                        pg.quit()
                        sys.exit()
                        
                    elif event.key == pg.K_w or event.key == pg.K_UP:
                        lista_paginas = list(Display.paginas.keys())
                        indice_atual = lista_paginas.index(Display.pagina_atual)
                        Display.pagina_atual = lista_paginas[(indice_atual + 1) % len(lista_paginas)]
                        
                    elif event.key == pg.K_s or event.key == pg.K_DOWN:
                        lista_paginas = list(Display.paginas.keys())
                        indice_atual = lista_paginas.index(Display.pagina_atual)
                        Display.pagina_atual = lista_paginas[(indice_atual - 1) % len(lista_paginas)]
                        
                # Handle mouse input
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Handle mouse clicks
                    pass


            Display.update()   
            CLOCK.tick(60)
                        
             
            
        
    pg.quit()

if __name__ == "__main__":
        main()


        #if not render_all:
        #    SCREEN.blit(best_car.image, (int(best_car.pos_x), int(best_car.pos_y)))

    
        # Check to close app
        '''
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            running = False'''


#grid.sort(key=lambda car: (car.fitness()), reverse=True)
