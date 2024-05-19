from .base import Mob
from config.configuracoes import randint, pygame
from pygame import *
from recursos import dados
from ..rede_neural.rede_neural import RedeNeural

class Player(Mob):
    def __init__(self, vida, dano, real=False):
        Mob.__init__(self, 'recursos/imagens/sprite1.png', (1, 1), (70, 60), (0, 0), vida, dano)

        self.rede_neural = RedeNeural([2, 6, 6, 2], ['relu', 'relu', 'relu'], 0, 0.05)
        self.recompensa = 0

        self.rect.centerx = randint(100, 500)
        self.rect.centery = randint(500, 600)

        self.image_dir = pygame.transform.rotate(self.image, -10)
        self.image_esq = pygame.transform.rotate(self.image, 10)

        self.velocidade = 4
        self.real = real
    
    def mover_esquerda(self):
        self.velocidade_x -= self.velocidade
        self.image = self.image_esq
    def mover_direita(self):
        self.velocidade_x += self.velocidade
        self.image = self.image_dir

    def obter_entradas(self):
        return [randint(0, 100), randint(0, 100)]

    def update(self):

        if not self.real:
            self.recompensa += 1
            self.rede_neural.definir_entrada(self.obter_entradas())
            output = self.rede_neural.obter_saida()

            if output[0]:
                self.mover_esquerda()
            if output[1]:
                self.mover_direita()
        
        self.mover()
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > dados.dimensoes_janela[0]:
            self.rect.right = dados.dimensoes_janela[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > dados.dimensoes_janela[1]:
            self.rect.bottom = dados.dimensoes_janela[1]


class Controle:  # criar classe para resolver coisas sobre controle
    def __init__(self):

        self.eixo_x = 0
        self.eixo_y = 0

        self.iniciar_joy()
    
    def iniciar_joy(self):
        
        quantidade_joysticks = pygame.joystick.get_count() # verificar se há joysticks
        if quantidade_joysticks > 0:
            self.controle = pygame.joystick.Joystick(0)
            self.controle.init()
    
    def conferir_joystik(self, event):
        eixo_joystick = event.axis
        if eixo_joystick == 0:
            self.eixo_x = event.value
        if eixo_joystick == 1:
            self.eixo_y = event.value
    
    def mover(self):
        if jogador != None:
            # para mover player ao pressionar tecla, ou joystick
            if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT] or self.eixo_x <= -0.4:
                jogador.mover_esquerda()
            if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT] or self.eixo_x >= 0.4:
                jogador.mover_direita()
            
            if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] or self.eixo_y <= -0.4:
                jogador.rect.y -= jogador.velocidade
            if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] or self.eixo_y >= 0.4:
                jogador.rect.y += jogador.velocidade

controle = Controle()
jogador = None
