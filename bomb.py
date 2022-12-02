class Bomb:
    block_size = None
    color = (0,255,0)
    x = 150; 
    y = 0; 

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))