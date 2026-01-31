import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            pass
            if event.type == pygame.QUIT:
                return
                # pygame.quit()
                # exit()
        # log_state(screen)
        screen.fill('black')
        # player.draw(screen)
        for draw_object in drawable:
            draw_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # player.update(dt)
        # for updatable_object in updatable:
        #     updatable_object.update(dt)
        updatable.update(dt)
        for ansteroid in asteroids:
            if ansteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                # pygame.quit()
                # exit()
            for shot in shots:
                if ansteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    ansteroid.split()
                    shot.kill()
        # print(dt)
        # print(f"FPS: {clock.get_fps()}")
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
