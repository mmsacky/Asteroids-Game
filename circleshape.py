import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        color_white = (255,255,255)
        pygame.draw.polygon(screen, color_white, self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, player):
        player_distance = player.position.distance_to(self.position)

        if player_distance <= player.radius + self.radius:
            return True
        return False