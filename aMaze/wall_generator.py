from settings import *


class WallGenerator:
    def __init__(self, game):
        self.game = game
        self.ray_scan = None

    def update(self):
        self.ray_scan = self.game.ray_caster.ray_scan

    def draw(self):
        i = 0
        for ray in self.ray_scan:
            length = ray["length"]

            scanline_height = screen_distance / (length + 0.00001)

            color = []

            for j in range(3):
                color.append(255 * (1 - (length / draw_distance)))

            pg.draw.rect(self.game.screen, color,
                         (i * scale_3d, height // 2 - scanline_height // 2, scale_3d, scanline_height))

            i += 1
