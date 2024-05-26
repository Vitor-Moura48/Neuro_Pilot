from config.configuracoes import pygame, plano_de_fundo, plano_de_fundo2, tela, fps, clock, uniform
from recursos import dados
from src.jogo import inimigos, player, colisoes, visualizador
from src.rede_neural import estrategia_evolutiva


def atualizar_objetos():

    if dados.mobs_restantes <= 0: # quando esse contador acabar o cenári odeve mudar para o boss
        pass
    if len(dados.sprites_inimigas) < 5:
        if uniform(0, 1) > 0.5:
            dados.sprites_inimigas.add(inimigos.Inimigo1(2, 1))
        else:
            dados.sprites_inimigas.add(inimigos.Inimigo2(2, 1))  

    # adiconar objetos sprites na tela
    dados.sprites.draw(tela)
    dados.sprites.update()

def finalizar_partida():

    inimigos.grupo_inimigos = []
    for sprite in dados.sprites:
        sprite.kill()
    
    player.jogador = player.Player(2, 1, real=True)

    estrategia_evolutiva.gerenciador.nova_partida()

def responder_a_eventos():
    
    for event in pygame.event.get(): # responder a eventos

        if event.type == pygame.QUIT:
            print("game over")
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for agente in dados.sprites_agentes:
                    agente.disparar()

estrategia_evolutiva.gerenciador = estrategia_evolutiva.GerenciadorNeural(600, 4, 0.5, player.Player, (2, 1))
estrategia_evolutiva.gerenciador.nova_partida()
colisoes.colisao = colisoes.Colisoes()
visualizador.informacoes = visualizador.Visualizador()
player.jogador = player.Player(2, 1, real=True)

while True: # loop principal

    if len(estrategia_evolutiva.gerenciador.agentes) == 0 and player.jogador == None:
        finalizar_partida()

    dados.cenario = (dados.cenario + 1.5) if dados.cenario < 1000 else 0

    tela.fill((000, 000, 000))
    tela.blit(plano_de_fundo, (0, dados.cenario)) # plano de fundo da tela
    tela.blit(plano_de_fundo2, (0, dados.cenario - 1000))

    atualizar_objetos()

    colisoes.colisao.update()
    visualizador.informacoes.update()

    responder_a_eventos()

    player.controle.mover()

    pygame.display.flip()  # atualizar a tela
    clock.tick(fps)