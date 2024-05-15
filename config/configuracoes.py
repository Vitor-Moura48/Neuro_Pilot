import pygame
import numpy
import os
from random import randint, uniform, choice

fps = 60
clock = pygame.time.Clock()

tela = pygame.display.set_mode((600, 700), pygame.RESIZABLE)

plano_de_fundo = pygame.image.load("recursos/imagens/space1.png")
plano_de_fundo2 = pygame.image.load("recursos/imagens/space1.png")

pygame.display.set_caption("Neural Pilot")