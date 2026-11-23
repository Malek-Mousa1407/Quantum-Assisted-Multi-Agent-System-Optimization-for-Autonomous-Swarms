class Environment:
    
    def __init__(self, width, height, obstacles: list):
        self.width = width
        self.height = height
        
        if obstacles:
            self.obstacles = set(obstacles)
        else:
            set()

    def is_valid_posistion(self, position: tuple) :
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, position: tuple) :
        return self.is_valid_posistion(position) and position not in self.obstacles