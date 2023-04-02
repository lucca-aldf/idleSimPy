class Tracker:
    all_trackers = dict()

    def __init__(self, _valor, _pos) -> None:
        self.pos = _pos
        self.valor = _valor

    
    def updateValor(self, _novo_valor):
        self.valor = _novo_valor