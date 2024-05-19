from .base import Mob
from config.configuracoes import randint

class Player(Mob):
   def __init__(self, vida, dano):
        Mob.__init__(self, 'recursos/imagens/sprite1.png', (1, 1), (70, 60), (0, 0), vida, dano)

        self.rect.centerx = randint(100, 500)
        self.rect.centery = randint(500, 600)

class Controle:
    def __init__(self):
        pass
