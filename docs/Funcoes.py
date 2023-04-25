import pygame
import random
import math
class Ponto:
    def __init__(self):
        pygame.init()
        self.tick = pygame.time.get_ticks()
        self.tempo = 20
        self.window = pygame.display.set_mode((1024, 720))
        pygame.display.set_caption("Jogo Dragao")
        dragao_ini_b = pygame.image.load('sprites/dragaoo_cab.png')
        dragao_ini_e = pygame.image.load('sprites/dragaoo_cab_esq.png')
        dragao_ini_c = pygame.image.load('sprites/dragaoo_cab_cima.png')
        dragao_ini_d = pygame.image.load('sprites/dragaoo_cab_direita.png')
        
        corcao = pygame.image.load('sprites/coracao.png')
        coracao_true = pygame.transform.scale(corcao, (90, 40))
        sprite_g = pygame.image.load('sprites/guarda.png')
        guarda = pygame.transform.scale(sprite_g, (130, 150))
        dragao_co = pygame.image.load('sprites/dragao_corpo.png')
        plano = pygame.image.load('sprites/portaa_f.png')
        plano_de_fundo = pygame.transform.scale(plano, (1024, 720))
        dragao_corpo = pygame.transform.scale(dragao_co, (90, 40))
        self.dragao_img_e = pygame.transform.scale(dragao_ini_e, (67, 56))
        self.dragao_img_d = pygame.transform.scale(dragao_ini_d, (67, 56))
        self.dragao_img_b = pygame.transform.scale(dragao_ini_b, (67, 56))
        self.dragao_img_c = pygame.transform.scale(dragao_ini_c, (67, 56))
        self.direcao = pygame.math.Vector2(2,2)
        self.velo = 2
        self.vida = 1
        self.coracao = 5
        #react dragao 
        largura = self.dragao_img_c.get_width()
        altura = self.dragao_img_c.get_height()
        rect_dragao = pygame.Rect(200,300, largura, altura)
  
        self.assets = {
            'dragao_pos': rect_dragao,
            'dragao_img': self.dragao_img_b,
            'dragao_corpo': dragao_corpo,
            'fundo_de_tela': plano_de_fundo,
            'guarda': guarda,
            'coracao': coracao_true,
            
        }

        self.state = {
            'tecla': 'direita',
            'pos_anterior': [0, 0],
            'coracao_pos': [],
        
        }
        
        
    def recebe_evento(self, tecla):       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.state['tecla'] = 'direita'
                    self.assets['dragao_img'] = self.dragao_img_d
                if event.key == pygame.K_a:
                    self.state['tecla'] = 'esquerda'
                    self.assets['dragao_img'] = self.dragao_img_e
                if event.key == pygame.K_w:
                    self.state['tecla'] = 'cima'
                    self.assets['dragao_img'] = self.dragao_img_c
                if event.key == pygame.K_s:
                    self.state['tecla'] = 'baixo'
                    self.assets['dragao_img'] = self.dragao_img_b
        self.state['pos_anterior'] = self.assets['dragao_pos'][0], self.assets['dragao_pos'][1]

        if self.state['tecla'] == 'direita':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][0] += self.direcao.x * self.velo
                self.tick = agora
        if self.state['tecla'] == 'esquerda':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][0] -= self.direcao.x * self.velo
                self.tick = agora
        if self.state['tecla'] == 'cima':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][1] -= self.direcao.y * self.velo
                self.tick = agora
        if self.state['tecla'] == 'baixo':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][1] += self.direcao.y * self.velo
                self.tick = agora
        

        return True, self.state['tecla']

    def cauda(self):
        larg = self.assets['coracao'].get_width()
        alt = self.assets['coracao'].get_height()
        for i in range(10):
            x = random.randint(0, 1024 - larg)
            y = random.randint(0, 720 - alt) 
            if [x,y] not in self.state['coracao_pos']:
                rect = pygame.Rect(x,y, larg, alt)
                self.state['coracao_pos'].append(rect)
        

    def desenha_coracao(self):
        self.window.blit(self.assets['fundo_de_tela'], (0, 0))
        for coracao in self.state['coracao_pos']:
            self.window.blit(self.assets['coracao'], (coracao[0], coracao[1]))
            print(self.vida)
        
    def desenha(self):
        
        
        self.window.blit(self.assets['dragao_corpo'], (self.state['pos_anterior'][0], self.state['pos_anterior'][1]))
        self.window.blit(self.assets['guarda'], (20,20) )
        self.window.blit(self.assets['dragao_img'], (self.assets['dragao_pos'][0], self.assets['dragao_pos'][1]))
        pygame.display.update()

    def colisao(self):
        for coracao in self.state['coracao_pos']:
            if coracao.colliderect(self.assets['dragao_pos']):
                self.state['coracao_pos'].remove(coracao)
                self.vida += 1
                print(self.vida)
