# IdleSim

import sys
import threading
import time
import pygame as pg
import math
from core import *
from pygame.locals import *


def main():
    # Clock utilizado internamente pelo PyGame
    CLOCK = pg.time.Clock()

    #Variavel de carregamento de musica
    pg.mixer.music.load("gfx/music.mpga")


    # Variaveis para carregamento de imagens para renderização
    A_img= pg.image.load("gfx/A.png").convert_alpha()
    H_img= pg.image.load("gfx/H.png").convert_alpha()
    P_img= pg.image.load("gfx/P.png").convert_alpha()
    floresta_img = pg.image.load("gfx/Back.png").convert_alpha()
    Mapa_img = pg.image.load("gfx/mapa.jpg").convert_alpha()
    castelo_img = pg.image.load("gfx/castelo.jpg").convert_alpha()
    caverna_img = pg.image.load("gfx/caverna.jpg").convert_alpha()
    deserto_img = pg.image.load("gfx/Deserto.jpg").convert()
    fcongelada_img = pg.image.load("gfx/floresta congelada.jpg").convert_alpha()
    praia_img = pg.image.load("gfx/praia.jpg").convert_alpha()



    # sprites herois
    heroi1_img = pg.image.load("gfx/sprites herois/heroi1.png").convert_alpha()
    heroi2_img = pg.image.load("gfx/sprites herois/heroi2.png").convert_alpha()
    heroi3_img = pg.image.load("gfx/sprites herois/heroi3.png").convert_alpha()
    heroina1_img = pg.image.load("gfx/sprites herois/heroina1.png").convert_alpha()
    heroina2_img = pg.image.load("gfx/sprites herois/heroina2.png").convert_alpha()
    heroina3_img = pg.image.load("gfx/sprites herois/heroina3.png").convert_alpha()

    #sprites vilões
    harpia1_img = pg.image.load("gfx/sprites monstros/hrp1.png").convert_alpha()
    harpia2_img = pg.image.load("gfx/sprites monstros/hrp2.png").convert_alpha()
    gesqueleto1_img = pg.image.load("gfx/sprites monstros/skeleton1.png").convert_alpha()
    gesqueleto2_img = pg.image.load("gfx/sprites monstros/skeleton2.png").convert_alpha()
    esqueleto1_img = pg.image.load("gfx/sprites monstros/sklt1.png").convert_alpha()
    esqueleto2_img = pg.image.load("gfx/sprites monstros/sklt2.png").convert_alpha()
    sereia1_img = pg.image.load("gfx/sprites monstros/sereia1.png").convert_alpha()
    sereia2_img = pg.image.load("gfx/sprites monstros/sereia2.png").convert_alpha()
    demonio1_img = pg.image.load("gfx/sprites monstros/dmn1.png").convert_alpha()
    demonio2_img = pg.image.load("gfx/sprites monstros/dmn2.png").convert_alpha()
    goblin1_img = pg.image.load("gfx/sprites monstros/gbln1.png").convert_alpha()
    goblin2_img = pg.image.load("gfx/sprites monstros/gbln2.png").convert_alpha()
    yeti1_img = pg.image.load("gfx/sprites monstros/yet1.png").convert_alpha()
    yeti2_img = pg.image.load("gfx/sprites monstros/yet2.png").convert_alpha()
    troll1_img = pg.image.load("gfx/sprites monstros/troll1.png").convert_alpha()
    troll2_img = pg.image.load("gfx/sprites monstros/troll2.png").convert_alpha()
    zumbi1_img = pg.image.load("gfx/sprites monstros/zmb1.png").convert_alpha()
    zumbi2_img = pg.image.load("gfx/sprites monstros/zmb2.png").convert_alpha()
    fantasma1_img = pg.image.load("gfx/sprites monstros/gst1.png").convert_alpha()
    fantasma2_img = pg.image.load("gfx/sprites monstros/gst2.png").convert_alpha()
    gigante1_img = pg.image.load("gfx/sprites monstros/gnt1.png").convert_alpha()
    gigante2_img = pg.image.load("gfx/sprites monstros/gnt2.png").convert_alpha()
    aranha1_img = pg.image.load("gfx/sprites monstros/arnh1.png").convert_alpha()
    aranha2_img = pg.image.load("gfx/sprites monstros/arnh2.png").convert_alpha()
    golem1_img = pg.image.load("gfx/sprites monstros/glm1.png").convert_alpha()
    golem2_img = pg.image.load("gfx/sprites monstros/glm2.png").convert_alpha()
    fera1_img = pg.image.load("gfx/sprites monstros/lobo1.png").convert_alpha()
    fera2_img = pg.image.load("gfx/sprites monstros/lobo2.png").convert_alpha()
    sapo1_img = pg.image.load("gfx/sprites monstros/sapo1.png").convert_alpha()
    sapo2_img = pg.image.load("gfx/sprites monstros/sapo2.png").convert_alpha()

    """#herois
    class Heroi(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(heroi1_img)
            self.sprites.append(heroi2_img) 
            self.sprites.append(heroi3_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft= 100, 100
 

    class Heroina(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(heroina1_img)
            self.sprites.append(heroina2_img) 
            self.sprites.append(heroina3_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft= 100, 100

        
        def update(self):
            self.atual = (self.atual + 1) % len(self.sprites)
            self.image = self.sprites[self.atual]

    heroi= Heroi()
    heroina= Heroina()
    

    

    ##inimigos 
    class Sapo(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(sapo1_img)
            self.sprites.append(sapo2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Demonio(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(demonio1_img)
            self.sprites.append(demonio2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Aranha(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(aranha1_img)
            self.sprites.append(aranha2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Esqueleto(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(esqueleto1_img)
            self.sprites.append(esqueleto2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Harpia(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(harpia1_img)
            self.sprites.append(harpia2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Lobo(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(fera1_img)
            self.sprites.append(fera2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Golem(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(golem1_img)
            self.sprites.append(golem2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Troll(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(troll1_img)
            self.sprites.append(troll2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Yeti(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(yeti1_img)
            self.sprites.append(yeti2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Gesqueleto(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(gesqueleto1_img)
            self.sprites.append(gesqueleto2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100

    
    class Sereia(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(sereia1_img)
            self.sprites.append(sereia2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Goblin(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(goblin1_img)
            self.sprites.append(goblin2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Zumbi(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(zumbi1_img)
            self.sprites.append(zumbi2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Fantasma(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(fantasma1_img)
            self.sprites.append(fantasma2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    class Gigante(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(gigante1_img)
            self.sprites.append(gigante2_img)

            self.atual = 0
            self.image = self.sprites[self.atual]

            self.rect = self.image.get_rect()
            self.rect.bottomleft = 100, 100


    sprites_monstros = pg.sprite.Group()

    demonio_das_sombras = Demonio()
    espectro_devorador = Fantasma()
    golem_de_gelo = Golem()
    harpia_voadora = Harpia()
    esqueleto_amaldicoado = Esqueleto()
    troll_enfurecido = Troll()
    aberracao_das_trevas = Gigante()
    fada_obiscura = Harpia()
    espectro_sinistro = Fantasma()
    goblin_andarilho = Goblin()
    aranha_mistica = Aranha()
    aranha_mortifera = Aranha()
    ogro_vermelho = Gigante()
    sapo_feroz = Sapo()
    fera_gigante = Lobo()
    sereia_encantadora = Sereia()
    troll_de_pedra = Troll()
    lobo_devorador = Lobo()
    guerreiro_esqueleto = Gesqueleto()
    zumbi_frenetico = Zumbi()


    sprites_monstros.add(demonio_das_sombras, espectro_devorador, golem_de_gelo, harpia_voadora, esqueleto_amaldicoado, troll_enfurecido, aberracao_das_trevas, fada_obiscura, espectro_sinistro, goblin_andarilho, aranha_mistica, aranha_mortifera, ogro_vermelho, sapo_feroz, fera_gigante, sereia_encantadora, troll_de_pedra, lobo_devorador, guerreiro_esqueleto, zumbi_frenetico)


"""
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
    tela_aventura.add_elemento  ("Background"         , \
                        Imagem   ("Background"        ,  floresta_img           , 15 / 10, (  0,   0)))
    tela_historia.add_elemento  ("Background"         , \
                        Imagem   ("Background"        ,  Mapa_img           , 1 / 1, (  0,   0)))
    tela_personagem.add_elemento  ("Background"         , \
                        Imagem   ("Background"        ,  Mapa_img           , 1 / 1, (  0,   0)))

    tela_aventura.add_elemento  ("BotaoAventura"      , \
                        Botao   ("BotaoAventura"      ,  A_img                , 1 / 8, (  0, 287)))
    tela_historia.add_elemento  ("BotaoAventura"      , \
                        Botao   ("BotaoAventura"      ,  A_img                , 1 / 8, (  0, 287)))
    tela_personagem.add_elemento("BotaoAventura"      , \
                        Botao   ("BotaoAventura"      ,  A_img                , 1 / 8, (  0, 287)))
    
    tela_aventura.add_elemento  ("BotaoHistoria"      , \
                        Botao   ("BotaoHistoria"      ,  H_img                , 1 / 8, (  0, 347)))
    tela_historia.add_elemento  ("BotaoHistoria"      , \
                        Botao   ("BotaoHistoria"      ,  H_img                , 1 / 8, (  0, 347)))
    tela_personagem.add_elemento("BotaoHistoria"      , \
                        Botao   ("BotaoHistoria"      ,  H_img                , 1 / 8, (  0, 347)))
    
    tela_aventura.add_elemento  ("BotaoPersonagem"    , \
                        Botao   ("BotaoPersonagem"    ,  P_img                , 1 / 8, (  0, 407)))
    tela_historia.add_elemento  ("BotaoPersonagem"    , \
                        Botao   ("BotaoPersonagem"    ,  P_img                , 1 / 8, (  0, 407)))
    tela_personagem.add_elemento("BotaoPersonagem"    , \
                        Botao   ("BotaoPersonagem"    ,  P_img                , 1 / 8, (  0, 407)))

    tela_aventura.add_elemento("VidaJogadorTexto"     , \
                       Tracker("VidaJogadorTexto"     , "Vida do Personagem"     , 16, (145, 300)))
    tela_aventura.add_elemento("VidaJogadorNumero"    , \
                       Tracker("VidaJogadorNumero"    , 100                      , 16, (145, 320)))
    
    tela_aventura.add_elemento("NomeInimigo"          , \
                       Tracker("NomeInimigo"          , ""                       , 16, (145, 410)))
    tela_aventura.add_elemento("ContraTexto"          , \
                       Tracker("ContraTexto"          , "Contra"                 , 12, (145, 390)))
    tela_aventura.add_elemento("NomeJogador"          , \
                       Tracker("NomeJogador"          , "Héroi"                  , 16, (145, 370)))
    
    tela_aventura.add_elemento("DataAtual"          , \
                       Tracker("DataAtual"          , data_atual.get_data_extensa(), 12, (2, 2)))
    tela_aventura.add_elemento("DataCurta"          , \
                       Tracker("DataCurta"          , data_atual.get_data_curta(), 12, (2, 22)))
    
    pg.mixer.music.play(-1)
    
    #tela_historia.add_elemento("DataEvento"         , \
     #                  Tracker("DataEvento"         , "Ola" , 8, (40, 600)))
    #tela_historia.add_elemento("Evento"             , \
     #                  Tracker("Evento"             , "Professor" , 12, (80, 600)))




    threads = list()
    running = True
    Display.get_tela().fill((185, 110, 194))
    threads_esperando = 0
    while running:
        #game_tick += 1

        dificuldade = 0
        personagem_jogador = Player.gerar()
        dict_trackers["NomeJogador"].update_valor(personagem_jogador.nome)



        if personagem_jogador.sexo == 'Feminino' :
           tela_aventura.add_elemento  ("herois"         , \
                Imagem   ("heroina"        ,  heroina1_img          , 2/1, (  90,   180)))   
           
                             
        if personagem_jogador.sexo == 'Masculino' :
            tela_aventura.add_elemento  ("herois"         , \
                Imagem   ("heroi"        ,  heroi1_img          , 2/1, (  90,   180))) 




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
            #display historia
            for i in range(min(25,len(personagem_jogador.historia))):
                tela_historia.add_elemento(f"HistoriaJogador{i}"     , \
                       Tracker(f"HistoriaJogador{i}"     , personagem_jogador.historia[i]     , 8, (145, 300+15*i)))        


            Display.update()   
            CLOCK.tick(60)
        tela_aventura.rmv_elemento("herois")
        for i in range(min(25,len(personagem_jogador.historia))):
            tela_historia.add_elemento(f"HistoriaJogador{i}"     , \
                       Tracker(f"HistoriaJogador{i}"     ,  ''     , 8, (145, 300+15*i)))        


        
        """heroina.update()
        heroina_image=heroina.image
        heroina_rect=heroina.rect

        tela_aventura.blit(heroina_image, heroina_rect)"""
                        
             
            
        
    pg.quit()

if __name__ == "__main__":
        main()