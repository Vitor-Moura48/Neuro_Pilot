import pygame
import numpy, math, time
import os
from random import randint, uniform, choice

pygame.init()

fps = 600
clock = pygame.time.Clock()

largura = 600
altura = 700

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)

plano_de_fundo = pygame.image.load("recursos/imagens/space1.png")
plano_de_fundo2 = pygame.image.load("recursos/imagens/space1.png")

musica_de_fundo = pygame.mixer.Sound("recursos/sons/fundo.wav")
musica_de_fundo.set_volume(0.5)
musica_de_fundo.play(-1)

pygame.display.set_caption("Neural Pilot")