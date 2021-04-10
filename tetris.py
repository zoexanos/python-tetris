import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""



#GLOBAL VARIABLES
s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
      ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
      ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
      '.00..',
      '.00..',
      '.....',
      '.....']]

O = [['.....',
      '.00..',
      '.00..',
      '.....',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
      ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
      ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
      ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0,255,0), (255,0,0), (0,255,255), (255,255,0), (255,165,0), (0,0,255), (128,0,128)]
#index 0 - 6 represent shape

class Piece(object):
  def __init__(self, x, y, shape):
    self.x = x
    self.y = y
    self.shape = shape
    self.color = shape_colors[shape.index(shape)]
    self.rotation = 0

def create_grid(locked_positions = {}):
  grid = [[(0,0,0) for x in range(10)] for x in range(20)]
  for i in range(len(grid)):
    for j in range(len(grid[1])):
      if (j, i) in locked_positions:
        c = locked_positions[(j,i)]
        grid[i][j] = c
  return grid



def convert_shape_format(shape):
  pass

def valid_space(shape, grid):
  pass

def check_lost(positions):
  pass

def get_shape():
  return random.choice(shapes)

def draw_text_middle(text, size, color, surface):
  pass

def draw_grid(surface):
  surface.fill((0,0,0))
  pygame.font.init() 
  font = pygame.font.SysFont('comicsans', 60)
  label = font.render('Tetris', 1, (255, 255, 255))

  surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2, 30)))

  for i in range(len(grid)):
    for j in range(len(grid[i])):
      pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)
  
  pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)


def clear_rows(grid, locked):
  pass

def draw_next_shape(shape, surface):
  pass

def draw_window(surface, grid):
  surface.fill((0,0,0))
  pygame.font.init() 
  font = pygame.font.SysFont('comicsans', 60)
  label = font.render('Tetris', 1, (255, 255, 255))

  surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2, 30)))
  draw_grid(surface, grid)
  pygame.display.update()

def main():
  locked_positions = {}

def main_menu():
  pass

main_menu()