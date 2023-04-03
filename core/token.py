class Token:

    def __init__(self, nome_, epico_):
        self.nome = nome_
        self.epico = epico_


class Item(Token):

    def __init__(self, nome_, epico_, desc_):
        super().__init__(nome_, epico_)
        self.desc = desc_


class Arma(Item):

    def __init__(self, nome_, epico_, desc_, dano_):
        super().__init__(nome_, epico_, desc_)
        self.dano = dano_


class Armadura(Item):
    def __init__(self, nome_, epico_, desc_, protecao_):
        super().__init__(nome_, epico_, desc_)
        self.protecao = protecao_
