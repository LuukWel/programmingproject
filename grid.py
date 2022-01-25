from pygame import draw, font

class GridElement:

    def __init__(self, x, y, size):
        self.position = (x, y)
        self.neighbours = []
        self.size = (size[0], size[1])
        self.parent = None
        self.distance = None
        self.score = None
        self.color = (255, 255, 255)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return (self.score is not None) and (other.score is None or self.score < other.score)

    def __hash__(self):
        return hash(self.position)

    def __repr__(self):
        return "[%s, %s]" % (self.position, self.score)

    def reset_neighbours(self):
        self.neighbours = []

    def reset_state(self):
        self.parent = None
        self.score = None
        self.distance = None
        self.color = (255, 255, 255)

    def get_neighbours(self):
        return self.neighbours[:]

    def manhattan_distance(self, other):
        x_distance = abs(self.position[0] - other.position[0])
        y_distance = abs(self.position[1] - other.position[1])
        return x_distance + y_distance

    def null_distance(self, other):
        x_distance = abs(self.position[0] - other.position[0])
        y_distance = abs(self.position[1] - other.position[1])
        return max(x_distance ,y_distance)

    def direction(self, other):
        return other.position[0] - self.position[0], other.position[1] - self.position[1]

    def set_score(self, score):
        self.score = score

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_score(self, score):
        return self.score

    def get_position(self):
        return self.position

    def set_parent(self, parent):
        self.parent = parent
        if parent.distance is not None:
            self.distance = parent.distance+1

    def set_color(self, color):
        self.color = color

    def draw_grid_element(self, surface):
        draw.rect(surface, self.color,
                  (self.position[0] * self.size[0], self.position[1] * self.size[1], self.size[0], self.size[1]), 0)

        # discard the directions where neighbours are
        compass = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # The four directions
        for neighbour in self.neighbours:
            if self.direction(neighbour) in compass:
                compass.remove(self.direction(neighbour))

        for direction in compass:
            if direction == (0, -1):  # North
                draw.line(surface, (100, 200, 200), (self.position[0] * self.size[0], self.position[1] * self.size[1]),
                          ((self.position[0] + 1) * self.size[0], self.position[1] * self.size[1]), 2)
            if direction == (1, 0):  # East
                draw.line(surface, (100, 200, 200), ((self.position[0] + 1) * self.size[0], self.position[1] * self.size[1]),
                          ((self.position[0] + 1) * self.size[0], (self.position[1] + 1) * self.size[1]), 2)
            if direction == (0, 1):  # South
                draw.line(surface, (100, 200, 200), (self.position[0] * self.size[0], (self.position[1] + 1) * self.size[1]),
                          ((self.position[0] + 1) * self.size[0], (self.position[1] + 1) * self.size[1]), 2)
            if direction == (-1, 0):  # West
                draw.line(surface, (100, 200, 200), (self.position[0] * self.size[0], self.position[1] * self.size[1]),
                          (self.position[0] * self.size[0], (self.position[1] + 1) * self.size[1]), 2)

    def print_walls(self):
        # discard the directions where neighbours are
        compass = {(0, -1): "North",
                   (1, 0): "East",
                   (0, 1): "South",
                   (-1, 0): "West"}  # The four directions
        for neighbor in self.neighbours:
            compass.pop(self.direction(neighbor))

        print(list(compass.values()))
        return None
