import pygame as pg
from .trackers import *


class Display:
    pg.init()


    pg.display.init()
    font = pg.font.SysFont('century', 25)
    to_render = list()
    screen = pg.display.set_mode((480, 900))
    
    def print_text(_text, _coords, _color=(0, 0, 0)):
        Display.screen.blit(Display.font.render(_text, False, _color),  _coords)

    def getScreen():
        return Display.screen

    def createTracker(_label, _tracker):
        Tracker.all_trackers[_label] = _tracker
        Display.to_render.append(Tracker.all_trackers[_label])

    def createElement(_element):
        Display.to_render.append(_element)

    def update():
        Display.screen.fill((185, 110, 194))
        for element in Display.to_render:
            Display.print_text(str(element.valor), element.pos)

        pg.display.update()

    pg.display.update()

