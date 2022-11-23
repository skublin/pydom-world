import pygame


class Player:
    def __init__(self, name, position, width=64, height=64, sight_size=8, speed=2, image='player.png'):
        self.name = name
        self.position = position
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=self.position)
        self.direction = pygame.math.Vector2()
        # width, height necessary or get from self.rect (same situation with top_left)?
        self.player_width, self.player_height = width, height
        self.top_left = position[0] - self.player_width / 2, position[1] - self.player_height / 2
        self.sight_size = sight_size
        self.sight_offset = 4
        self.total_sight_load = self.sight_size + self.sight_offset
        self.speed = speed

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed
