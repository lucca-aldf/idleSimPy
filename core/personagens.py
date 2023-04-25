from .database import *
from .elementos import *
from .display import *
from .token import *
import random as rd
import math
from numpy import prod

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
        
        vida = int(10 + prod([rd.randint(8,15) for _ in range(int(1.2 ** _dificuldade))]))
        dano = int( 2 +  8 * (1.3 ** _dificuldade))
        
        
        return Personagem(nome, vida, dano)


class Player(Personagem):
    casa = rd.choice(NOMES_CASAS).split()[-1]

    
    def __init__(self, _nome, _vida, _ataque, _idade, _sexo):
        super().__init__(_nome, _vida, _ataque)
        self.nome = self.nome + " da casa " + Player.casa
        self.idade = _idade
        self.sexo = _sexo

        self.dinheiro = {
            "ouro":  0,
            "prata": 0,
            "cobre": 0
        }
        self.inventario = list()

        #self.arma = Arma()
        #self.armadura = Armadura()

        self.historia = list()

    def gerar():
        _nome = rd.choice(NOMES_HEROIS)
        _vida = rd.randint(50,80)
        _dano = rd.randint(9,20)
    
        return Player(_nome[0], _vida, _dano, 18, _nome[1])
    
    def receber_dano(self, _dano_recebido):
        self.vida -= _dano_recebido
        Tracker.todos_trackers["VidaJogadorNumero"].update_valor(f"{max(self.vida, 0)} / {self.vida_max}")

        if self.vida < 0:
            self.vivo = False


#class Sprites(Imagem):
    #def __init__(self, _chave, _imagem, _escala, _pos):



class Historia:

    def __init__(self, _desc, _epico, _data):
        self.desc = _desc
        self.epico = _epico
        self.data = _data

    def __lt__(self, _other):
        return self._escore < _other.score
    
    def escore(self):
        _escore = math.log(self._epico)
        return _escore
         
