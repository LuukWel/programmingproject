import bisect


class Search:

    def __init__(self, graph):
        self.graph = graph

    def move_loop(self, path, count):
        for node in path:
            self.graph.set_source(node, count)

    def a_star_search(self, indextemp):
        self.graph.reset_state()
        queue = [self.graph.enemy[indextemp]]
        visited = []

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node != self.graph.player:
                if current_node not in visited:
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    for next_node in neighbours:
                        if next_node not in visited:
                            next_node.set_parent(current_node)
                            gscore = next_node.manhattan_distance(self.graph.player)
                            fscore = current_node.get_distance() + 1
                            score = gscore + fscore
                            if next_node not in queue:
                                next_node.set_score(score)
                                bisect.insort_left(queue, next_node)
                            elif score > next_node.score:
                                next_node.set_score(score)
                                queue.remove(next_node)
                                bisect.insort_left(queue, next_node)




            else:
                break

        newpath = self.add_path(indextemp)
        self.move_loop(newpath, indextemp)
        pass

    def add_path(self, count):
        path = []
        current_node = self.graph.player
        while current_node is not None and current_node != self.graph.enemy[count]:
            path.append(current_node)
            current_node = current_node.parent

        return path
