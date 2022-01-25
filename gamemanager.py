from gyro import GyroTracking

class GameManager:

    def __init__(self, graph, search):
        self.gyro = GyroTracking()
        self.graph = graph
        self.search = search
        self.kill_count = 0;

    def player_caught(self):
        index = 0
        while index < len(self.graph.enemy):
            if self.graph.enemy[index].manhattan_distance(self.graph.player) == 0:
                index += 1
                return True
            else:
                index += 1

    def escape(self):
        if self.graph.goal.manhattan_distance(self.graph.player) == 0:
            return True
        else:
            return False

    def game_ending(self, screen, myfont, height, width):
        if self.escape():
            screen.fill([0, 255, 0])
            text = myfont.render("You win", True, (0, 0, 0))
            screen.blit(text, (width/2, height/2))
            return True
        if self.player_caught():
            screen.fill([255, 0, 0])
            text2 = myfont.render("Game Over", True, (0, 0, 0))
            screen.blit(text2, (width/2, height/2))
            return True

    def handle_chaser(self):
        index = 0
        while index < len(self.graph.enemy):
            self.search.a_star_search(index)
            index += 1

    def add_enemy(self):
        if len(self.graph.enemy) < 5:
            if self.gyro.rotation():
                self.graph.append_enemy()

    def restart(self):
        if self.gyro.rotation_y():
            self.graph.generate_maze()


