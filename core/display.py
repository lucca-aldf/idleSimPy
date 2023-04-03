import pygame as pg
from os import path
from .trackers import *


class Display:
    pg.init()
    pg.display.init()

    font_path = path.join("core", "database", "fonts", "EightBitDragon-anqx.ttf")

    # Load the font file
    font = pg.font.Font(font_path, 16)
    
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

    def update():
        Display.TELA.fill((185, 110, 194))
        lista_elementos = Display.paginas[Display.pagina_atual].elementos
        for obj in lista_elementos:
            if lista_elementos[obj].visivel:
                Display.print_text(str(lista_elementos[obj].valor), lista_elementos[obj].pos)

        pg.display.update()

    pg.display.update()

