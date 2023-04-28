import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
	def __init__(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)
		self.new_block = False

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
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True

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
		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)

class GUARDA:
	def __init__(self):
		self.randomize()
		self.vida = 3


	def draw_monster(self):
		guarda_react = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(guarda,guarda_react)
	def randomize(self):

		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)


class MAIN:
	def __init__(self):
		self.snake = SNAKE()
		self.fruit = FRUIT()
		self.guarda = GUARDA()
	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()

	def draw_elements(self):
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.guarda.draw_monster()
		
	

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()
		
		if self.snake.body[0] == self.guarda.pos:
			self.guarda.vida -=1
			self.guarda.randomize()
			print(self.guarda.pos)

		if self.guarda.vida == 0:
			fase = True
			

		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	def check_fail(self):
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()
		
	def game_over(self):
		self.snake.reset()




pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 50
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
pygame.display.set_caption("Jogo Dragao")
clock = pygame.time.Clock()
apple = pygame.image.load('sprites/apple.png').convert_alpha()
guarda = pygame.image.load('sprites/guarda_real.png')
#plano_de_fundo = pygame.transform.scale(guarda_def,)
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