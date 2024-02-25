from settings import *
from maze_generator import *


class Map:
    def __init__(self, game):
        self.game = game

        maze = MazeGenerator(map_width, map_height)
        self.map = maze.generate_map(13)

        self.start = None

    def update(self):
        pass

    def draw(self):
        for y in range(map_height * 2 + 1):
            for x in range(map_width * 2 + 1):
                if self.map[y][x] == "#":
                    pg.draw.rect(self.game.screen, "white",
                                 (x * scale_2d, y * scale_2d, scale_2d, scale_2d))
