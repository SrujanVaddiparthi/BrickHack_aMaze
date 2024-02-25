from settings import *


class RayCaster:
    def __init__(self, game):
        self.game = game
        self.ray_scan = None

    def update(self):
        self.ray_scan = []

        px, py = self.game.player.x, self.game.player.y
        mx, my = int(px), int(py)

        ray_angle = self.game.player.angle - (fov / 2) + 0.0001

        for ray in range(num_rays):
            wall = False
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            x_depth = ((mx + 1) - px) if cos_a > 0 else (
                    px - mx)

            y_depth = ((my + 1) - py) if sin_a > 0 else (
                    py - my)

            ray_length = 0

            d_mx = mx
            d_my = my

            while ray_length <= draw_distance:
                if self.game.map.map[int(d_my)][int(d_mx)] == "#":
                    wall = True
                    break

                x_length = abs(x_depth / cos_a)
                y_length = abs(y_depth / sin_a)

                if y_length < x_length:
                    ray_length = y_length
                    y_depth += 1
                    d_my += sin_a / abs(sin_a)
                elif y_length > x_length:
                    ray_length = x_length
                    x_depth += 1
                    d_mx += cos_a / abs(cos_a)
                else:
                    ray_length = x_length
                    x_depth += 1
                    y_depth += 1
                    d_mx += cos_a / abs(cos_a)
                    d_my += sin_a / abs(sin_a)

            if wall:
                self.ray_scan.append(
                    {"length": ray_length, "angle": ray_angle})
            else:
                self.ray_scan.append(
                    {"length": draw_distance, "angle": ray_angle})
            ray_angle += delta_angle

    def draw(self):
        for scan in self.ray_scan:
            pg.draw.line(self.game.screen, "yellow",
                         (self.game.player.x * scale_2d, self.game.player.y * scale_2d),
                         (self.game.player.x * scale_2d + scan["length"] * scale_2d * math.cos(scan["angle"]),
                          self.game.player.y * scale_2d + scan["length"] * scale_2d * math.sin(scan["angle"])), 1)
