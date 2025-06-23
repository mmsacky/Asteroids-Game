import pygame
from constants import *
from player import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0,0,0)
    fps = pygame.time.Clock()
    dt = 0 
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    my_player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

   
        pygame.Surface.fill(screen, black)
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        pygame.display.flip()

        fps.tick(60)
        dt = fps.get_time() / 1000
        # print(fps , dt)

        
        
if __name__ == "__main__":
    main()