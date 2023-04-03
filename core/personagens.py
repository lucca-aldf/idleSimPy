from .database import *
from .trackers import *
from .display import *
from .token import *
import random as rd

class Personagem:
	
    def __init__(self, _nome="", _vida="", _ataque="") -> None:

        self.vivo           = True
        self.nome			= _nome
        self.vida			= _vida
        self.vida_max		= _vida
        self.dano			= _ataque

    # Métodos

    def receber_dano(self, danoRecebido):
        self.vida -= danoRecebido
        if self.vida < 0:
            self.vivo = False

    # Retornos
    def get_ataque(self):
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

        self.inventario = list()

        self.arma = Arma()
        self.armadura = Armadura()

    def gerar():
        _nome = rd.choice(NOMES_HEROIS)
        _vida = 180
        _dano = 25
    
        return Player(_nome[0], _vida, _dano, 18, _nome[1])
    
    def receber_dano(self, danoRecebido):
        self.vida -= danoRecebido
        Tracker.todos_trackers["VidaJogadorNumero"].update_valor(max(self.vida, 0))

        if self.vida < 0:
            self.vivo = False