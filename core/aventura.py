import threading
from .quests import *

def aventura(_jogador, _dificuldade):
    print(_jogador)
    while _jogador.vivo:
        _quest_sucesso = quest(_jogador, _dificuldade)
        print("Thread", _jogador.vivo)
        
        if _jogador.vivo:
            print("Quest terminada!")

            _dificuldade += 1
            _jogador.dano *= 1.5
            _jogador.vida_max *= 1.6
            _jogador.vida = _jogador.vida_max

            print(f"{_jogador.nome} é agora nível {_dificuldade}")
        
        else:
            print(f"{_jogador.nome} faleceu...")
            return False