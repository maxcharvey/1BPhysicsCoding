import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm


class Canvas():
    def __init__(self):
        self.size = 20
        self.blocks = []
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.collision_counter = 0

    def add_block(self, block):
        self.blocks.append(block)

    def update_blocks(self):
        self.ax.clear()
        for i, block in enumerate(self.blocks):
            block.move()
            block.draw()

    def fix_axes(self):
        self.ax.set_xlim(-self.size / 2, self.size / 2)
        self.ax.set_zlim(-self.size / 2, self.size / 2)
        self.ax.set_ylim(-self.size / 2, self.size / 2)

    def check_collision(self):
        combinations = list(itertools.combinations(range(len(self.blocks)), 2))

        for pair in combinations:
            if abs(self.blocks[pair[0]].position - self.blocks[pair[1]].position) < 0.1:
                self.collision_counter += 1
                self.blocks[pair[0]].collide(self.blocks[pair[1]])


class Block():
    def __init__(self,
                 canvas,
                 recip_mass,
                 position=0,
                 velocity=0
                 ):
        self.canvas = canvas
        self.recip_mass = recip_mass
        self.position = position
        self.velocity = velocity
        self.canvas.add_block(self)
        self.color = 'black'

    def move(self):
        self.position = self.position + self.velocity

    def draw(self):
        canvas.ax.plot(self.position, 0, "o")

    def collide(self, other):
        # This was the original one where it would just reverse the direction of the velocity during a collision
        # if abs(self.position - other.position) < 0.1:
        # self.velocity *= -1
        # other.velocity *= -1
        if abs(self.position - other.position) < 0.1:
            # Defining our collision velocities for use within the following equations
            v1 = self.velocity
            v2 = other.velocity
            m1 = self.recip_mass
            m2 = other.recip_mass
            # Now generate the equations but in terms of inverse masses
            v1_new = v1 * (m2 - m1) / (m1 + m2) + (2 * v2 * m1) / (m1 + m2)
            v2_new = (2 * v1 * m2) / (m1 + m2) - v2 * (m2 - m1) / (m1 + m2)
            # Then get back to desired outputs - dummy variables required to prevent assignment happening before both
            # equations had been constructed
            self.velocity = v1_new
            other.velocity = v2_new


canvas = Canvas()

# Input the block masses here so that the class will convert and take inputs of inverse mass not absolute mass
# If you need

block1_mass = 1
block2_mass = 1
block3_mass = 10
block4_mass = 5

wall1 = Block(canvas, recip_mass=0, position=0, velocity=0)
block2 = Block(canvas, recip_mass=1 / block2_mass, position=0.5, velocity=-0)
block3 = Block(canvas, recip_mass=1 / block3_mass, position=1, velocity=-0.05)
block4 = Block(canvas, recip_mass=1 / block4_mass, position=2, velocity=-0.1)

collisions = []

no_frames = 1000
progress = tqdm(total=no_frames)


def animate(i):
    # print("The frame is: ", i)
    canvas.update_blocks()
    canvas.check_collision()
    canvas.fix_axes()
    collisions.append(canvas.collision_counter)
    progress.update(1)
    if i == no_frames - 1:
        progress.close()


anim = animation.FuncAnimation(canvas.fig, animate, frames=no_frames, interval=0.0001)

writervideo = animation.FFMpegWriter(fps=60)

anim.save("block.mp4", writer=writervideo, dpi=300)

print(f'The number of collisions occurring was {collisions[-1]}')
