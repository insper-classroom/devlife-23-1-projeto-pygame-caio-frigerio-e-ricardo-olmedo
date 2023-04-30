import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
	def __init__(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)
		self.new_block = False
		self.remove_blocks = False

		self.head_up = pygame.image.load('sprites/assets_dragao/dragaoo_cab (4).png').convert_alpha()
		self.head_down = pygame.image.load('sprites/assets_dragao/dragaoo_cab (2).png').convert_alpha()
		self.head_right = pygame.image.load('sprites/assets_dragao/dragaoo_cab (5).png').convert_alpha()
		self.head_left = pygame.image.load('sprites/assets_dragao/dragaoo_cab (3).png').convert_alpha()
		
		self.tail_up = pygame.image.load('sprites/assets_dragao/rabo_d (4).jpeg').convert_alpha()
		self.tail_down = pygame.image.load('sprites/assets_dragao/rabo_d (2).jpeg').convert_alpha()
		self.tail_right = pygame.image.load('sprites/assets_dragao/rabo_d.jpeg').convert_alpha()
		self.tail_left = pygame.image.load('sprites/assets_dragao/rabo_d (3).jpeg').convert_alpha()

		self.body_vertical = pygame.image.load('sprites/assets_dragao/dragao_corpo (5).png').convert_alpha()
		self.body_horizontal = pygame.image.load('sprites/assets_dragao/dragao_corpo (4).png').convert_alpha()

		self.body_tr = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_e.png').convert_alpha()
		self.body_tl = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_e.png').convert_alpha()
		self.body_br = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_d.png').convert_alpha()
		self.body_bl = pygame.image.load('sprites/assets_dragao/dragao_corpo_vira_d.png').convert_alpha()


		

	def draw_snake(self):
		self.update_head_graphics()
		self.update_tail_graphics()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br,block_rect)

	def update_head_graphics(self):
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


	def draw_monster(self):
		guarda_react = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		if self.vivo == True:
			screen.blit(guarda,(guarda_react.x, guarda_react.y))
		
	def randomize(self):

		self.x = random.randint(0,cell_number - 3)
		self.y = random.randint(0,cell_number - 3)
		self.pos = Vector2(self.x,self.y)

	def barra_vida(self):
		guarda_react_bara = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		if self.vida == 2:
			screen.blit(self.barra_66,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		if self.vida == 3:
			screen.blit(self.barra_100,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		if self.vida == 1:
			screen.blit(self.barra_33,(guarda_react_bara.x - 104,guarda_react_bara.y + 50))
		


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
		self.msg.textos = (f'Wave 1, Mate o guarda!')
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

	def telas(self):
		if self.fase == 2:
			screen.blit(self.fase_2,(0,0))
		
	def game_over(self):
		self.snake.reset()

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()
		
		if self.snake.body[0] == self.guarda.pos:
			print(self.snake.body[0], '', self.guarda.pos)
			self.guarda.vida -=1
			self.msg.textos = (f'O GUARDA TEM {self.guarda.vida} de vida')
			print(self.guarda.vida)
			self.snake.remove_block()
			if self.guarda.vida == 0:
				
				self.fase = 2
				self.guarda.vivo = False
			
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