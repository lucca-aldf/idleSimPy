from .database import *
from .trackers import *
from .display import *
import random as rd

class Personagem:
	
    def __init__(self, _nome="", _vida="", _ataque="") -> None:

        self.nome			= _nome
        self.vida			= _vida
        self.vida_max		= _vida
        self.dano			= _ataque

    # Métodos

    def receberDano(self, danoRecebido):
        self.vida -= danoRecebido

    # Retornos
    def getAtaque(self):
        return self.dano
    
    def gerar(_dificuldade):
        
        nome = rd.choice(NOMES_INIMIGOS)
        
        vida = int(16 + 8 * (_dificuldade ** 1.6))
        dano = int(10 + 5 * (_dificuldade ** 1.75))
        
        
        return Personagem(nome, vida, dano)


class Player(Personagem):
    casa = rd.choice(NOMES_CASAS).split()[-1]

    
    def __init__(self, _nome, _vida, _ataque, _idade, _sexo):
        super().__init__(_nome, _vida, _ataque)
        self.nome = self.nome + " da casa " + Player.casa
        self.idade = _idade
        self.sexo = _sexo

    def gerar():
        
        nome = rd.choice(NOMES_HEROIS)
        
        vida = 180
        dano = 25
        
        
        return Player(nome[0], vida, dano, 18, nome[1])
    
    def receberDano(self, danoRecebido):
        self.vida -= danoRecebido
        Tracker.all_trackers["VidaJogador"].updateValor(self.vida)
        Display.update()