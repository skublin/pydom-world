import random


class Game:
    def __init__(self):
        self.seeds = [random.randint(0, 999999), random.randint(0, 999999), random.randint(0, 999999)]
        self.map = Map(self.seeds)
        self.player = Player()
        self.world = World(self.map, self.player)