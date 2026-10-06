from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        

    def draw(self, screen: pygame.Surface) -> None:
        position = self.position
        radius = self.radius
        pygame.draw.circle(screen, "white", position, radius, LINE_WIDTH)
        


    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            angle = random.uniform(20, 50)

            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = self.velocity * 1.2
            asteroid2.velocity = self.velocity * 1.2

