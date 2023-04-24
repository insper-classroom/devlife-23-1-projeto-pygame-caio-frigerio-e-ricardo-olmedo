import pygame

class Ponto:
    def __init__(self):
        pygame.init()
        self.tick = pygame.time.get_ticks()
        self.tempo = 100
        self.window = pygame.display.set_mode((1024, 720))
        pygame.display.set_caption("Jogo Dragao")
        dragao_ini = pygame.image.load('sprites/dragaoo_cab.png')
        dragao_co = pygame.image.load('sprites/dragao_corpo.png')
  
        dragao_corpo = pygame.transform.scale(dragao_co, (90, 40))
        dragao_img = pygame.transform.scale(dragao_ini, (67, 56))
        self.direcao = pygame.math.Vector2(2,2)
        self.velo = 7
        self.assets = {
            'dragao_pos': [50, 100],
            'dragao_img': dragao_img,
            'dragao_corpo': dragao_corpo,
        }

        self.state = {
            'tecla': 'direita'

        }
    
    def recebe_evento(self, tecla):       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.state['tecla'] = 'direita'
                if event.key == pygame.K_a:
                    self.state['tecla'] = 'esquerda'
                if event.key == pygame.K_w:
                    self.state['tecla'] = 'cima'
                if event.key == pygame.K_s:
                    self.state['tecla'] = 'baixo'
            print(self.state['tecla'])
        if self.state['tecla'] == 'direita':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][0] += self.direcao.x * self.velo
                print(self.assets['dragao_pos'][0])
                self.tick = agora
        if self.state['tecla'] == 'esquerda':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][0] -= self.direcao.x * self.velo
                print(self.assets['dragao_pos'][0])
                self.tick = agora
        if self.state['tecla'] == 'cima':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][1] -= self.direcao.y * self.velo
                print(self.assets['dragao_pos'][1])
                self.tick = agora
        if self.state['tecla'] == 'baixo':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][1] += self.direcao.y * self.velo
                print(self.assets['dragao_pos'][1])
                self.tick = agora
        
        return True, self.state['tecla']

    def atualiza_estado(self):
        pass



    def desenha(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['dragao_corpo'], (self.assets['dragao_pos'][0]-11, self.assets['dragao_pos'][1] -48))
        self.window.blit(self.assets['dragao_corpo'], (self.assets['dragao_pos'][0]-11, self.assets['dragao_pos'][1] - 23))
        self.window.blit(self.assets['dragao_img'], (self.assets['dragao_pos'][0], self.assets['dragao_pos'][1]))
        
        pygame.display.update()


if __name__ == '__main__':
    ponto = Ponto()
    
    while ponto.recebe_evento(ponto.state['tecla']):
        ponto.desenha()
