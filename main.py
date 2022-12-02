import pygame
from shark import *
from food import Food
from bomb import Bomb
class Controller:
  def __init__(self):
    pygame.init()
    self.bounds = (300,300)
    self.window = pygame.display.set_mode(self.bounds)
    pygame.display.set_caption("Shark")
    block_size = 20
    self.shark = Shark(block_size, self.bounds)
    self.food = Food(block_size,self.bounds)
    self.bomb = Bomb(block_size,self.bounds)
  def mainloop(self):
    font = pygame.font.SysFont('comicsans',60, True)
    self.run = True
    while self.run:
      pygame.time.delay(100)
    
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
      self.keys = pygame.key.get_pressed()
      if self.keys[pygame.K_LEFT]:
        self.shark.steer(Direction.LEFT)
      elif self.keys[pygame.K_RIGHT]:
        self.shark.steer(Direction.RIGHT)
      elif self.keys[pygame.K_UP]:
        self.shark.steer(Direction.UP)
      elif self.keys[pygame.K_DOWN]:
        self.shark.steer(Direction.DOWN)
      self.shark.move()
      self.shark.check_for_food(self.food)
      if self.shark.check_bounds() == True :
        self.text = font.render('Game Over', True, (255,255,255))
        self.window.blit(self.text, (20,120))
        pygame.display.update()
        pygame.time.delay(1000)
        self.shark.respawn()
        self.food.respawn()
      self.window.fill((0,0,0))
      self.shark.draw(pygame, self.window)
      self.food.draw(pygame, self.window)
      self.bomb.draw(pygame, self.window)
      pygame.display.update()
        
    
   
  
      
    
    
    
    
  #def drawshark(self):
    #shark=pygame.rect(self.pos.x*self)
  
def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()
    
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

