# Configurações iniciais
import pygame
import random


'''
Snippet de código

classDiagram
    class Game {
        +run()
    }
    class Snake {
        -x: int
        -y: int
        -body: list
        +move()
        +grow()
        +check_collision()
    }
    class Food {
        -x: int
        -y: int
        +generate()
    }
    Game --> Snake
    Game --> Food
'''

import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)

# Tamanho do quadrado e velocidade do jogo
tamanho_quadrado = 20
velocidade_jogo = 15

class Snake:
    def __init__(self):
        self.x = largura // 2
        self.y = altura // 2
        self.body = []
        self.direction = pygame.K_RIGHT

    def move(self):
        # Adicione a nova posição da cabeça à lista do corpo
        self.body.append([self.x, self.y])

        # Atualize a posição da cabeça de acordo com a direção
        if self.direction == pygame.K_UP:
            self.y -= tamanho_quadrado
        elif self.direction == pygame.K_DOWN:
            self.y += tamanho_quadrado
        elif self.direction == pygame.K_LEFT:
            self.x -= tamanho_quadrado
        elif self.direction == pygame.K_RIGHT:
            self.x += tamanho_quadrado

        # Remova o último elemento da lista do corpo se a cobra não crescer
        self.body = self.body[-tamanho_cobra:]

    def grow(self):
        # Lógica de crescimento da cobra
        pass

    def check_collision(self):
        # Verifica se a cabeça da cobra colidiu com as paredes ou com o próprio corpo
        if self.x < 0 or self.x >= largura or self.y < 0 or self.y >= altura:
            return True
        if [self.x, self.y] in self.body[:-1]:
            return True
        return False

class Food:
    def __init__(self):
        self.x, self.y = self.generate()

    def generate(self):
        # Gera uma posição aleatória para a comida
        x = random.randint(0, (largura-tamanho_quadrado)//tamanho_quadrado) * tamanho_quadrado
        y = random.randint(0, (altura-tamanho_quadrado)//tamanho_quadrado) * tamanho_quadrado

        # Verifica se a nova posição não coincide com nenhum segmento da cobra
        while [x, y] in snake.body:
            x = random.randint(0, (largura-tamanho_quadrado)//tamanho_quadrado) * tamanho_quadrado
            y = random.randint(0, (altura-tamanho_quadrado)//tamanho_quadrado) * tamanho_quadrado

        return x, y

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.game_over = False

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    self.snake.change_direction(event.key)

            self.snake.move()
            self.check_collision()
            self.draw()
            pygame.display.update()
            pygame.time.Clock().tick(velocidade_jogo)

    def check_collision(self):
        if self.snake.check_collision():
            self.game_over = True
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.grow()
            self.food.generate()

    def draw(self):
        tela.fill(preto)
        for pixel in self.snake.body:
            pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado])
        pygame.draw.rect(tela, verde, [self.food.x, self.food.y, tamanho_quadrado, tamanho_quadrado])

if __name__ == "__main__":
    game = Game()
    game.run()