from .personagens import *
from .elementos import *
from time import sleep


def quest(_personagem, _dificuldade, _data):
    
    TIPOS_PASSOS = ["Viagem", "Combate", "Descanso", "Busca", "Escolta", "Explorar"]

    _epico = 0
    passos = list()

    for _ in range(rd.randint(3,24)):
        _passo = rd.choice(TIPOS_PASSOS)

        if _passo == "Viagem":
            passos.append((
                rd.choice(LISTA_LUGARES),
                _distancia := rd.randint(30,250),
                _dificuldade_real := _dificuldade - rd.randint(1,3),
            ))

            _epico += _distancia * max(1, _dificuldade_real) / 100

        elif _passo== "Combate":
            passos.append((
                "Combate",
                _personagem,
                Personagem.gerar(_dificuldade_real := max(0, _dificuldade - rd.randint(3,5)))
            ))
            
            _epico += _dificuldade_real
    
    for etapa in passos:
        resultado = passo(*etapa)
        
        if not resultado:
            return False
    
        _data.avancar_etapa()
        Tracker.todos_trackers["Data"].update_valor(_data.get_data_extensa())
        
    return True
    

def passo(_passo, *args):
    if _passo == "Viagem":
        return viagem(*args)

    if _passo == "Combate":
        return combate(*args)


def viagem(_personagem, _destino, _distancia, _dificuldade):
    print(_distancia, _dificuldade)
    while _personagem.vivo and _distancia > 0:
        sleep(0.1)

        _chance_ataque = rd.random < _dificuldade / 30

        if _chance_ataque:
            combate(_personagem, Personagem.gerar(_dificuldade - 3))

        else:
            _personagem.dinheiro["cobre"] += rd.randint(1,10)

        _distancia -= rd.randint(15, 60)
        _distancia = max(0, _distancia)

    return _personagem.vivo


        


def combate(_personagem, _inimigo):
    Tracker.todos_trackers["NomeInimigo"].update_valor(_inimigo.nome)

    while _personagem.vivo and _inimigo.vivo:
        sleep(0.1)

        _inimigo.receber_dano(_personagem.get_ataque())

        if _inimigo.vida > 0:
            _personagem.receber_dano(_inimigo.get_ataque())
                        
    if _personagem.vida > 0:
        print(f"{_personagem.nome} matou {_inimigo.nome}")
        _personagem.historia.append(f"{_personagem.nome} derrotou {_inimigo.nome} em um combate")
        return True
    return False


def busca(_personagem):
    # Tracker.todos_trackers["Acao"].update_valor(_inimigo.nome)
    pass


def viagem(_personagem):
    pass