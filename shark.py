from enum import Enum
#Direction for the Shark
class Direction(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Shark:
  length = None
  direction = None
  body = None
  block_size = None
  color = (0,0,255)
  bounds = None

  def __init__(self, block_size, bounds):
    self.block_size = block_size
    self.bounds = bounds
    self.respawn()
#Appear at the beginning of the program, always heading to the RIGHT
  def respawn(self):
    self.length = 0.5
    self.body = [(20,20),(20,40),(20,60)]
    self.direction = Direction.RIGHT
   #Draw a Shark 
  def draw(self, game, window):
    for segment in self.body:
      game.draw.rect(window, self.color, (segment[0],segment[1],self.block_size, self.block_size))
      #Move the head and the whole body
  def move(self):
      curr_head = self.body[-1]
      if self.direction == Direction.DOWN:
        next_head = (curr_head[0], curr_head[1] + self.block_size)
        self.body.append(next_head)
      elif self.direction == Direction.UP:
        next_head = (curr_head[0], curr_head[1] - self.block_size)
        self.body.append(next_head)
      elif self.direction == Direction.RIGHT:
        next_head = (curr_head[0] + self.block_size, curr_head[1])
        self.body.append(next_head)
      elif self.direction == Direction.LEFT:
        next_head = (curr_head[0] - self.block_size, curr_head[1])
        self.body.append(next_head)
  
      if self.length < len(self.body):
        self.body.pop(0)
  def steer(self, direction):
      if self.direction == Direction.DOWN and direction != Direction.UP:
        self.direction = direction
      elif self.direction == Direction.UP and direction != Direction.DOWN:
        self.direction = direction
      elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
        self.direction = direction
      elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
        self.direction = direction
  #If the shark head  touch the food then the food will move to random position
  def check_for_food(self, food):
      head = self.body[-1]
      if head[0] == food.x and head[1] == food.y:
       
        food.respawn()
  
  
      #If the shark get out of the screen edge, return True, else return False
  def check_bounds(self):
      head = self.body[-1]
      if head[0] >= self.bounds[0]:
        return True
      if head[1] >= self.bounds[1]:
        return True
  
      if head[0] < 0:
          return True
      if head[1] < 0:
          return True  
  
      return False