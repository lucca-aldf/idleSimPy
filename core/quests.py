from .personagens import *
from time import sleep

class Quest:

    def __init__(self, _personagem, _dificuldade) -> None:
        self.passos = [Step("Combate", _personagem, max(0, _dificuldade + rd.randint(1, 3))) for i in range(rd.randint(1,6)) ]


    def getLength(self):
        return len(self.passos)

    def executar(self):
        for step in self.passos:
            resultado = step.executar()
            if not resultado:
                 break


class Step:

    def __init__(self, _tipo, _personagem, _dificuldade) -> None:
        self.tipo = _tipo
        self.personagem = _personagem
        self.dificuldade = _dificuldade


    def executar(self):
        if self.tipo == "Combate":
            inimigo = Personagem.gerar(self.dificuldade)
            return Combate(self.personagem, inimigo)
        

def Combate(_personagem, _inimigo):
    Tracker.all_trackers["NomeInimigo"].updateValor(_inimigo.nome)
    Display.update()

    while _personagem.vida > 0 and _inimigo.vida > 0:
        sleep(0.7)

        _inimigo.receberDano(_personagem.getAtaque())

        if _inimigo.vida > 0:
            _personagem.receberDano(_inimigo.getAtaque())
                        
    if _personagem.vida > 0:
        print(f"{_personagem.nome} matou {_inimigo.nome}")
        return True
    return False


