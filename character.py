from constant import Constants
import pygame.draw

class Character:

    def __init__(self, graph):
        self.graph = graph
        self.constant = Constants
        self.x = self.graph.player.position[0]
        self.y = self.graph.player.position[1]

    def move_position(self):
        self.graph.set_target(self.graph.grid[self.x][self.y])

    def check_neighbours(self):
        neighbours = self.graph.player.get_neighbours()
        return neighbours

    def north(self):
        if self.y > 0:
            if self.graph.grid[self.x][self.y-1] in self.check_neighbours():
                self.y = self.y - 1

        return

    def south(self):
        if self.y < (self.constant.WINDOW_HEIGHT/self.constant.CELL_SIZE) - 1:
            if self.graph.grid[self.x][self.y + 1] in self.check_neighbours():
                self.y = self.y + 1
        return

    def west(self):
        if self.x > 0:
            if self.graph.grid[self.x-1][self.y] in self.check_neighbours():
                self.x = self.x - 1
        return

    def east(self):
        if self.x < (self.constant.WINDOW_WIDTH/self.constant.CELL_SIZE) - 1:
            if self.graph.grid[self.x + 1][self.y] in self.check_neighbours():
                self.x = self.x + 1
        return


