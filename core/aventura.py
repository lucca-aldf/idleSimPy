import threading
from .quests import *

def aventura(jogador, _dificuldade):
    while jogador.vivo:
        _quest_sucesso = quest(jogador, _dificuldade)
        
        if jogador.vivo and _quest_sucesso:
            print("Quest terminada!")
            jogador.historia.append(f"{jogador.nome} terminou sua quest.")

            _dificuldade += 1
            jogador.dano *= 1.5
            jogador.vida_max *= 1.6
            jogador.vida = jogador.vida_max

            print(f"{jogador.nome} é agora nível {_dificuldade}")
            jogador.historia.append(f"{jogador.nome} é um aventureiro de nível {_dificuldade} agora.")
        
        else:
            print(f"{jogador.nome} faleceu...")
            jogador.historia.append(f"{jogador.nome} foi derrotado em combate.")
            jogador.historia.append(f"Esse é o fim da história de {jogador.nome}")
    print(jogador.historia)