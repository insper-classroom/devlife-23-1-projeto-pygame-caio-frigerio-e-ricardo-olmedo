import pygame

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inicializa():
        pygame.init()
        window = pygame.display.set_mode((1024, 720))
        pygame.display.set_caption("Exemplo de Funcao")

        assets = {

        }

        state = {

        }
        return window, assets, state
    
    def recebe_evento():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            pygame.display.update()

if __name__ == '__main__':
    window, assets, state = Ponto.inicializa()
    while Ponto.recebe_evento():
         pass
