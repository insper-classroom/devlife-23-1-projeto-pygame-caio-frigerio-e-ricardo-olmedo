import pygame

class Ponto:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1024, 720))
        pygame.display.set_caption("Jogo Dragao")
        dragao_img = pygame.image.load('dragao.png')
        dragao_p = pygame.transform.scale(dragao_img, (100, 100))
        self.assets = {
            'dragao_pos': (50, 100),
            'dragao_img': dragao_p,

        }

        self.state = {

        }
    
    def recebe_evento(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        return True

        

    def desenha(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['dragao_img'], (self.assets['dragao_pos'][0], self.assets['dragao_pos'][1]))
        pygame.display.update()


if __name__ == '__main__':
    ponto = Ponto()
    while ponto.recebe_evento():
        ponto.desenha()
