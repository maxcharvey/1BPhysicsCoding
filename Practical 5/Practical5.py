import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


class SolarSystem():
    def __init__(self):
        self.size = 10000
        self.planets = []
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.dT = 1

    def new_planet(self, planet):
        self.planets.append(planet)

    def update_planets(self):
        self.ax.clear()
        for planet in self.planets:
            planet.move()
            planet.draw()

    def fix_axes(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))

    def gravity_planets(self):
        for i, first in enumerate(self.planets):
            for second in self.planets[i + 1:]:
                first.gravity(second)


class Planet():
    def __init__(self,
                 SolarSys,
                 mass,
                 position=(0, 0, 0),
                 velocity=(0, 0, 0)
                 ):
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
            acceleration = np.divide(force, body.mass)
            acceleration = np.multiply(force, SolarSys.dT * switch)
            body.velocity = np.add(body.velocity, acceleration)
            switch *= -1


class Sun(Planet):
    def __init__(self,
                 SolarSys,
                 mass=1000,
                 position=(0, 0, 0),
                 velocity=(0, 0, 0)
                 ):


        super(Sun, self).__init__(SolarSys, mass, position, velocity)
        self.color = 'yellow'

    def move(self):
        self.position = self.position

SolarSys = SolarSystem()

# star1 = Sun(SolarSys, position=(25, 0, 0), velocity=(0, -5, -5))
# star2 = Sun(SolarSys, position=(-25, 0, 0), velocity=(0, 5, 5))

planet1 = Planet(SolarSys, mass=10, position=(300, 50, 0), velocity=(0, 5, 5))
planet2 = Planet(SolarSys, mass=10, position=(100, -300, 150), velocity=(5, 0, 0))
planet3 = Planet(SolarSys, mass=10, position=(-300, -50, 150), velocity=(-4, 0, 0))


sun = Sun(SolarSys)


def animate(i):
    print('The frame is:', i)
    SolarSys.gravity_planets()
    SolarSys.update_planets()
    SolarSys.fix_axes()


anim = animation.FuncAnimation(SolarSys.fig, animate, frames=100, interval=100)

writervideo = animation.FFMpegWriter(fps=60)

anim.save("binary_animation.mp4", writer=writervideo, dpi=200)
