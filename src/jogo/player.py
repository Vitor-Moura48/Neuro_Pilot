from .base import Mob

class Player(Mob):
   def __init__(self, vida, dano):
        Mob.__init__(self, 'recursos/imagens/sprite1.png', (1, 1), (70, 60), (0, 0), vida, dano, escala=(0, 0))

class Controle:
    def __init__(self):
                               
