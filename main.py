from config.configuracoes import pygame, plano_de_fundo, plano_de_fundo2, tela, fps, clock, choice
from recursos import dados
from src.jogo import inimigos, player
from src.rede_neural import estrategia_evolutiva


def atualizar_objetos():

    if dados.mobs_restantes <= 0: # quando esse contador acabar o cenári odeve mudar para o boss
        pass

    if len(dados.sprites_inimigas) < 3:
        mob = choice([inimigos.Inimigo1(2, 1), inimigos.Inimigo2(2, 1)])
        dados.sprites_inimigas.add(mob)

    # adiconar objetos sprites na tela
    dados.sprites.draw(tela)
    dados.sprites.update()

def colisao():

    for agente in dados.sprites_agentes:

        for inimigo in dados.sprites_inimigas:
            if pygame.sprite.collide_rect(agente, inimigo):        
                agente.receber_dano(inimigo.dano)
    
        for projetil_inimigo in dados.sprites_projeteis_inimigos:
            if pygame.sprite.collide_rect(agente, projetil_inimigo):
                agente.receber_dano(inimigo.dano)

        
    for projetil_aliado in dados.sprites_projeteis_aliados:

        for inimigo in dados.sprites_inimigas:
            if pygame.sprite.collide_rect(projetil_aliado, inimigo):
                inimigo.receber_dano(projetil_aliado.dano)

def responder_a_eventos():
    
    for event in pygame.event.get(): # responder a eventos

        if event.type == pygame.QUIT:
            print("game over")
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for agente in dados.sprites_agentes:
                    agente.disparar()

try: player.jogador = player.Player(2, 1)
except: pass

gerenciador = estrategia_evolutiva.GerenciadorNeural(100, 1, 0.5, player.Player, (2, 1))
gerenciador.nova_partida()

while True: # loop principal

    dados.cenario = (dados.cenario + 1.5) if dados.cenario < 1000 else 0

    tela.fill((000, 000, 000))
    tela.blit(plano_de_fundo, (0, dados.cenario)) # plano de fundo da tela
    tela.blit(plano_de_fundo2, (0, dados.cenario - 1000))

    atualizar_objetos()

    colisao()

    responder_a_eventos()
    player.controle.mover()

    pygame.display.flip()  # atualizar a tela
    clock.tick(fps)

