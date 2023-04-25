import pygame
class tela_inicio:
    def __init__(self):
        pygame.init()
        self.tick = pygame.time.get_ticks()
        self.window = pygame.display.set_mode((1024, 720))
        pygame.display.set_caption("Jogo Dragao")
        plano = pygame.image.load('sprites/portaa_f.png')
        plano_de_fundo = pygame.transform.scale(plano, (1024, 720))
        self.assets = {
            'fundo_de_tela': plano_de_fundo,
        }
    def recebe_evento(self):
        self.rodando = True
        while self.rodando:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    self.rodando = False
                    return False
                    
                elif eventos.type == pygame.KEYDOWN:
                    self.rodando = False
                    return False
        return True
    def desenha(self):
        self.window.blit(self.assets['fundo_de_tela'], (0, 0))
        pygame.display.update()