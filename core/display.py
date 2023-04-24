import pygame as pg
from os import path
from .elementos import *


class Display:
    pg.init()
    pg.display.init()
    pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 0)

    pg.display.set_caption("IdleSim")

    font_path = path.join("core", "database", "fonts", "EightBitDragon-anqx.ttf")

    # Load the font file
    font = {
         8: pg.font.Font(font_path,  8),
        12: pg.font.Font(font_path, 12),
        16: pg.font.Font(font_path, 16),
        20: pg.font.Font(font_path, 20),
    

    }
    TELA = pg.display.set_mode((480, 720))

    paginas = dict()
    pagina_atual = ""
    

    def __init__(self, _nome):
        self.nome = _nome
        self.elementos = dict()
        Display.paginas[_nome] = self

        if Display.pagina_atual == "":
            Display.pagina_atual = _nome

    def print_text(_text, _coords, _color=(0, 0, 0), _font=font):
        Display.TELA.blit(Display.font.render(_text, False, _color),  _coords)

    def get_tela():
        return Display.TELA

    def add_elemento(self, _chave, _elemento):
        self.elementos[_chave] = _elemento

    def rmv_elemento(self, chave):
        if chave in self.elementos:
            del self.elementos[chave]
            
    def update():
        Display.TELA.fill((185, 110, 194))
        lista_elementos = Display.paginas[Display.pagina_atual].elementos
        for obj in lista_elementos:
            
            _obj_render = lista_elementos[obj].get_render(Display.font)
            Display.TELA.blit(_obj_render, lista_elementos[obj].get_pos())

        pg.display.update()
        

class AventuraDisplay(Display):

    def __init__(self, _nome):
        super().__init__(_nome)


class HistoriaDisplay(Display):

    def __init__(self, _nome):
        super().__init__(_nome)
