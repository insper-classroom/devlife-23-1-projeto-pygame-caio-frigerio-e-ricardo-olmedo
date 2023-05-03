import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
	#Classe do dragao 
	
	def __init__(self):
	# -carrega as sprites e as ajustas
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)
		self.new_block = False
		self.remove_blocks = False
		imagemup = pygame.image.load('sprites/assets_dragao/dragaoo_cab (4).png').convert_alpha()
		imagemdown = pygame.image.load('sprites/assets_dragao/dragaoo_cab (2).png').convert_alpha()
		imagemright=pygame.image.load('sprites/assets_dragao/dragaoo_cab (5).png').convert_alpha()
		imagemleft = pygame.image.load('sprites/assets_dragao/dragaoo_cab (3).png').convert_alpha()
		size_cabe_w = imagemup.get_width()
		size_cabe_h = imagemup.get_height()

        
		self.head_up = pygame.transform.scale(imagemup, (size_cabe_w/6, size_cabe_h/6))
		self.head_down = pygame.transform.scale(imagemdown, (size_cabe_w/6, size_cabe_h/6))
		self.head_right = pygame.transform.scale(imagemright, (size_cabe_w/6, size_cabe_h/6))
		self.head_left = pygame.transform.scale(imagemleft, (size_cabe_w/6, size_cabe_h/6))
		
		rabobaixo= pygame.image.load('sprites/assets_dragao/rabobaixo removebg.png').convert_alpha()
		size_ww = rabobaixo.get_width()
		size_hh = rabobaixo.get_height()
		rabocima = pygame.image.load('sprites/assets_dragao/rabocima-removebg-preview.png').convert_alpha()
		raboesquerda = pygame.image.load('sprites/assets_dragao/raboesqeurda-removebg-preview.png').convert_alpha()
		rabodireita = pygame.image.load('sprites/assets_dragao/rabodireita-removebg-preview.png').convert_alpha()
		self.tail_up =  pygame.transform.scale(rabobaixo, (size_ww/4, size_hh/4))
		self.tail_down = pygame.transform.scale(rabocima, (size_ww/4, size_hh/4))
		self.tail_right = pygame.transform.scale(raboesquerda, (size_ww/4, size_hh/4))
		self.tail_left = pygame.transform.scale(rabodireita, (size_ww/4, size_hh/4))

		
        
		corpo_baixo = pygame.image.load('sprites/assets_dragao/dragao_corpo (2).png').convert_alpha()
		corpo_horizontal_direita = pygame.image.load('sprites/assets_dragao/dragao_corpo (5).png').convert_alpha()
		corpo_horizontal_esquerda = pygame.image.load('sprites/assets_dragao/dragao_corpo (3).png').convert_alpha()
		corpo_vertical_cima = pygame.image.load('sprites/assets_dragao/dragao_corpo (4).png').convert_alpha()
		size_corpo_h = corpo_baixo.get_height()
		size_corpo_w = corpo_baixo.get_width()
		self.body_vertical_baixo = pygame.transform.scale(corpo_baixo, (size_corpo_w/3, size_corpo_h/3))
		self.body_vertical_cima = pygame.transform.scale(corpo_vertical_cima, (size_corpo_w/3, size_corpo_h/3))
		
		self.body_horizontal = pygame.transform.scale(corpo_horizontal_direita, (size_corpo_w/3, size_corpo_h/3))
		self.body_horizontal_e = pygame.transform.scale(corpo_horizontal_esquerda, (size_corpo_w/3, size_corpo_h/3))
		
		body_tr = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_d.png').convert_alpha()
		body_tl = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_e.png').convert_alpha()
		body_br = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_d.png').convert_alpha()
		body_bl = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_e.png').convert_alpha()
		size_corpo_turn_w = body_tr.get_width()
		size_corpo_turn_h = body_tr.get_height()
		
		self.body_tr = pygame.transform.scale(body_tr, (size_corpo_turn_w/5, size_corpo_turn_h/5))
		self.body_tl = pygame.transform.scale(body_tl, (size_corpo_turn_w/5, size_corpo_turn_h/5))
		self.body_br = pygame.transform.scale(body_br, (size_corpo_turn_w/5, size_corpo_turn_h/5))
		self.body_bl = pygame.transform.scale(body_bl, (size_corpo_turn_w/5, size_corpo_turn_h/5))
		
	def draw_snake(self):
		
		self.update_tail_graphics()
		self.update_head_graphics()
		#Desenha o dragao tanto a cabeca, rabo e corpo
		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size )
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos ,y_pos,cell_size,cell_size)
		# o desenho do corpo é baseado em celulas onde ele verifica tanto a direcao para que deve ser desenhada
		# e qual a sprite
			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x and previous_block.y <= next_block.y:
					screen.blit(self.body_vertical_baixo,block_rect)
				if previous_block.x == next_block.x and previous_block.y >= next_block.y:
					screen.blit(self.body_vertical_cima,block_rect)
				elif previous_block.y == next_block.y and previous_block.x <= next_block.x:
					screen.blit(self.body_horizontal,block_rect)
				elif previous_block.y == next_block.y and previous_block.x >= next_block.x:
					screen.blit(self.body_horizontal_e,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_horizontal_e,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_horizontal_e,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_horizontal,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_horizontal,block_rect)
		self.update_head_graphics()

	def update_head_graphics(self):
		#aqui atualiza e desenha o grafico da cabeca 
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	def update_tail_graphics(self):
		#Por base em index da lista do corpo ele pega a celula e desenha em ultimo lugar
		#Tambem verifica a direcao para que possa desenha na direcao correta
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def move_snake(self):
		#primeiro iff remove um corpo baseado em index removendo os ultimos
		if self.remove_blocks == True:
			body_copy = self.body[:-1]
			body_copy.remove(body_copy[-1])
			self.body = body_copy[:]
			self.remove_blocks = False
		#Aqui adiciona blocos de corpo no ultimo lugar com a direcao para que possa saber qual sprite usar
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			if len(body_copy) != 0:
				body_copy.insert(0,body_copy[0] + self.direction)
				self.body = body_copy[:]

	def add_block(self):
		#funcao para adicionar corpo
		self.new_block = True

	def remove_block(self):
		#funcao para remover
		self.remove_blocks = True

	def reset(self):
		#reseta a direcao do dragao
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)

