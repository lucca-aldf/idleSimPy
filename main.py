# IdleSim

import sys
import threading
import time
import pygame as pg
import math
import core.button as button
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

    #load button images
    A_img= pg.image.load('images/A.png').convert_alpha()
    H_img= pg.image.load('images/H.png').convert_alpha()
    C_img= pg.image.load('images/C.png').convert_alpha()


    #pg.display.set_caption("gfx/Race Works")
    #icon = pg.image.load("gfx/RaceWorksIcon.png")
    #pg.display.set_icon(icon)
    
    
    pg.display.update()
    

    data_atual = Data()

    dict_trackers = Tracker.todos_trackers
    tela_aventura = Display("AVENTURA")
    tela_historia = Display("HISTÓRIA")


    #A_button= button.Button(20,20, A_img, 0.5)
    #H_button= button.Button(20,50, H_img, 0.5)
    #C_button= button.Button(20,80, C_img, 0.5)
    
    tela_aventura.add_elemento("VidaJogadorTexto"   , \
                       Tracker("VidaJogadorTexto"   , "Vida do Personagem" , (105, 220)))
    tela_aventura.add_elemento("VidaJogadorNumero"  , \
                       Tracker("VidaJogadorNumero"  , 100                  , (105, 240)))
    
    tela_aventura.add_elemento("NomeInimigo"        , \
                       Tracker("NomeInimigo"        , ""                   , (130, 290)))
    tela_aventura.add_elemento("NomeJogador"        , \
                       Tracker("NomeJogador"        , "Héroi"              , (130, 320)))
    
    tela_aventura.add_elemento("Data"        , \
                       Tracker("Data"        , data_atual.get_data_extensa(), (0, 50)))


    tela_historia.add_elemento("DataEvento"         , \
                       Tracker("DataEvento"         , "He" ,  (40, 600)))
    tela_historia.add_elemento("Evento"             , \
                       Tracker("Evento"             , "She" , (80, 600)))

    threads = list()
    running = True
    Display.get_tela().fill((185, 110, 194))
    threads_esperando = 0
    while running:
        #CLOCK.tick(60)
        #game_tick += 1

        '''if A_button.draw(Display.TELA):
            print("aaa")
        if H_button.draw(Display.TELA):
            print("aaa")
        if C_button.draw(Display.TELA):
            print("aaa")'''
        
        dificuldade = 0
        personagem_jogador = Player.gerar()
        dict_trackers["NomeJogador"].update_valor(personagem_jogador.nome)

        #dict_trackers["Evento"].update_valor(personagem_jogador.historia)

        minha_aventura = threading.Thread(
                target=aventura, args=(personagem_jogador, dificuldade, data_atual), daemon=True)
        threads.append(minha_aventura)
        minha_aventura.start()
        while personagem_jogador.vivo:

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