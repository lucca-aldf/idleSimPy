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
        Tracker.todos_trackers[_chave] = self
        

    def update_valor(self, _novo_valor):
        self.valor = _novo_valor

    def get_render(self, _font, *args, **kwargs):
        render = _font[self.tamanho_fonte].render(str(self.valor), False, self.cor)
        return render
    
    def get_valor(self):
        return self.valor

class Botao(Elemento):
    todos_botoes = dict()

    def __init__(self, _chave, _imagem, _pos, _escala):
        super().__init__(_chave, _pos)

        largura = _imagem.get_width()
        altura = _imagem.get_height()
        self.imagem = pg.transform.scale(_imagem, (int(largura * _escala), int(altura + _escala)))
        self.rect = self.imagem.get_rect()
        self.rect.topleft= self.pos
        self.clicado = False

        Botao.todos_botoes[_chave] = self
    
    def get_render(self, *args, **kwargs):
        return self.imagem



    def foo():
        action = False
        #get mouse position
        pos = pg.mouse.get_pos()

        #check mouseover and clicado condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicado == False:
                self.clicado= True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicado = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x,self.rect.y))

        return action
