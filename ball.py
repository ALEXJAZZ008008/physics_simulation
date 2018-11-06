import vector2d
import vector3d


class Ball(object):
    def __init__(self, position, velocity, force, mass, radius, elasticity, friction):
        self.position = position
        self.velocity = velocity
        self.force = force

        self.mass = mass
        self.radius = radius

        self.elasticity = elasticity
        self.friction = friction

        self.moving = True

        self.path = []
        self.x_path = []
        self.y_path = []
        self.z_path = []

        self.update_path_list()

    @staticmethod
    def integrate(value, increment, delta_time):
        new_value = vector3d.Vector3D(0, 0, 0)

        new_value.x = value.x + (increment.x * delta_time)
        new_value.y = value.y + (increment.y * delta_time)
        new_value.z = value.z + (increment.z * delta_time)

        return new_value

    def elastic_constant(self, room):
        return (self.elasticity + room.elasticity) * 0.5

    def friction_constant(self, room):
        return 1 - ((self.friction + room.friction) * 0.5)

    def collision(self, room, previous_position):
        if self.position.x < room.origin.x or self.position.x > room.limit.x:
            self.position = previous_position

            self.velocity.x *= -1

            self.velocity.x *= self.elastic_constant(room)
            self.velocity.y *= self.friction_constant(room)
            self.velocity.z *= self.friction_constant(room)

        if self.position.y < room.origin.y or self.position.y > room.limit.y:
            self.position = previous_position

            self.velocity.y *= -1

            self.velocity.x *= self.friction_constant(room)
            self.velocity.y *= self.elastic_constant(room)
            self.velocity.z *= self.friction_constant(room)

        if self.position.z < room.origin.z or self.position.z > room.limit.z:
            self.position = previous_position

            self.velocity.z *= -1

            self.velocity.x *= self.friction_constant(room)
            self.velocity.y *= self.friction_constant(room)
            self.velocity.z *= self.elastic_constant(room)

    def update_moving(self):
        if self.velocity.dot() < 0.1:
            self.velocity = vector3d.Vector3D(0, 0, 0)

            self.moving = False

    def update_path_list(self):
        self.path.append(self.position)

    def update(self, delta_time, room):
        previous_position = self.position

        self.velocity = self.integrate(self.velocity, self.force, delta_time)
        self.position = self.integrate(self.position, self.velocity, delta_time)

        self.collision(room, previous_position)

        self.update_moving()

        self.update_path_list()

    def update_path_lists(self, position):
        self.x_path.append(position.x)
        self.y_path.append(position.y)
        self.z_path.append(position.z)

    def convert_path(self):
        for position in self.path:
            self.update_path_lists(position)
