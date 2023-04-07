import pygame as pg

class Elemento:
    todos_elementos = dict()

    def __init__(self, _chave, _pos):
        self.chave = _chave
        self.pos = _pos
        self.visivel = True
        Elemento.todos_elementos[_chave] = self

    
    def toggle_visibilidade(self, _visibilidade=None):
        if _visibilidade == None:
            self.visivel = not self.visivel
        else:
            self.visivel = _visibilidade

    def get_render(self, *args, **kwargs):
        return None

    def get_pos(self):
        return self.pos
    
    def get_clicados(_mouse):
    
        for item in Elemento.todos_elementos:
            with Elemento.todos_elementos[item] as elemento:
                if elemento.rect.collidepoint(_mouse):
                    return elemento
                    
                 
        return False
        

class Tracker(Elemento):
    todos_trackers = dict()


    def __init__(self, _chave, _valor, _tamanho_fonte, _pos, _cor=(0,0,0)):
        super().__init__(_chave, _pos)

        self.valor         = _valor
        self.cor           = _cor
        self.tamanho_fonte = _tamanho_fonte
        self.clicado       = False
        Tracker.todos_trackers[_chave] = self
        

    def update_valor(self, _novo_valor):
        self.valor = _novo_valor

    def get_render(self, _font, *args, **kwargs):
        render = _font[self.tamanho_fonte].render(str(self.valor), False, self.cor)
        return render
    
    def get_valor(self):
        return self.valor

class Imagem(Elemento):
    todas_imagens = dict()

    def __init__(self, _chave, _imagem, _escala, _pos):
        super().__init__(_chave, _pos)


        self.imagem = pg.transform.scale(_imagem, (_imagem.get_width() * _escala, _imagem.get_height() *_escala))

        Imagem.todas_imagens[_chave] = self
    
    def get_render(self, *args, **kwargs):
        return self.imagem
    

class Botao(Imagem):
    todos_botoes = dict()

    def __init__(self, _chave, _imagem, _escala, _pos):
        super().__init__(_chave, _imagem, _escala, _pos)

        self.rect = self.imagem.get_rect()
        self.rect.x, self.rect.y = self.pos

        Botao.todos_botoes[_chave] = self


    def get_clique(self, _mouse):
        if self.rect.collidepoint(_mouse):
            return True
    
        return False
