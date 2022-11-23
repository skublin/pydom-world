import random
import numpy as np
import matplotlib.pyplot as plt
from noise import snoise3


"""
Biomes:
    -> 0 - Snow
    -> 1 - Grass
    -> 2 - Forest
    -> 3 - Dark Forest
    -> 4 - Jungle
    -> 5 - Desert
    -> 6 - Tundra
    -> 7 - Scorched
"""


class Map:
    def __init__(self, world_size: int):
        # TODO: make matrix with tuples (x, y) - centers of tiles
        self.world_size = world_size
        self.offset = 4
        self.total_size = self.world_size + self.offset * 2
        self.start_matrix = np.zeros((self.total_size, self.total_size), dtype=int) - 1
        self.colors = {'0': (255, 255, 255), '1': (0, 170, 0), '2': (0, 140, 0), '3': (0, 100, 0),
                       '4': (0, 70, 0), '5': (200, 190, 0), '6': (140, 0, 0), '7': (80, 40, 0)}
        self.initial_map = self.generate_land()
        # self.biomes = self.create_biomes()
        # self.map = finish_map()    (?)
        self.map = self.create_biomes()

    def generate_land(self):
        nm = self.noise_map()
        nm[nm < -0.25] = -1  # -1 is value for water
        nm[nm >= -0.4] = 1  # 1 is value for land
        lower = self.total_size // 2 - (self.world_size // 2)
        upper = (self.total_size // 2) + (self.world_size // 2)
        self.start_matrix[lower:upper, lower:upper] = nm
        # plt.matshow(self.start_matrix)
        # plt.show()
        return self.start_matrix

    def noise_map(self, octaves=1, persistence=0.5, lacunarity=2.0, offset=0):
        scale = self.world_size / 2
        seed = random.randint(1, 999999)
        noise_map = np.array([[snoise3(x / scale, y / scale, seed,
                               octaves=octaves, persistence=persistence, lacunarity=lacunarity)
                               for x in range(self.world_size + offset)] for y in range(self.world_size + offset)])
        return noise_map

    def create_biomes(self):
        # if water and low temperature -> ice tiles (?)
        # biomes: tundra -> 0, desert -> 1, savanna -> 2, forest -> 3, taiga -> 4, jungle -> 5
        # water -> -1, ice -> -2
        temperature = self.noise_map(offset=self.offset * 2)
        humidity = self.noise_map(offset=self.offset * 2)
        biomes = np.zeros((self.total_size, self.total_size))
        for i in range(self.total_size):
            for j in range(self.total_size):
                biomes[i][j] = -1 if self.initial_map[i][j] == -1 else biomes[i][j]
                biomes[i][j] = -2 if biomes[i][j] == -1 and temperature[i][j] < -0.5 else biomes[i][j]
                if not biomes[i][j] < 0:
                    biomes[i][j] = 0 if temperature[i][j] > -0.4 and humidity[i][j] <= -0.5 else biomes[i][j]
                    biomes[i][j] = 1 if temperature[i][j] < -0.4 and humidity[i][j] < 0 else biomes[i][j]
                    biomes[i][j] = 2 if temperature[i][j] > -0.4 and -0.5 < humidity[i][j] <= 0 else biomes[i][j]
                    biomes[i][j] = 3 if temperature[i][j] > -0.4 and 0 < humidity[i][j] <= 0.5 else biomes[i][j]
                    biomes[i][j] = 4 if temperature[i][j] < -0.4 and humidity[i][j] > 0 else biomes[i][j]
                    biomes[i][j] = 5 if temperature[i][j] > -0.4 and humidity[i][j] > 0.5 else biomes[i][j]
        return biomes

    def draw_tile(self, position):
        pygame.draw.polygon(self.surface, self.colors['1'], calculate_corners(position), 1)


if __name__ == '__main__':
    m = Map(32)
    m.create_biomes()
