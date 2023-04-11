# IdleSim

import sys
import threading
import time
import pygame as pg
import math
from core import *


def main():
    # Clock utilizado internamente pelo PyGame
    CLOCK = pg.time.Clock()


    # Variaveis para carregamento de imagens para renderização
    A_img= pg.image.load("gfx/A.png").convert_alpha()
    H_img= pg.image.load("gfx/H.png").convert_alpha()
    P_img= pg.image.load("gfx/C.png").convert_alpha()


    # Icone da aba
    icon = pg.image.load("gfx/A.png")
    pg.display.set_icon(icon)
    
    
    pg.display.update()
    
    # Data inicial do jogo
    data_atual = Data(_ano = 1789, _mes=4, _dia = 10, _etapa = 4)

    # Armazenar pointer para dicionário que guarda todos os Trackers
    dict_trackers = Tracker.todos_trackers

    # Inicialização das telas com a classe Display
    tela_aventura   = Display("AVENTURA")
    tela_historia   = Display("HISTORIA")
    tela_personagem = Display("PERSONAGEM")
    
    '''
    Criação de elementos de cada tela.
    Para cada elemento, os primeiros a serem descritos serão renderizados primeiros, e portanto estarão ao fundo.
    Para criar um elemento, utilizar instrução do tipo Display().add_elemento(chave, Elemento()), onde
        - Display() é um objeto da classe Display
        - chave é uma string (que deve ser repetida a mesma para o construtor Elemento())
        - Elemento() é um objeto da classe Elemento ou derivado
    
    Para saber mais sobra a classe Elemento, vide elementos.py, ou copie um dos usos abaixo
        - Botão são para elementos que devem ser clicados
        - Tracker são para strings que devem ser apresentadas na tela
        - Imagem são para elementos estáticos que renderizem uma imagem
    '''
    tela_aventura.add_elemento  ("BotaoAventura"      , \
                        Botao   ("BotaoAventura"      ,  A_img                , 1 / 8, (  0,   0)))
    tela_historia.add_elemento  ("BotaoAventura"      , \
                        Botao   ("BotaoAventura"      ,  A_img                , 1 / 8, (  0,   0)))
    tela_personagem.add_elemento("BotaoAventura"      , \
                        Botao   ("BotaoAventura"      ,  A_img                , 1 / 8, (  0,   0)))
    
    tela_aventura.add_elemento  ("BotaoHistoria"      , \
                        Botao   ("BotaoHistoria"      ,  H_img                , 1 / 8, (  0,  60)))
    tela_historia.add_elemento  ("BotaoHistoria"      , \
                        Botao   ("BotaoHistoria"      ,  H_img                , 1 / 8, (  0,  60)))
    tela_personagem.add_elemento("BotaoHistoria"      , \
                        Botao   ("BotaoHistoria"      ,  H_img                , 1 / 8, (  0,  60)))
    
    tela_aventura.add_elemento  ("BotaoPersonagem"    , \
                        Botao   ("BotaoPersonagem"    ,  P_img                , 1 / 8, (  0, 120)))
    tela_historia.add_elemento  ("BotaoPersonagem"    , \
                        Botao   ("BotaoPersonagem"    ,  P_img                , 1 / 8, (  0, 120)))
    tela_personagem.add_elemento("BotaoPersonagem"    , \
                        Botao   ("BotaoPersonagem"    ,  P_img                , 1 / 8, (  0, 120)))

    tela_aventura.add_elemento("VidaJogadorTexto"   , \
                       Tracker("VidaJogadorTexto"   , "Vida do Personagem"     , 16, (105, 220)))
    tela_aventura.add_elemento("VidaJogadorNumero"  , \
                       Tracker("VidaJogadorNumero"  , 100                      , 16, (105, 240)))
    
    tela_aventura.add_elemento("NomeInimigo"        , \
                       Tracker("NomeInimigo"        , ""                       , 12, (130, 290)))
    tela_aventura.add_elemento("NomeJogador"        , \
                       Tracker("NomeJogador"        , "Héroi"                  , 12, (130, 320)))
    
    tela_aventura.add_elemento("DataAtual"          , \
                       Tracker("DataAtual"          , data_atual.get_data_extensa(), 8, (0, 50)))


    tela_historia.add_elemento("DataEvento"         , \
                       Tracker("DataEvento"         , "He" , 8, (40, 600)))
    tela_historia.add_elemento("Evento"             , \
                       Tracker("Evento"             , "She" , 12, (80, 600)))

    threads = list()
    running = True
    Display.get_tela().fill((185, 110, 194))
    threads_esperando = 0
    while running:
        #game_tick += 1

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
                    if event.button == 1: #LMB
                        mouse = event.pos
                        clicados = list()
                        for botao in Botao.todos_botoes.values():
                            if botao.get_clique(mouse):
                                clicados.append(botao.chave)
                        
                        for chave_botao in clicados:
                            if chave_botao == "BotaoAventura":
                                Display.pagina_atual = "AVENTURA"
                            elif chave_botao == "BotaoHistoria":
                                Display.pagina_atual = "HISTORIA"
                            elif chave_botao == "BotaoPersonagem":
                                Display.pagina_atual = "PERSONAGEM"
                    


            Display.update()   
            CLOCK.tick(60)
                        
             
            
        
    pg.quit()

if __name__ == "__main__":
        main()