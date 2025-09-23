import pygame
import random

class Particle:
    def __init__(self, pos, vel, radius):
        """
        pos: [x, y] starting position (float or int)
        vel: [vx, vy] velocity
        radius: starting radius (float)
        """
        self.x, self.y = pos
        self.vx, self.vy = vel
        self.radius = radius

    def update(self, decay=0.3):
        """
        Update position, radius etc.
        Returns False if particle is “dead” (radius ≤ 0), else True.
        """
        self.x += self.vx
        self.y += self.vy
        self.radius -= decay
        if self.radius <= 0:
            return False
        return True

    def draw(self, surface, color=(random.randint(20,250),random.randint(20,250),random.randint(20,250))):
        """
        Draw this particle on given surface.
        """
        # convert pos & radius to ints for consistent drawing
        pos_int = (int(self.x), int(self.y))
        radius_int = max(1, int(self.radius))
        pygame.draw.circle(surface, color, pos_int, radius_int, 0)  # filled circle
print("Loaded")
class Particle_System:
    def __init__(self, surface, pos_getter, color=(255,255,255),
                 radius_range=(5,20), vel_range_x=(-1,4), vel_range_y=(-2,2),
                 decay=0.3):
        """
        surface: pygame surface to draw on
        pos_getter: function or callable returning current position (x, y)
                    e.g. pygame.mouse.get_pos or a lambda
        color: color of particles
        radius_range: (min, max) starting radius
        vel_range_x: (min, max) horizontal velocity
        vel_range_y: (min, max) vertical velocity
        decay: how much radius reduces per update
        """
        self.surface = surface
        self.pos_getter = pos_getter
        self.color = color
        self.radius_range = radius_range
        self.vel_range_x = vel_range_x
        self.vel_range_y = vel_range_y
        self.decay = decay
        self.particles = []

    def emit(self):
        """
        Add a new particle at the current pos
        """
        mx, my = self.pos_getter()
        # random velocity
        vx = random.randint(self.vel_range_x[0], self.vel_range_x[1])
        vy = random.randint(self.vel_range_y[0], self.vel_range_y[1])
        radius = random.uniform(self.radius_range[0], self.radius_range[1])
        p = Particle(pos=[mx, my], vel=[vx, vy], radius=radius)
        self.particles.append(p)

    def update_and_draw(self):
        """
        Update all particles, draw them, and remove dead ones.
        """
        # iterate over a copy so removal is safe
        for p in self.particles[:]:
            alive = p.update(decay=self.decay)
            if alive:
                p.draw(self.surface, self.color)
            else:
                self.particles.remove(p)







