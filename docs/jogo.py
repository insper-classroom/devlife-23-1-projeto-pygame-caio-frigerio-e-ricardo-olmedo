from telainicio import *
from telagameover import *
from Funcoes import *

tela_inicioa = tela_inicio()
main = MAIN()
tela_over = gameover()
if __name__ == '__main__':
    rodando= True
    while rodando:
        tela_inicioa.desenha()
        while SCREEN_UPDATE:
                main.draw_elements()
                tela_over.desenha()
        if tela_over.recebe_evento()==True:
            rodando = False
