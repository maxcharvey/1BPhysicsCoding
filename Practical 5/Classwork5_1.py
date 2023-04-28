import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


class SolarSystem():
    def __init__(self):
        self.size = 100000
        self.stars = []
        self.planets = []
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.dT = 1

    def new_star(self, star):
        self.stars.append(star)

    def new_planet(self, planet):
        self.planets.append(planet)

    def update_stars(self):
        self.ax.clear()
        for star in self.stars:
            star.move()
            star.draw()

    def update_planets(self):
        self.ax.clear()
        for planet in self.planets:
            planet.move()
            planet.draw()

    def fix_axes(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))

    def gravity_stars(self):
        for i, first in enumerate(self.stars):
            for second in self.stars[i + 1:]:
                first.gravity(second)

    def gravity_planets(self):
        for planet in self.planets:
            for star in self.stars:
                planet.gravity(star)
                for other_planet in self.planets:
                    if other_planet != planet:
                        planet.gravity(other_planet)

class Planet():
    def __init__(self, SolarSys, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        self.SolarSys = SolarSys
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.SolarSys.new_planet(self)
        self.color = 'black'

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0] * SolarSys.dT,
            self.position[1] + self.velocity[1] * SolarSys.dT,
            self.position[2] + self.velocity[2] * SolarSys.dT
        )

    def draw(self):
        self.SolarSys.ax.plot(
            *self.position,
            marker="o",
            markersize=10,
            color=self.color
        )

    def gravity(self, other):
        distance = np.subtract(other.position, self.position)
        distanceMag = np.linalg.norm(distance)
        distanceUnit = np.divide(distance, distanceMag)
        forceMag = self.mass * other.mass / (distanceMag ** 2)
        force = np.multiply(distanceUnit, forceMag)
        switch = 1
        for body in self, other:
            acceleration = np.multiply(force, SolarSys.dT * switch)
            body.velocity = np.add(body.velocity, acceleration)
            switch *= -1


class Star(Planet):
    def __init__(self,
                 SolarSys,
                 mass=10000,
                 position=(0, 0, 0),
                 velocity=(0, 0, 0)
                 ):
        super(Star, self).__init__(SolarSys, mass, position, velocity)
        self.color = 'yellow'

    def move(self):
        self.position = self.position


def alignsuns(m1, m2, r, t):
    r1 = r * (m2 / (m1 + m2))
    r2 = r * (m1 / (m1 + m2))
    p1 = (r1, 0, 0)
    p2 = (-r2, 0, 0)
    v1 = (0, 2 * np.pi * r1 / t, 0)
    v2 = (0, -2 * np.pi * r2 / t, 0)
    return p1, p2, v1, v2


SolarSys = SolarSystem()

planet1 = Planet(SolarSys, mass=0.1, position=(4000, 0, 0), velocity=(0, 0, 0))
planet2 = Planet(SolarSys, mass=0.1, position=(-4000, 0, 0), velocity=(0, 0, 0))

data = alignsuns(10000, 10000, 4000, 1000)
sun1 = Star(SolarSys, position=data[0], velocity=data[2])
sun2 = Star(SolarSys, position=data[1], velocity=data[3])


def animate(j):
    SolarSys.gravity_planets()
    #SolarSys.gravity_stars()
    SolarSys.update_planets()
    #SolarSys.update_stars()
    SolarSys.fix_axes()


anim = animation.FuncAnimation(SolarSys.fig, animate, frames=500, interval=100)

writervideo = animation.FFMpegWriter(fps=60)

anim.save("binary2.mp4", writer=writervideo, dpi=200)
