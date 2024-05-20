from config.configuracoes import *
from ..rede_neural import estrategia_evolutiva
from . import player, inimigos
from recursos import dados

#classe para conferir conliões
class Colisoes:

    # função para conferir as colisões com o player
    def verificar_colisao(self, objeto):
        if pygame.sprite.spritecollideany(objeto, dados.sprites_inimigas):
            estrategia_evolutiva.gerenciador.desativar_agente(objeto)
            objeto.kill()
    
    def verificar_saida(self, objeto):
        if objeto.rect.top > dados.dimensoes_janela[1] or objeto.rect.right < 0 or objeto.rect.left > dados.dimensoes_janela[0]:
            objeto.kill()
            
    # função para chamar as funções de colisão a cada iteração
    def update(self):
        if len(estrategia_evolutiva.gerenciador.agentes) > 0:
            for agente in estrategia_evolutiva.gerenciador.agentes[:]:
                self.verificar_colisao(agente)

        for objeto in dados.sprites:
            self.verificar_saida(objeto)

        try: 
            if pygame.sprite.spritecollideany(player.jogador, dados.sprites_inimigas):
                player.jogador.kill()
                player.jogador = None
        except: pass

