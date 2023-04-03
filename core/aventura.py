import threading
from .quests import *

def aventura(jogador, _dificuldade):
    while jogador.vivo:
        _quest_sucesso = quest(jogador, _dificuldade)
        
        if jogador.vivo and _quest_sucesso:
            print("Quest terminada!")

            _dificuldade += 1
            jogador.dano *= 1.5
            jogador.vida_max *= 1.6
            jogador.vida = jogador.vida_max

            print(f"{jogador.nome} é agora nível {_dificuldade}")
        
        else:
            print(f"{jogador.nome} faleceu...")