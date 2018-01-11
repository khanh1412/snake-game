import pygame
import random
import pygame
from pygame.locals import *

class snake:
  def __init__(self, points, velocity):
    self.points = points
    self.velocity = velocity
    self.head = points[-1]
    self.tail = points[0]

  def move(self):
    if self.velocity == "right":
      new_point = self.head[0] + 1 , self.head[1]
    elif self.velocity == "left":
      new_point = self.head[0] - 1 , self.head[1]
    elif self.velocity == "up":
      new_point = self.head[0] , self.head[1] - 1
    elif self.velocity == "down":
      new_point = self.head[0] , self.head[1] + 1
    else:
      new_point = self.head
    new_points = self.points[1:] + [new_point]
    new_velocity = self.velocity
    return snake(new_points, new_velocity)

  def eat(self):
    new_points = [self.tail] + self.move().points
    new_velocity = self.velocity
    return snake(new_points, new_velocity)

  def die(self):
    if self.head in self.points[:-2]:
      return True
    if self.head[0] == -1 or self.head[0] == 40:
      return True
    if self.head[1] == -1 or self.head[1] == 30:
      return True
    return False

  def direction(self):
    if self.head[0] - self.points[-2][0] == 1:
      return "right"
    if self.head[0] - self.points[-2][0] == -1:
      return "left"
    if self.head[1] - self.points[-2][1] == 1:
      return "down"
    if self.head[1] - self.points[-2][1] == -1:
      return "up"



def draw(screen, mysnake, apple, dead = False):
  background_color = (255,255,255)
  snake_color = (0,0,0)
  apple_color = (0,255,0)
  head_color = (255,0,0)
  if dead == True:
      background_color = (255,255,255)
      snake_color = (255,0,0)
      apple_color = (0,255,0)
      head_color = (255,0,0)
  screen.fill(background_color)

  for point in mysnake.points:
    x0, y0 = point
    x, y = 20*x0, 20*y0
    pygame.draw.rect(screen, snake_color, (x,y,20,20), 0)

  x0, y0 = apple
  x, y = 20*x0+10, 20*y0+10
  pygame.draw.circle(screen, apple_color, (x,y), 10, 0)

  x0, y0 = mysnake.head
  x, y = 20*x0, 20*y0
  pygame.draw.rect(screen, head_color, (x,y,20,20), 0)


  pygame.display.update()
  
def main():
  x0, y0 = random.randrange(10,30),random.randrange(10,20)
  mysnake = snake([(x0-1, y0),(x0,y0)], velocity = "right")
  pygame.init()
  screen = pygame.display.set_mode((800,600))
  t0 = pygame.time.get_ticks()

  apple = (random.randrange(5,35),random.randrange(5,25))
  while mysnake.die() == False:
    draw(screen, mysnake, apple)
    if pygame.time.get_ticks() - t0 > 300:
      mysnake = mysnake.move()
      t0 = pygame.time.get_ticks()
      if mysnake.head == apple:
        mysnake = mysnake.eat()
        apple = (random.randrange(5,35),random.randrange(5,25))

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()
      if event.type == KEYDOWN:
        if event.key == 273 and mysnake.direction() != "down":
          mysnake.velocity = "up"
        elif event.key == 274 and mysnake.direction() != "up":
          mysnake.velocity = "down"
        elif event.key == 275 and mysnake.direction() != "left":
          mysnake.velocity = "right"
        elif event.key == 276 and mysnake.direction() != "right":
          mysnake.velocity = "left"
        else:
          pass
  print("dead")

  draw(screen, mysnake, apple, True)
  pygame.time.delay(1000)
  main()











if __name__ == "__main__":
  main()













