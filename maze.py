import random
from random import randint
from datetime import datetime
from grid import GridElement


class Maze:

    def __init__(self, grid_size_x, grid_size_y, screen_size):
        self.grid_size = (grid_size_x, grid_size_y)
        self.cell_width = screen_size[0] / grid_size_x
        self.cell_height = screen_size[1] / grid_size_y
        self.grid = []
        for x in range(grid_size_x):
            self.grid.append([])
            for y in range(grid_size_y):
                self.grid[x].append(GridElement(x, y, (self.cell_width, self.cell_height)))
        self.enemy = [self.grid[0][0], self.grid[-1][0], self.grid[0][-1]]
        self.player = self.grid[-1][-1]
        self.goal = self.grid[5][5]
        self.reset_state()
        self.reset_all()
        random.seed(datetime.now())

    def reset_all(self):
        for row in self.grid:
            for cell in row:
                cell.reset_neighbours()
        self.reset_state()
        return None

    def reset_state(self):
        for row in self.grid:
            for cell in row:
                cell.reset_state()
        self.goal.color = (0, 255, 0)
        for foe in self.enemy:
            foe.set_distance(0)
            foe.set_score(0)
            foe.color = (255, 0, 0)
        self.player.color = (0, 0, 255)
        return None

    def append_enemy(self):
        self.enemy.append(self.grid[randint(0, 5)][randint(0, 5)])
        self.reset_state()

    def set_source(self, cell, i):
        for foe in self.enemy:
            if self.enemy[i] != foe:
                if cell != foe:
                    self.enemy[i] = cell
                    self.enemy[i].reset_state()
            else:
                self.enemy[i] = cell
                self.enemy[i].reset_state()

    def set_target(self, cell):
        for foe in self.enemy:
            self.player = cell
            self.reset_state()

    def draw_maze(self, surface):
        for row in self.grid:
            for element in row:
                element.draw_grid_element(surface)
        return None

    def possible_neighbours(self, cell):
        neighbours = []
        if cell.position[0] > 0:  # North
            neighbours.append(self.grid[cell.position[0] - 1][cell.position[1]])
        if cell.position[0] < self.grid_size[0] - 1:  # East
            neighbours.append(self.grid[cell.position[0] + 1][cell.position[1]])
        if cell.position[1] < self.grid_size[1] - 1:  # South
            neighbours.append(self.grid[cell.position[0]][cell.position[1] + 1])
        if cell.position[1] > 0:  # West
            neighbours.append(self.grid[cell.position[0]][cell.position[1] - 1])
        return neighbours

    def add_link(self, cell1, cell2):
        if cell1.manhattan_distance(cell2) == 1:
            cell1.neighbours.append(cell2)
            cell2.neighbours.append(cell1)
        return None

    def generate_maze(self):
        self.reset_all()
        for foe in self.enemy:
            wait = [foe]
        passed = set()
        while len(wait) > 0:
            current_element = wait.pop(-1)
            if current_element not in passed:
                passed.add(current_element)

                neighbours = self.possible_neighbours(current_element)  # Here we want to us all possible neighbours
                for cell in neighbours[:]:
                    if cell in passed:
                        neighbours.remove(cell)
                random.shuffle(neighbours)
                wait.extend(neighbours)
                for next_element in neighbours:
                    next_element.parent = current_element

                if current_element.parent is not None:  # The source has no parent
                    self.add_link(current_element.parent, current_element)

        # add a few random links
        for i in range(max(self.grid_size)):
            random_row = random.choice(self.grid)
            random_element = random.choice(random_row)
            possible = self.possible_neighbours(random_element)
            for cell in possible[:]:
                if cell in random_element.get_neighbours():
                    possible.remove(cell)
            if len(possible) > 0:
                random_neighbor = random.choice(possible)
                self.add_link(random_element, random_neighbor)

        self.reset_state()
        return None
