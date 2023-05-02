import pygame
import math

class tela_inicio:
    def __init__(self):
        pygame.init()
        lista = []
        self.tick = pygame.time.get_ticks()
        pygame.mixer.music.load('sprites/01. Elden Ring.mp3')#musica de fundo
        pygame.mixer.music.play(-1)#toca a musica
        self.window = pygame.display.set_mode((1024, 720))#cria a janela do jogo
        pygame.display.set_caption("Dragons rage")
        self.som_dragao = pygame.mixer.Sound('sprites/dragon-roar-96996.mp3')#som do dragao
        self.fonte = pygame.font.Font('sprites/8-BIT WONDER.TTF', 45)#fonte do titulo
        self.fonte_baixo = pygame.font.Font('sprites/8-BIT WONDER.TTF', 20)#fonte do texto abaixo do titulo
        self.fonte_espera = pygame.font.Font('sprites/8-BIT WONDER.TTF', 60)#fonte do texto apos iniciar o jogo
        self.cor = (255, 255, 255)#cor inicial do titulo
        for contador in range(39):#cria uma lista com todas as imagens da tela inicial
            imagem = pygame.image.load(f'sprites/tile0{contador}.png')
            imagemreal=pygame.transform.scale(imagem, (1024, 720))
            lista.append(imagemreal)
        self.assets = {
            'fundo_de_tela': lista,
        }
    def desenha(self):
        imagens = self.assets['fundo_de_tela']#variavel que recebe a lista de imagens
        i = 0
        self.rodando = True
        while self.rodando:#roda a tela inicial
            valorizado = imagens[i]
            pygame.time.delay(40)#delay para trocar as imagens
            self.window.blit(valorizado, (0, 0))
            tempo = pygame.time.get_ticks() / 1000.0 #tempo para mudar a cor do titulo
            self.cor = (int(abs(math.sin(tempo) * 110)+140),40,40) #muda a cor do titulo
            texto_contorno = self.fonte.render('Dragons Rage', True, (255,255,255))#cria o contorno do titulo
            texto_pos = texto_contorno.get_rect(center=(542, 60))
            for posicao in [(3,0), (-3,0), (0,3), (0,-3)]:#move o contorno do titulo
                texto_pos.move_ip(*posicao)
                pygame.display.get_surface().blit(texto_contorno, texto_pos)
            texto_real = self.fonte.render('Dragons Rage', True, self.cor)#cria o titulo
            texto_pos = texto_real.get_rect(center=(542, 60))
            pygame.display.get_surface().blit(texto_real, texto_pos)#desenha o titulo
            texto_contorno_baixo = self.fonte_baixo.render('aperte qualquer tecla para jogar', True, (0,0,0))#cria o contorno do texto abaixo do titulo
            texto_pos_baixo = texto_contorno_baixo.get_rect(center=(542, 620))
            for posicao_baixo in [(4,0), (-4,0), (0,4), (0,-4)]:#move o contorno do texto abaixo do titulo
                texto_pos_baixo.move_ip(*posicao_baixo)
                pygame.display.get_surface().blit(texto_contorno_baixo, texto_pos_baixo)
            texto_real_baixo = self.fonte_baixo.render('aperte qualquer tecla para jogar', True, (255,255,255))#cria o abaixo do titulo
            texto_pos_baixo = texto_real_baixo.get_rect(center=(542, 620))
            pygame.display.get_surface().blit(texto_real_baixo, texto_pos_baixo)#desenha o texto abaixo do tiutlo
            i += 1
            if i >= len(imagens):#condição para voltar a primeira imagem
                i = 0
            pygame.display.update()
            for eventos in pygame.event.get():#condicao para terminar a tela inicial
                    if eventos.type == pygame.QUIT:
                        self.rodando = False
                        return self.rodando
                    elif eventos.type == pygame.KEYDOWN:
                        self.window.fill((0,0,0))
                        pygame.mixer_music.stop()
                        texto_contorno_baixo = self.fonte_espera.render('Destrua o castelo', True, (255,160,0))#cria o contorno da espera
                        texto_pos_baixo = texto_contorno_baixo.get_rect(center=(522, 360))
                        for posicao_baixo in [(3,0), (-3,0), (0,3), (0,-3)]:#move o contorno da espera
                            texto_pos_baixo.move_ip(*posicao_baixo)
                            pygame.display.get_surface().blit(texto_contorno_baixo, texto_pos_baixo)
                        texto_real_baixo = self.fonte_espera.render('Destrua o castelo', True, (255,255,255))#cria da espera
                        texto_pos_baixo = texto_real_baixo.get_rect(center=(522, 360))
                        pygame.display.get_surface().blit(texto_real_baixo, texto_pos_baixo)#desenha o texto da espera
                        pygame.display.update()
                        self.som_dragao.play()
                        pygame.time.delay(5000)
                        self.rodando = False
                        return self.rodando
    def estado(self):
        return self.rodando