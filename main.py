import matplotlib.pyplot as plt
x = 1000 #horionztal position from origin
y = 0 #vertical position from origin
vx = 0 #horizontal velocity
r = (x**2 + y**2)**0.5
dt = 0.01 #seconds per step
steps = 100000

G = 100 #gravitational constant controls strength of gravity
M = 1000 #mass of object at origin 0, 0 could be earth or another planet
vy = (G*M/r)**0.5 #verical velocity and can be a value like vx but less accurate

#store positions for graphing
x_positions = []
y_positions = []

for step in range(steps): #seconds simulated
    #distance from satellite to center | pythagorean (y->x)^2 * (origin->y)^2 = (satellite->origin)^2
    r = (x**2 + y**2)**0.5

    #acceleration due to gravity, how strong the pull is (how quick the velocity changes)
    a = G*M / r**2

    #- pulls down/left toward center
    #x/r and y/r is how much you need to go in those directions
    ax = -a * (x/r) #acceleration horiozntally toward origin
    ay = -a * (y/r) #acceleration vertically toward origin

    #affected by acceleration, in all speed plus effect of gravity
    vx += ax * dt
    vy += ay * dt

    #orbit curves because velocity keeps changing due to acceleration
    x = x + vx * dt
    y = y + vy * dt

    x_positions.append(x)
    y_positions.append(y)

plt.plot(x_positions, y_positions)
plt.scatter(0, 0, color='red', s=100)
plt.xlabel("X position")
plt.ylabel("Y positions")
plt.title("Orbit Simulation")
plt.axis('equal')
plt.show()