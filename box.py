class Box(object):
    def __init__(self, origin, limit, elasticity, friction):
        self.origin = origin
        self.limit = limit

        self.elasticity = elasticity
        self.friction = friction
