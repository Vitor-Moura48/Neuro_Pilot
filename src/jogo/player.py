from .base import Mob
from config.configuracoes import randint, pygame, math
from recursos import dados
from ..rede_neural.rede_neural import RedeNeural

class Player(Mob):
    def __init__(self, vida, dano, real=False):
        Mob.__init__(self, 'recursos/imagens/sprite1.png', (1, 1), (70, 60), (0, 0), vida, dano)

        self.rede_neural = RedeNeural([14, 16, 8, 4], ['relu', 'relu', 'relu'], 0, 0.05)

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
    def animacao_normal(self):
        self.image = self.sprites[0]
    def mover_frente(self):
        self.velocidade_y -= self.velocidade
    def mover_tras(self):
        self.velocidade_y += self.velocidade

    def obter_entradas(self):
        entradas = [self.rect.centerx, self.rect.centery]

        if len(dados.sprites_inimigas) > 0:

            inimigos = []
            for inimigo in dados.sprites_inimigas: 

                distancia_x = inimigo.rect.center[0] - self.rect.center[0]
                distancia_y = inimigo.rect.center[1] - self.rect.center[1]
                distancia = math.hypot(distancia_x, distancia_y)

                inimigos.append([distancia, distancia_x, distancia_y, inimigo.velocidade])

            inimigos.sort(key=lambda x: x[3])

            while len(inimigos) > 4:
                inimigos.pop(-1)
        
            for inimigo in range(len(inimigos)):  
                inimigos[inimigo].pop(0)
            
            for inimigo in inimigos:
                entradas.extend(inimigo)
        
        entradas.extend([0] * (14 - len(entradas))) # preenche com 0 oq faltar
               
        return entradas

    def update(self):

        if not self.real:
            self.rede_neural.recompensa += 1
            self.rede_neural.definir_entrada(self.obter_entradas())
            output = self.rede_neural.obter_saida()

            if output[0]:
                self.mover_esquerda()
            if output[1]:
                self.mover_direita()
            elif output[0] == False and output[1] == False:
                self.animacao_normal()
            
            if output[2]:
                self.mover_frente()
            if output[3]:
                self.mover_tras()
        
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

            parado = True
            # para mover player ao pressionar tecla, ou joystick
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT] or self.eixo_x <= -0.4:
                jogador.mover_esquerda()
                parado = False
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT] or self.eixo_x >= 0.4:
                jogador.mover_direita()
                parado = False
            elif parado:
                jogador.animacao_normal()
            
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP] or self.eixo_y <= -0.4:
                jogador.mover_frente()
            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN] or self.eixo_y >= 0.4:
                jogador.mover_tras()

controle = Controle()
jogador = None
