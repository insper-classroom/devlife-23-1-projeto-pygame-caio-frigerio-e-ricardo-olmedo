from telainicio import *
from telagameover import *
from Funcoes import *

ponto = Ponto()
tela_inicio = tela_inicio()
tela_over = gameover()
if __name__ == '__main__':
    rodando= True
    while rodando:
        tela_inicio.desenha()
        ponto.coracao_spw()
        while ponto.recebe_evento(ponto.state['tecla']):
            ponto.colisao()
            ponto.desenha_coracao()
            ponto.desenha()
        tela_over.desenha()
        if tela_over.recebe_evento()==True:
            rodando = False
