from .database import *
from .elementos import *
from .display import *
from .token import *
import random as rd
import math

class Personagem:
	
    def __init__(self, _nome="", _vida="", _ataque="") -> None:

        self.vivo           = True
        self.nome			= _nome
        self.vida			= _vida
        self.vida_max		= _vida
        self.dano			= _ataque

    # Métodos

    def receber_dano(self, _dano_recebido):
        self.vida -= _dano_recebido
        if self.vida < 0:
            self.vivo = False

    # Retornos
    def get_ataque(self):
        return self.dano
    
    def gerar(_dificuldade):
        _dificuldade = max(0, _dificuldade)

        nome = rd.choice(NOMES_INIMIGOS)
        
        vida = int(10 + 12 * (1.2 ** _dificuldade))
        dano = int( 2 +  8 * (1.3 ** _dificuldade))
        
        
        return Personagem(nome, vida, dano)


class Player(Personagem):
    casa = rd.choice(NOMES_CASAS).split()[-1]

    
    def __init__(self, _nome, _vida, _ataque, _idade, _sexo, _historia):
        super().__init__(_nome, _vida, _ataque)
        self.nome = self.nome + " da casa " + Player.casa
        self.idade = _idade
        self.sexo = _sexo
        self.historia = _historia
        #self.historia = list()

        self.dinheiro = {
            "ouro":  0,
            "prata": 0,
            "cobre": 0
        }
        self.inventario = list()

        #self.arma = Arma()
        #self.armadura = Armadura()


    def gerar():
        _nome = rd.choice(NOMES_HEROIS)
        _vida = 60
        _dano = 15
        _historia = []
    
        return Player(_nome[0], _vida, _dano, 18, _nome[1], _historia)
    
    def receber_dano(self, _dano_recebido):
        self.vida -= _dano_recebido
        Tracker.todos_trackers["VidaJogadorNumero"].update_valor(f"{max(self.vida, 0)} / {self.vida_max}")

        if self.vida < 0:
            self.vivo = False


#class Sprites(Imagem):
    #def __init__(self, _chave, _imagem, _escala, _pos):



         
