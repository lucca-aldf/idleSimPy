from .personagens import *
from time import sleep

def quest(_personagem, _dificuldade, _data):
    print("Chegeui")
    passos = [("Combate", 
               _personagem,
               max(0, _dificuldade + rd.randint(1, 3))) for i in range(rd.randint(1,6)) ]

    
    for etapa in passos:
        resultado = passo(*etapa)
        if not resultado:
            break


def passo(_tipo, _personagem, _dificuldade):

    
    if _tipo == "Combate":
        inimigo = Personagem.gerar(_dificuldade)
        return combate(_personagem, inimigo)
        

def combate(_personagem, _inimigo):
    Tracker.todos_trackers["NomeInimigo"].update_valor(_inimigo.nome)

    while _personagem.vida > 0 and _inimigo.vida > 0:
        sleep(0.5)
        print(_personagem.vida)

        _inimigo.receber_dano(_personagem.get_ataque())

        if _inimigo.vida > 0:
            _personagem.receber_dano(_inimigo.get_ataque())
                        
    if _personagem.vida > 0:
        print(f"{_personagem.nome} matou {_inimigo.nome}")
        return True
    return False


def busca(_personagem):
    pass


def viagem(_personagem):
    pass