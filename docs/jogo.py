from telainicio import *
from Funcoes import *
ponto = Ponto()
tela_inicio = tela_inicio()
if __name__=="__main__":
    tela_inicio.desenha()
    ponto.cauda()
    while ponto.recebe_evento(ponto.state['tecla']):
            ponto.colisao()
            ponto.desenha_coracao()
            ponto.desenha()

        