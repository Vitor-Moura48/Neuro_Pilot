from .base import Mob
from recursos.dados import *
from config.configuracoes import pygame, choice

class Inimigos1(Mob):
    def __init__(self, vida, dano):
        Mob.__init__(self, 'recursos/imagens/sprite3.png', (1,1), (232, 171), (0, 0), vida, dano)

        self.randomizar()

        self.subir = choice([True, False])
        
        self.velocidade_inimigo = 4
        self.zig_zag = None

    def update(self):

        self.contar_vulnerabilidade
        if self.conferir_vida():
            self.morrer()

        if mobs_restantes <= 20 and self.velocidade_inimigo != 6:
            self.velocidade_inimigo = 6
            
        self.velocidade_y -= self.velocidade_inimigo
        self.mover()

class Inimigos2(Mob):
    def __init__(self, vida, dano):
        Mob.__init__(self, 'recursos/imagens/sprite4.png', (1,1), (232, 171), (0, 0), vida, dano)

        self.randomizar()

        self.subir = choice([True, False])

    def update(self):

        self.contar_vulnerabilidade
        if self.conferir_vida():
            self.morrer()

        if mobs_restantes <= 20:
                zig_zag = True
                
        if zig_zag != None:
            self.velocidade_x += 2 if zig_zag else -2
        self.velocidade_y -= self.velocidade_inimigo
        self.mover()