class FRUIT:
	def __init__(self):
		#aqui a comida do dragao é aleatoriazada
		self.randomize()

	def draw_fruit(self):
		#desenha a comida baseado no tamanho do mapa juntamente com a posicao aleatorizada 
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(apple,fruit_rect)

	def randomize(self):
		#faz a com que a posicao da comida seja aleatoria, com restricao para o tamanaho do mapa que é identificado pelo cell number -4 que seria o limite da sprite da comida
		self.x = random.randint(0,cell_number - 4)
		self.y = random.randint(0,cell_number - 4)
		self.pos = Vector2(self.x,self.y)

class GUARDA:
	def __init__(self):
		#carrega a sprite da barra de vida do personagem e as ajustas
		
		self.randomize()
		self.vida = 3
		barra_100 = pygame.image.load('sprites/barra_vida/100.png').convert_alpha()
		barra_66 = pygame.image.load('sprites/barra_vida/66.png').convert_alpha()
		barra_33 = pygame.image.load('sprites/barra_vida/33.png').convert_alpha()
		barra_0 = pygame.image.load('sprites/barra_vida/0.png').convert_alpha()
		size_h = barra_100.get_height()
		size_w = barra_100.get_width()
		self.barra_100 = pygame.transform.scale(barra_100,(size_w/4 ,size_h/4))
		self.barra_66 = pygame.transform.scale(barra_66,(size_w/4 ,size_h/4))
		self.barra_33 = pygame.transform.scale(barra_33,(size_w/4 ,size_h/4))
		self.barra_0 = pygame.transform.scale(barra_100,(size_w/4 ,size_h/4))
    	
	def randomize(self):
		#aleatoriza a posicao em que a sprite aparece com restricao no tamanho do mapa menos o tamanho da sprite
		self.x = random.randint(0,cell_number - 3)
		self.y = random.randint(0,cell_number - 3)
		self.pos = Vector2(self.x,self.y)

	def draw_monster(self):
		#cria a colisao do guarda com o dragao e faz com que ele aparece a partir das cordedas do guarda_react
		guarda_react = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(guarda,(guarda_react.x, guarda_react.y))
		
	def barra_vida(self):
		#aqui com as condicoes de vida do guarda usa o blit para utiliza a sprite de vida em que ele se encontra
		guarda_react_bara = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		if self.vida == 2:
			screen.blit(self.barra_66,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		if self.vida == 3:
			screen.blit(self.barra_100,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		if self.vida == 1:
			screen.blit(self.barra_33,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		
class PONTO:
	def __init__(self):
		#sistema de pontuacao inicializado com zero
		self.pontos = 0
		self.max_pontos = 0
	def max(self):
		#sistema de pontuacao maxima onde se a self.pontos for maior que self.max_pontos substitui ele
		if self.pontos > self.max_pontos:
			self.max_pontos = self.pontos
			
class TEXTO:
	def __init__(self):
		#essa classe faz a funcoes de inicializar a fonte e renderizar elas no jogo
		self.ponto = PONTO()
		self.fonte = pygame.font.Font('sprites/8-BIT WONDER.TTF', 16)
		self.textos = ""
		self.max = ''
		self.comeu = False
			
	def imprimir(self):
	
		if self.comeu == False:
			self.mensagem = '!!!O Dragao so aceita comer a cabeca!!!'
			impre_3 = self.fonte.render(self.mensagem,1, (255,0,0))
			screen.blit(impre_3,(200,60))
		#essa funcao faz todo o trabalho de blit dos textos da pontuacao
		impre = self.fonte.render(self.textos, 1,(255,255,255))
		impre_2 = self.fonte.render(self.max, 1,(255,255,255))
		
		screen.blit(impre, (40,20))
		screen.blit(impre_2,(40,60))
		
		pygame.display.update()

class MAIN:
	def __init__(self):
		#essa classe controla as funcoes e as chama tambem checa colisao e diz se perdeu o jogo
		self.snake = SNAKE()
		self.fruit = FRUIT()
		self.guarda = GUARDA()
		self.msg = TEXTO()
		self.pontos = PONTO()
		self.msg.textos = (f'Mate o guarda! & faca pontos!')
		self.fase = 1
		self.fase_2 = pygame.image.load('sprites/fundo2.png').convert_alpha()
		self.espada = pygame.mixer.Sound('sprites/espada.mp3')#som espada
		self.homen = pygame.mixer.Sound('sprites/homen.mp3')#som espada

		#incia e comeca o som do jogo
		pygame.mixer.init()
		pygame.mixer.music.load('sprites/Super Mario World Music.mp3')
		pygame.mixer.music.play()
		pygame.mixer.music.set_volume(0.5)
	#as 2 funcoes seguintes somente chamam funcoes para que possam acontecer	
	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()
		
	def draw_elements(self):
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.guarda.draw_monster()
		self.pontos.max()
		self.msg.imprimir()
		self.guarda.barra_vida()


	#Essa funcoes seria um game_over resetando a pontuacao atual, e a vida do guarda
	def game_over(self):
		self.snake.reset()
		self.pontos.pontos = 0
		#atualizo a msg.textos separadamente para chamar somente quando necessario(quando muda a pontuacao)
		self.msg.textos = (f'Pontos: {self.pontos.pontos}')
		self.msg.max = (f'Maximo: {self.pontos.max_pontos}')
		self.guarda.vida = 3

	def check_collision(self):
		#essa funcoes verifica a colisao e a partiri disso faz as acoes necessarias, como randomizar a posicao da comida novamente,e adicionar os blocos pois novamente
		if self.fruit.pos == self.snake.body[0]:
			self.homen.play()
			self.fruit.randomize()
			self.snake.add_block()
			
			self.pontos.pontos += 10
			self.msg.comeu = True
			
			#adiciona 10 pontos por pegar a comida
			self.msg.textos = (f'Pontos: {self.pontos.pontos}')
			self.msg.max = (f'Maximo: {self.pontos.max_pontos}')
		
		if self.snake.body[0] == self.guarda.pos:
			if len(self.snake.body) != 0 and len(self.snake.body) != 1 and len(self.snake.body) != 3:
				#verifica a colisao com o guarda e toma as acoes como perder vida do guarda 
				self.guarda.vida -=1
				self.espada.play()
				
				self.snake.remove_block()
			if self.guarda.vida == 0:
				#quando mata o guarda multiplica a pontuacao total e atualiza sua vida para 3 e randomiza a posicao do guarda para que o jogador possa matar o guarda novamente
				self.pontos.pontos *=2
				self.msg.textos = (f'Pontos: {self.pontos.pontos}')
				self.msg.max = (f'Maximo: {self.pontos.max_pontos}')
				self.guarda.randomize()
				self.guarda.vida = 3

		
	def check_fail(self):
		#aqui verifica se a condicao onde o jogador "perde" é atendida e chama a funcoes game_over
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()
		
	
#essa parte do codigo basicamente configura algumas opcoes importantes para o codigo e que nao mudam nunca,
# devido a isso nao precisa estar em funcoes ou em classe e sempre sao executadas
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
#define o tamanho da celular e consequentimente o tamanho do mapa, podendo ser alterada se prefriri, porem deve-se alterar os tamanhos da sprites ja que eles nao estao diretamente relacionadas
cell_size = 43
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
pygame.display.set_caption("Dragon Rage")
comida = pygame.image.load('sprites/comida.png').convert_alpha()
size_h = comida.get_height()
size_w = comida.get_width()
apple = pygame.transform.scale(comida,(size_w/2 ,size_h/2))
guarda = pygame.image.load('sprites/guarda_real.png')
plano = pygame.image.load('sprites/portaa_f.png')
plano_de_fundo = pygame.transform.scale(plano, (cell_number * cell_size,cell_number * cell_size))
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,100)
main_game = MAIN()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if main_game.snake.direction.y != 1:
					main_game.snake.direction = Vector2(0,-1)
			if event.key == pygame.K_RIGHT:
				if main_game.snake.direction.x != -1:
					main_game.snake.direction = Vector2(1,0)
			if event.key == pygame.K_DOWN:
				if main_game.snake.direction.y != -1:
					main_game.snake.direction = Vector2(0,1)
			if event.key == pygame.K_LEFT:
				if main_game.snake.direction.x != 1:
					main_game.snake.direction = Vector2(-1,0)

	screen.fill((175,215,70))
	screen.blit(plano_de_fundo,(0,0))
	main_game.draw_elements()
	pygame.display.update()
