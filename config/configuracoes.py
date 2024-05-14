import pygame
import numpy
import os
from random import randint, uniform, choice

fps = 60
clock = pygame.time.Clock()

tela = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

plano_de_fundo = pygame.image.load("recursos/imagens/space1.png")
plano_de_fundo = pygame.transform.scale(plano_de_fundo, (650, 1000))

pygame.display.set_caption("Neural Pilot")