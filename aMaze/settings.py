import math

import pygame as pg


def get_window_mode(mode=0):
    modes = {
        0: pg.SHOWN,
        1: pg.NOFRAME,
        2: pg.FULLSCREEN
    }

    return modes.get(mode)


# Window parameters #
resolution = width, height = 1920, 1080
window_mode = get_window_mode(0)
fps = 0

# Map parameters #
map_width = 20
map_height = 20

scale_2d = 10

# Player parameters #
player_speed = 1 / 800
rotation_speed = math.pi / 4000
outer_radius = 10

# Ray parameters #
draw_distance = 5
fov = math.pi / 3
num_rays = width // 1
delta_angle = fov / num_rays

# 3d projection parameters #
screen_distance = (width // 2) / (math.tan(fov / 2))
scale_3d = width // num_rays

# Debug parameters #
mode_2d = 0
show_rays = 0
