import sys

from map import Map
from player import Player
from ray_caster import RayCaster
from settings import *
from wall_generator import WallGenerator


class Maze:
    def __init__(self):
        self.map = None
        self.player = None
        self.ray_caster = None
        self.wall_generator = None

        pg.init()
        self.screen = pg.display.set_mode(resolution, window_mode)
        self.clock = pg.time.Clock()
        self.delta_time = 1

        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.ray_caster = RayCaster(self)
        self.wall_generator = WallGenerator(self)

    def update(self):
        self.player.update()
        self.ray_caster.update()
        self.wall_generator.update()

        pg.display.flip()

        self.delta_time = self.clock.tick(fps)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')

        if mode_2d:
            self.map.draw()
            self.player.draw()

            if show_rays:
                self.ray_caster.draw()
        else:
            self.wall_generator.draw()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.update()
            self.draw()


if __name__ == "__main__":
    game = Maze()
    game.run()
