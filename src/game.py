import pygame
import sys
from math import sqrt
from map import Map
from player import Player


class Game:
    def __init__(self, world_size):
        # 2 * tile-size * map-size
        self.world_size = world_size
        self.size = (self.width, self.height) = (1024, 1024)
        self.white = (255, 255, 255)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Some experiments with maps in Pygame")
        self.m = Map(self.world_size)
        self.map = self.m.map
        self.player = Player('Testy', (512, 512))
        self.colors = {'-2': (255, 255, 255), '-1': (42, 128, 148), '0': (146, 168, 172), '1': (194, 148, 12),
                       '2': (150, 164, 38), '3': (86, 178, 106), '4': (36, 114, 94), '5': (32, 78, 42)}

    def run(self):
        pygame.init()
        pygame.event.set_grab(True)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            # fill screen with color
            self.screen.fill(self.colors['-1'])
            # show tiles - map
            # self.map.draw_tiles()
            # self.map.hex_tiles(4)
            # update screen
            self.draw_hex_tiles(16)
            self.player.update()
            self.screen.blit(self.player.image, self.player.rect.center)
            pygame.display.update()

    def draw_hex_tiles(self, size):
        def calculate_corners(c):
            x, y = c
            # corners: c0, c1, c2, c3, c4, c5
            return [(x, y + size), (x + sqrt(3) * 0.5 * size, y + 0.5 * size),
                    (x + sqrt(3) * 0.5 * size, y - 0.5 * size), (x, y - size),
                    (x - sqrt(3) * 0.5 * size, y - 0.5 * size), (x - sqrt(3) * 0.5 * size, y + 0.5 * size)]
        w, h = sqrt(3) * size, 2 * size
        start_center = (0.5 * w, 1.5 * size)
        for i in range(self.world_size):
            for j in range(self.world_size):
                if self.map[i][j] > -1:
                    # should look like that -> center = (center[i][j][0], center[i][j][1])    (!)
                    center = (start_center[0] + j * w, start_center[1] + i * 0.75 * h)
                    if not i % 2 == 0:
                        center = (center[0] + 0.5 * w, center[1])
                    # fill insides of tiles with color
                    pygame.draw.polygon(self.screen, self.colors[str(int(self.map[i][j]))], calculate_corners(center), 0)
                    # draw black borders of tiles
                    pygame.draw.polygon(self.screen, (0, 0, 0), calculate_corners(center), 1)
                elif self.map[i][j] == -2:
                    center = (start_center[0] + j * w, start_center[1] + i * 0.75 * h)
                    if not i % 2 == 0:
                        center = (center[0] + 0.5 * w, center[1])
                    pygame.draw.polygon(self.screen, self.colors[str(int(self.map[i][j]))], calculate_corners(center), 0)
            # add option for water and ice    (!)


if __name__ == '__main__':
    s = int(input('World size: '))
    g = Game(s)
    # g.map.show_map()
    g.run()
