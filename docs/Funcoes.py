import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
	def __init__(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)
		self.new_block = False
		self.remove_blocks = False
		imagemup = pygame.image.load('sprites/assets_dragao/dragaoo_cab (4).png').convert_alpha()
		
		imagemdown = pygame.image.load('sprites/assets_dragao/dragaoo_cab (2).png').convert_alpha()
		imagemright=pygame.image.load('sprites/assets_dragao/dragaoo_cab (5).png').convert_alpha()
		imagemleft = pygame.image.load('sprites/assets_dragao/dragaoo_cab (3).png').convert_alpha()
        

        
		self.head_up = pygame.transform.scale(imagemup, (90, 80))
		self.head_down = pygame.transform.scale(imagemdown, (90, 80))
		self.head_right = pygame.transform.scale(imagemright, (80, 90))
		self.head_left = pygame.transform.scale(imagemleft, (80, 90))
		
		rabobaixo= pygame.image.load('sprites/assets_dragao/rabobaixo removebg.png').convert_alpha()
		size_ww = rabobaixo.get_width()
		size_hh = rabobaixo.get_height()
		rabocima = pygame.image.load('sprites/assets_dragao/rabocima-removebg-preview.png').convert_alpha()
		raboesquerda = pygame.image.load('sprites/assets_dragao/raboesqeurda-removebg-preview.png').convert_alpha()
		rabodireita = pygame.image.load('sprites/assets_dragao/rabodireita-removebg-preview.png').convert_alpha()
		self.tail_up =  pygame.transform.scale(rabobaixo, (size_ww/3, size_hh/3))
		self.tail_down = pygame.transform.scale(rabocima, (size_ww/3, size_hh/3))
		self.tail_right = pygame.transform.scale(raboesquerda, (size_ww/3, size_hh/3))
		self.tail_left = pygame.transform.scale(rabodireita, (size_ww/3, size_hh/3))

		
        
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
		self.update_head_graphics()
		self.update_tail_graphics()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size )
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos ,y_pos,cell_size,cell_size)

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

	def update_head_graphics(self):
		if len(self.body) == 0:
			print('game over')
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	def update_tail_graphics(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def move_snake(self):
		if self.remove_blocks == True:
			body_copy = self.body[:-1]
			print(body_copy)
			body_copy.remove(body_copy[-1])
			print(body_copy)
			self.body = body_copy[:]
		
			self.remove_blocks = False
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
			else:
				print("tela game over")

	def add_block(self):
		self.new_block = True

	def remove_block(self):
		self.remove_blocks = True

	def play_crunch_sound(self):
		pass
		#self.crunch_sound.play()

	def reset(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)


class FRUIT:
	def __init__(self):
		self.randomize()

	def draw_fruit(self):
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(apple,fruit_rect)

	def randomize(self):
		self.x = random.randint(0,cell_number - 4)
		self.y = random.randint(0,cell_number - 4)
		self.pos = Vector2(self.x,self.y)

class GUARDA:
	def __init__(self):
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
		self.vivo = True
    	
	def randomize(self):

		self.x = random.randint(0,cell_number - 3)
		self.y = random.randint(0,cell_number - 3)
		self.pos = Vector2(self.x,self.y)

	def draw_monster(self):
		guarda_react = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		if self.vivo == True:
			screen.blit(guarda,(guarda_react.x, guarda_react.y))
		
	def barra_vida(self):
		guarda_react_bara = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		if self.vida == 2:
			screen.blit(self.barra_66,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		if self.vida == 3:
			screen.blit(self.barra_100,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		if self.vida == 1:
			screen.blit(self.barra_33,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		
class PONTO:
	def __init__(self):
		self.pontos = 0

class TEXTO:
	def __init__(self):
		pygame.font.init()
		self.fonte = pygame.font.SysFont("arial", 50)
		self.textos = ""
			
	def imprimir(self):
		impre = self.fonte.render(self.textos, 1,(255,255,255))
		screen.blit(impre, (220,40))
		pygame.display.update()

class MAIN:
	def __init__(self):
		self.snake = SNAKE()
		self.fruit = FRUIT()
		self.guarda = GUARDA()
		self.msg = TEXTO()
		self.pontos = PONTO()
		self.msg.textos = (f'Mate o guarda! & faca pontos!')
		self.fase = 1
		self.fase_2 = pygame.image.load('sprites/fundo2.png').convert_alpha()
	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()

	def draw_elements(self):
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.guarda.draw_monster()
		self.msg.imprimir()
		self.guarda.barra_vida()



	def game_over(self):
		self.snake.reset()

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()
			self.pontos.pontos += 10
		
		if self.snake.body[0] == self.guarda.pos:
			print(self.snake.body[0], '', self.guarda.pos)
			self.guarda.vida -=1
			
			print(self.guarda.vida)
			self.snake.remove_block()
			if self.guarda.vida == 0:
				self.pontos.pontos *=2
				self.fase = 2
				self.guarda.randomize()
				self.guarda.vida = 3
				self.guarda.vivo = True
			
		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	def check_fail(self):
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()
		
	




pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 50
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
pygame.display.set_caption("Jogo Dragao")
clock = pygame.time.Clock()
comida = pygame.image.load('sprites/comida.png').convert_alpha()
size_h = comida.get_height()
size_w = comida.get_width()
apple = pygame.transform.scale(comida,(size_w/2 ,size_h/2))


guarda = pygame.image.load('sprites/guarda_real.png')

plano = pygame.image.load('sprites/portaa_f.png')
plano_de_fundo = pygame.transform.scale(plano, (cell_number * cell_size,cell_number * cell_size))


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
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
	clock.tick(60)