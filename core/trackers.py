class Tracker:
    todos_trackers = dict()


    def __init__(self, _chave, _valor, _pos) -> None:
        self.chave = _chave
        self.pos = _pos
        self.valor = _valor
        self.visivel = True
        Tracker.todos_trackers[_chave] = self


    def update_valor(self, _novo_valor):
        self.valor = _novo_valor
    
    def toggle_visibilidade(self):
        self.visivel = not self.visivel