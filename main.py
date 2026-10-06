import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print(f"Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt: float = 0.0

    

    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)

        for object in asteroids:
            if player.collides_with(object):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                return True

        for astroid in asteroids:
            for bullet in shots:
                if astroid.collides_with(bullet):
                    log_event("asteroid_shot")
                    astroid.split()
                    bullet.kill()



        for d in drawable:
            d.draw(screen)
             
            
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        dt = clock.tick(60) / 1000
        print(dt)
    


if __name__ == "__main__":
    main()
