import pygame

class Ponto:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1024, 720))
        pygame.display.set_caption("Jogo Dragao")
        dragao_ini = pygame.image.load('sprites/dragaoo_cab.png')
        dragao_co = pygame.image.load('sprites/dragao_corpo.png')
  
        dragao_corpo = pygame.transform.scale(dragao_co, (90, 40))
        dragao_img = pygame.transform.scale(dragao_ini, (67, 56))
        self.assets = {
            'dragao_pos': (50, 100),
            'dragao_img': dragao_img,
            'dragao_corpo': dragao_corpo,

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
        self.window.blit(self.assets['dragao_corpo'], (self.assets['dragao_pos'][0]-11, self.assets['dragao_pos'][1] -48))
        self.window.blit(self.assets['dragao_corpo'], (self.assets['dragao_pos'][0]-11, self.assets['dragao_pos'][1] - 23))
        self.window.blit(self.assets['dragao_img'], (self.assets['dragao_pos'][0], self.assets['dragao_pos'][1]))
        
        pygame.display.update()


if __name__ == '__main__':
    ponto = Ponto()
    while ponto.recebe_evento():
        ponto.desenha()
