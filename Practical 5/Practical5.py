import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

class SolarSystem():
    def __init__(self):
        self.size = 1000
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
        self.ax.set_xlim(-self.size / 2, self.size / 2)
        self.ax.set_ylim(-self.size / 2, self.size / 2)
        self.ax.set_zlim(-self.size / 2, self.size / 2)

    def gravity_planets(self):
        for i, first in enumerate(self.planets):
            for second in self.planets[i+1:]:
                first.gravity(second)


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
            self . position[0] + self . velocity[0] * SolarSys . dT,
            self . position[1] + self . velocity[1] * SolarSys . dT,
            self . position[2] + self . velocity[2] * SolarSys . dT
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
        forceMag = self.mass * other.mass / (distanceMag**2)
        force = np.multiply(distanceUnit, forceMag)
        switch = 1
        #for body in self, other:
        if type(self) == Sun and type(other) == Planet:
            switch = 0
            acceleration = np.multiply(force, SolarSys.dT * switch)
            self.velocity = np.add(self.velocity, acceleration)
            switch = -1
            acceleration = np.multiply(force, SolarSys.dT * switch)
            other.velocity = np.add(other.velocity, acceleration)
        if type(self) == Sun and type(other) == Sun:
            switch = 1
            acceleration = np.multiply(force, SolarSys.dT * switch)
            self.velocity = np.add(self.velocity, acceleration)
            switch = -1
            acceleration = np.multiply(force, SolarSys.dT * switch)
            other.velocity = np.add(other.velocity, acceleration)
        if type(self) == Planet and type(other) == Planet:
            switch = 1
            acceleration = np.multiply(force, SolarSys.dT * switch)
            self.velocity = np.add(self.velocity, acceleration)
            switch = -1
            acceleration = np.multiply(force, SolarSys.dT * switch)
            other.velocity = np.add(other.velocity, acceleration)
        if type(self) == Planet and type(other) == Sun:
            switch = 1
            acceleration = np.multiply(force, SolarSys.dT * switch)
            self.velocity = np.add(self.velocity, acceleration)
            switch = 0
            acceleration = np.multiply(force, SolarSys.dT * switch)
            other.velocity = np.add(other.velocity, acceleration)


class Sun(Planet):
    def __init__(self,
                 SolarSys,
                 mass=1000,
                 position=(0, 0, 0),
                 velocity=(0, 0, 0)
    ):
        super(Sun, self).__init__(SolarSys, mass, position, velocity)
        self.color = 'yellow'

    #def move(self):
     #   self.position = self.position


def alignsuns(SolarSys, m1, m2, r, T):
    r1 = r * (m2/(m1+m2))*(m1+m2)/200
    r2 = r * (m1/(m1+m2))*(m1+m2)/200
    p1 = (r1, 0, 0)
    p2 = (-r2, 0, 0)
    v1 = (0, 1*np.pi*r1/T, 0)
    v2 = (0, -1*np.pi*r2/T, 0)
    sun = Sun(SolarSys, position=p1, velocity=v1, mass=m1)
    sun2 = Sun(SolarSys, position=p2, velocity=v2, mass=m2)
    return SolarSys

SolarSys = SolarSystem()
planet1 = Planet(SolarSys, mass=10, position=(300, 0, 0), velocity=(0, 3, 1.5))
planet2 = Planet(SolarSys, mass=10, position=(-300, 0, 0), velocity=(0, -3, -1.5))

#sun = Sun(SolarSys)
#sun2 = Sun(SolarSys, position=(100, 0, 0))
suns = alignsuns(SolarSys, 150, 150, 100, 25)


def animate(i):
    print('The frame is:', i)
    SolarSys.gravity_planets()
    SolarSys.update_planets()
    SolarSys.fix_axes()


anim = animation.FuncAnimation(SolarSys.fig, animate, frames=500, interval=100)

writervideo = animation.FFMpegWriter(fps=60)

anim.save("b2.mp4", writer=writervideo, dpi=200)
