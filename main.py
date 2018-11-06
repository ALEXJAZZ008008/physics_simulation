import time
import random
import matplotlib.pyplot
import mpl_toolkits.mplot3d
import vector2d
import vector3d
import ball
import box


gravitational_acceleration = vector3d.Vector3D(0, -9.8, 0)

room = box.Box(vector3d.Vector3D(-5, -5, -5), vector3d.Vector3D(5, 5, 5), 0.8, 0.2)
balls = []

for i in range(2):
    balls.append(ball.Ball(vector3d.Vector3D(random.uniform(room.origin.x, room.limit.x),
                                             random.uniform((room.limit.y + room.origin.y) * 0.5, room.limit.y),
                                             random.uniform(room.origin.z, room.limit.z)),
                           vector3d.Vector3D(random.uniform(-room.limit.x, room.limit.x) * 2,
                                             random.uniform(0, room.limit.y) * 2,
                                             random.uniform(-room.limit.z, room.limit.z) * 2),
                           gravitational_acceleration, 1, 1, 0.8, 0.2))

moving = []

for i in balls:
    moving.append(True)

previous_time = time.time()

while any(moving):
    current_time = time.time()
    delta_time = current_time - previous_time

    for i, ball in enumerate(balls):
        if moving[i]:
            ball.update(delta_time, room)

            moving[i] = ball.moving

    previous_time = current_time

figure = matplotlib.pyplot.figure()
plot = figure.add_subplot(111, projection="3d")

for ball in balls:
    ball.convert_path()
    plot.plot(ball.x_path, ball.z_path, ball.y_path)

plot.set_xlim(room.origin.x, room.limit.x)
plot.set_ylim(room.origin.y, room.limit.y)
plot.set_zlim(room.origin.z, room.limit.z)

matplotlib.pyplot.show()
