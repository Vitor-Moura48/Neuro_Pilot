from config.configuracoes import pygame

dimensoes_janela = pygame.display.get_surface().get_size()

sprites = pygame.sprite.Group()
sprites_inimigas = pygame.sprite.Group()
sprites_agentes = pygame.sprite.Group()
sprites_projeteis_aliados = pygame.sprite.Group()
sprites_projeteis_inimigos = pygame.sprite.Group()

quantidade_mobs = 0
mobs_restantes = 30

cenario = 0