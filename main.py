import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0,0,0)
    fps = pygame.time.Clock()
    dt = 0 
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_types = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_types, updatable, drawable)
    AsteroidField.containers = (asteroid_field, updatable)
    Shot.containers = (shots, updatable, drawable)

    my_player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    my_asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

   
        pygame.Surface.fill(screen, black)
        for item in drawable:
            item.draw(screen)

        updatable.update(dt)

        for asteroid in asteroid_types:
            if asteroid.collision(my_player):
                print("Game over!") 
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()


        pygame.display.flip()

        fps.tick(60)
        dt = fps.get_time() / 1000       
        
if __name__ == "__main__":
    main()