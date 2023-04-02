# IdleSim

import random as rd
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


    render_all = True




    #track = pg.image.load(f"gfx/{track_name} Mask.png")
    #SCREEN.blit(track, (0, 0))
    pg.display.update()
    GAME_TICK = 0



    Display.createTracker("VidaJogadorTexto", Tracker("Vida do Personagem", (105, 220)))
    Display.createTracker("VidaJogador", Tracker(100, (105, 240)))
    
    Display.createTracker("NomeInimigo", Tracker("", (130, 290)))
    Display.createTracker("NomeJogador", Tracker("", (130, 320)))
    


    running = True

    while running:
        #CLOCK.tick(60)
        #game_tick += 1


        Display.getScreen().fill((185, 110, 194))
        
        # Estao ouvindo?????
        dificuldade = 0
        personagem_jogador = Player.gerar()
        Tracker.all_trackers["NomeJogador"].updateValor(personagem_jogador.nome)

        while personagem_jogador.vida > 0:
            quest_atual = Quest(personagem_jogador, dificuldade)
                        
            quest_atual.executar()
            if personagem_jogador.vida > 0:
                print("Quest terminada!")

                dificuldade += 1
                personagem_jogador.dano *= 1.5
                personagem_jogador.vida_max *= 1.6
                personagem_jogador.vida = personagem_jogador.vida_max

                print(f"{personagem_jogador.nome} é agora nível {dificuldade}")
            
            else:
                print(f"{personagem_jogador.nome} faleceu...")
        
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
