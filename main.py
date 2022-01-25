import pygame
import sys
from maze import Maze
from constant import Constants
from astar import Search
from joycon import JoyConHandler
from character import Character
from gamemanager import GameManager



class Game:

    def __init__(self):
        pygame.init()
        self.size = (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        self.joycon_handler = JoyConHandler()
        self.screen = pygame.display.set_mode(self.size)
        self.myfont = pygame.font.SysFont("Arial", 80)
        self.time = pygame.time.get_ticks()
        self.maze = Maze(Constants.GRID_COLS, Constants.GRID_ROWS, self.size)
        self.character = Character(self.maze)
        self.maze.generate_maze()
        self.search = Search(self.maze)
        self.game_manager = GameManager(self.maze, self.search)

    def game_loop(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.update_game(delta_time)
        self.handle_events()
        self.draw_components()

    def update_game(self, dt):
        if not self.game_manager.game_ending(self.screen, self.myfont, Constants.WINDOW_HEIGHT/2, Constants.WINDOW_WIDTH/2):
            self.character.move_position()
        self.game_manager.escape()
        self.game_manager.player_caught()
        self.game_manager.add_enemy()
        self.game_manager.restart()
        pass

    def draw_components(self):
        self.screen.fill([255, 255, 255])
        self.maze.draw_maze(self.screen)
        self.game_manager.game_ending(self.screen, self.myfont, Constants.WINDOW_HEIGHT/2, Constants.WINDOW_WIDTH/2)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for event, status in self.joycon_handler.joycon.events():
            if status == 1:
                self.handle_button_press(event)
            if status == 1:
                pass

    def handle_button_press(self, event):
        self.joycon_handler.key_pressed(event)
        if event == 'right':
            self.character.north()
            self.game_manager.handle_chaser()
        if event == 'left':
            self.character.south()
            self.game_manager.handle_chaser()
        if event == 'up':
            self.character.west()
            self.game_manager.handle_chaser()
        if event == 'down':
            self.character.east()
            self.game_manager.handle_chaser()


if __name__ == "__main__":
    game = Game()
    while True:
        game.game_loop()
