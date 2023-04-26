import pygame

class gameover:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1024, 720))#cria a janela
        self.fonte = pygame.font.Font('sprites/8-BIT WONDER.TTF', 38)#carrega a fonte do titulo
        self.fonte_baixo = pygame.font.Font('sprites/8-BIT WONDER.TTF', 24)# carrega a fonte do texto
        pygame.display.set_caption("Dragons rage")
    def recebe_evento(self):
        game_zero=True#condicao para o loop
        while game_zero:  
          for eventos in pygame.event.get():
              if eventos.type == pygame.QUIT:
                  pygame.quit()
              if eventos.type == pygame.KEYDOWN:
                  if eventos.key == pygame.K_ESCAPE:#se apertar esc sai do jogo
                      return game_zero
                  if eventos.key == pygame.K_RETURN:#se apertar enter recomeca o jogo
                      game_zero=False
                      return game_zero
        return game_zero
    def desenha(self):
        self.window.fill((0,0,0))#fundo preto
        text = self.fonte.render("O CASTELO SOBREVIVE", True, (255, 255, 255))#titulo
        text_rect = text.get_rect()
        text_rect.center = (512, 340)#diz onde o titulo vai ficar
        self.window.blit(text, text_rect)#desenha o titulo
        text = self.fonte_baixo.render("Pressione Enter para voltar ao menu", True, (255, 255, 255))#texto
        text_rect = text.get_rect()
        text_rect.center = (512, 400)#diz onde o texto vai ficar
        self.window.blit(text, text_rect)#desenha o texto
        pygame.display.update()#atualiza a tela
        pygame.time.delay(1000)#espera 1 segundo

