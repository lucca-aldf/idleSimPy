import threading
from .quests import *

def aventura(_jogador, _dificuldade, _data):
    print(f"Um novo herói surge: {_jogador.nome}")
    _jogador.historia.append(f"{_jogador.nome} saiu em uma jornada.")
    while _jogador.vivo:
        _quest_sucesso = quest(_jogador, _dificuldade, _data)
        
        if _jogador.vivo:
            print("Quest terminada!")
            _jogador.historia.append(f"{_jogador.nome} terminou sua quest.")

            _dificuldade += 1
            _jogador.dano = int(1.1 * _jogador.dano)
            _jogador.vida_max = int(1.2 * _jogador.vida_max)
            _jogador.vida = _jogador.vida_max

            print(f"{_jogador.nome} é agora nível {_dificuldade}")
            _jogador.historia.append(f"{_jogador.nome} é um aventureiro de nível {_dificuldade} agora.")
        
        else:
            print(f"{_jogador.nome} faleceu...")
            _jogador.historia.append(f"{_jogador.nome} foi derrotado em combate.")
            _jogador.historia.append(f"Esse é o fim da história de {_jogador.nome}")
    print(_jogador.historia)
