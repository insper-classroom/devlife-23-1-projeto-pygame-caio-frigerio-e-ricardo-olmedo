import pygame
import Funcoes
class tela:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dragon rage")
        self.tick = pygame.time.get_ticks()
        self.tempo = 100
        self.window = pygame.display.set_mode((1024, 720))
    def desenha(self):
        self.window.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Dragon rage", True, (255, 255, 255 )) # texto preto
        text_rect = text.get_rect(center=(1024//2, 720//2))
        self.window.blit(text, text_rect)
        pygame.display.update()
    def recebe_evento(self):
        rodando = True
        while rodando:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    return Funcoes.Ponto()
                elif eventos.type == pygame.KEYDOWN:
                    return Funcoes.Ponto()
        return True
    # Instancia a classe tela
tela_inicio = tela()

# Executa o loop principal
tela_inicio.desenha()
tela_inicio.recebe_evento()

# Finaliza o Pygame
pygame.quit()