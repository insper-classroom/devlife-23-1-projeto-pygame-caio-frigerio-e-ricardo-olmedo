import pygame
import random
class cauda:
    def __init__(self):
        self.posicao = ()
        self.direcao = ""
    def colide(self):
        pass
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
        plano = pygame.image.load('sprites/portaa_f.png')
        plano_de_fundo = pygame.transform.scale(plano, (1024, 720))
        s_dragao_corpo_s = pygame.image.load('sprites/dragao_corpo.png')
        s_dragao_corpo_d = pygame.image.load('sprites/dragao_corpo_direita.png')
        s_dragao_corpo_e = pygame.image.load('sprites/dragao_corpo_esquerda.png')
        s_dragao_corpo_w = pygame.image.load('sprites/dragao_corpo_direita.png')
        self.dragao_corpo_s = pygame.transform.scale(s_dragao_corpo_s, (90, 40))
        self.dragao_corpo_d = pygame.transform.scale(s_dragao_corpo_d, (90, 90))
        self.dragao_corpo_w = pygame.transform.scale(s_dragao_corpo_w, (90, 40))
        self.dragao_corpo_e = pygame.transform.scale(s_dragao_corpo_e, (90, 40))
        self.dragao_img_e = pygame.transform.scale(dragao_ini_e, (90, 75))
        self.dragao_img_d = pygame.transform.scale(dragao_ini_d, (90, 75))
        self.dragao_img_b = pygame.transform.scale(dragao_ini_b, (90, 75))
        self.dragao_img_c = pygame.transform.scale(dragao_ini_c, (90, 75))
        self.direcao = pygame.math.Vector2(2,2)
        self.velo = 2
        self.caudas = 0
        self.coracao = 5
        #react dragao 
        largura = self.dragao_img_c.get_width()
        altura = self.dragao_img_c.get_height()
        rect_dragao = pygame.Rect(200,300, largura, altura)
  
        self.assets = {
            'dragao_pos': rect_dragao,
            'dragao_img': self.dragao_img_b,
            'dragao_corpo': {},
            'fundo_de_tela': plano_de_fundo,
            'guarda': guarda,
            'coracao': coracao_true,
        }
        self.state = {
            'tecla': 'direita',
            'pos_anterior': [0, 0],
            'coracao_pos': [],
            'cauda_pos': [],
            'acoes': [],
            'caudas_obj': []
        }
        
        
    def recebe_evento(self, tecla):       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.state['tecla'] = 'direita'
                    self.assets['dragao_img'] = self.dragao_img_d
                    self.state['acoes'].append(['direita',self.assets['dragao_pos']])
                    print(self.state['acoes'])
                if event.key == pygame.K_a:
                    self.state['tecla'] = 'esquerda'
                    self.assets['dragao_img'] = self.dragao_img_e
                    self.state['acoes'].append(['esquerda',self.assets['dragao_pos']])
                if event.key == pygame.K_w:
                    self.state['tecla'] = 'cima'
                    self.assets['dragao_img'] = self.dragao_img_c
                    self.state['acoes'].append(['cima',self.assets['dragao_pos']])
                if event.key == pygame.K_s:
                    self.state['tecla'] = 'baixo'
                    self.assets['dragao_img'] = self.dragao_img_b
                    self.state['acoes'].append(['baixo',self.assets['dragao_pos']])
        
        
        if self.state['tecla'] == 'direita':
            agora = pygame.time.get_ticks()
            self.state['pos_anterior'] = (self.assets['dragao_pos'][0] -45), self.assets['dragao_pos'][1] -10
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][0] += self.direcao.x * self.velo
                self.tick = agora
                
        if self.state['tecla'] == 'esquerda':
            self.state['pos_anterior'] = (self.assets['dragao_pos'][0] +45), self.assets['dragao_pos'][1] -10
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][0] -= self.direcao.x * self.velo
                self.tick = agora
            
        if self.state['tecla'] == 'cima':
            self.state['pos_anterior'] = (self.assets['dragao_pos'][0]), self.assets['dragao_pos'][1] +40
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][1] -= self.direcao.y * self.velo
                self.tick = agora
                self.state['pos_anterior'] = (self.assets['dragao_pos'][0] -45), self.assets['dragao_pos'][1] -10
        if self.state['tecla'] == 'baixo':
            agora = pygame.time.get_ticks()
            if agora - self.tick >= self.tempo:
                self.assets['dragao_pos'][1] += self.direcao.y * self.velo
                self.tick = agora
                self.state['pos_anterior'] = (self.assets['dragao_pos'][0]), self.assets['dragao_pos'][1] +50
        
        return True, self.state['tecla']
    def coracao_spw(self):
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
          
    def desenha(self):
        self.window.blit(self.assets['guarda'], (20,20) )
        self.window.blit(self.assets['dragao_img'], (self.assets['dragao_pos'][0], self.assets['dragao_pos'][1]))
        pos = (self.assets['dragao_pos'][0], self.assets['dragao_pos'][1])
        print(self.assets['dragao_pos'][0], " ", self.assets['dragao_pos'][1])
        for i in range(self.caudas):
            self.state['caudas_obj'][i].posicao = (self.state['cauda_pos'][i][0], self.state['cauda_pos'][i][1])
        #    self.state['caudas_obj'][i].posicao = (self.state['cauda_pos'][i][0], self.state['cauda_pos'][i][1])
            self.state['caudas_obj'][i].posicao = pos
            self.state['caudas_obj'][i].direcao = self.state['tecla']

            self.window.blit(self.dragao_corpo_s, (pos[0], pos[1]))
            pos = (self.state['caudas_obj'][i].posicao[0], self.state['caudas_obj'][i].posicao[1])
            pos = (self.state['caudas_obj'][i].posicao[0]+ i *30, self.state['caudas_obj'][i].posicao[1])


            print('vlit ',self.state['caudas_obj'][i].posicao)
            print('pos ', i, " ",pos)
        pygame.display.update()
    def colisao(self):
        i = 0
        for coracao in self.state['coracao_pos']:
            if coracao.colliderect(self.assets['dragao_pos']):
                i +=1
                self.state['coracao_pos'].remove(coracao)
                self.state['cauda_pos'].append([self.state['pos_anterior'][0], self.state['pos_anterior'][1]])
                self.caudas +=1
           
           
                c = cauda()
                self.state['caudas_obj'].append(c)
                self.state['caudas_obj'][self.caudas - 1].posicao = (self.state['pos_anterior'][0], self.state['pos_anterior'][1])
                self.state['caudas_obj'][self.caudas - 1].direcao = self.state['tecla']
            
if __name__ == '__main__':
    ponto = Ponto()
    ponto.coracao_spw()
    while ponto.recebe_evento(ponto.state['tecla']):
        ponto.colisao()
        ponto.desenha_coracao()
        ponto.desenha()