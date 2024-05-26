from .base import Mob
from recursos.dados import *
from config.configuracoes import pygame, choice, randint

class Inimigo1(Mob):
    def __init__(self, vida, dano):
        Mob.__init__(self, 'recursos/imagens/sprite3.png', (1,1), (232, 171), (0, 0), vida, dano, escala=(60, 60))

        self.randomizar()
        self.image = pygame.transform.rotate(self.image, 180)

        self.velocidade = 5

    def update(self):

        self.contar_vulnerabilidade
        if self.conferir_vida():
            self.morrer()

        if mobs_restantes <= 20 and self.velocidade != 7:
            self.velocidade = 7
            
        self.velocidade_y += self.velocidade
        self.mover()
        #self.debug((000, 000, 255))

class Inimigo2(Mob):
    def __init__(self, vida, dano):
        Mob.__init__(self, 'recursos/imagens/sprite4.png', (1,1), (183, 234), (0, 0), vida, dano, escala=(60, 60))

        self.randomizar()
        self.image = pygame.transform.rotate(self.image, 180)

        self.velocidade = 4
        self.zig_zag = None

    def update(self):
        #self.debug((255, 000, 000))

        self.contar_vulnerabilidade
        if self.conferir_vida():
            self.morrer()

        if mobs_restantes <= 20:
                zig_zag = True
                
        if self.zig_zag != None:
            self.velocidade_x += 2 if zig_zag else -2
        self.velocidade_y += self.velocidade
        self.mover()
    
grupo_inimigos = []