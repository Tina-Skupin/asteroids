import sys
import pygame
import random
from constants import *
from player import Player
from shot import Shoot
from asteroid import Asteroid
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    shoots = pygame.sprite.Group()
    Shoot.containers = (shoots, updatable, drawable)



    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if CircleShape.collision(player, asteroid):
                print ("Game Over!")
                sys.exit()

            for shot in shoots:
                if CircleShape.collision(shot, asteroid):
                    shot.kill()
                    asteroid.split()
        #for asteroid in asteroids:
        #    for shots in shoots:
        #        if CircleShape.collision(shots, asteroid):
        #            asteroid.kill()


        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)  
  
        #screen.fill((0, 0, 0))
        #player.draw(screen)
        #player.update(dt)

        pygame.display.flip() 
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()