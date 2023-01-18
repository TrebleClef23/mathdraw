from typing import Tuple
from constants import *
from math import log, sin, cos
from pygame import draw
# from julia import Base as jlBase

class Graph:
    def __init__(self, func, iterable):
        self.func = func
        self.iterable = iterable

    def draw(self, surface):
        draw.lines(surface, COLOR, False, [(x, self.func(x)) for x in self.iterable])


class Controller(Graph):
    def __init__(self, pos):
        self.pos = pos
        self.pressed = False

    def draw(self, surface):
        draw.circle(surface, COLOR, self.pos, CONTROLLER_RADIUS)
        if self.pressed:
            draw.circle(surface, PRESSED_COLOR, self.pos, CONTROLLER_RADIUS, PRESSED_WIDTH)

    def collidepos(self, pos):
        return (pos[0] - self.pos[0]) ** 2 + (pos[1] - self.pos[1]) ** 2 <= CONTROLLER_RADIUS ** 2

    def motion(self, pos):
        self.pos = pos


class Line(Graph):
    def __init__(self, startpos, endpos):
        self.startpos = startpos
        self.endpos = endpos

    def draw(self, surface):
        draw.line(surface, COLOR, self.startpos), self.endpos
        return surface


class MyHelix(Graph):
    def __init__(self, center, r, θ, rect):
        self.center = center
        self.r = r
        self.θ = θ
        self.rect = rect

    def draw(self, surface):
        α = 0.0
        αmax = log(self.rect.width ** 2 + self.rect.height ** 2, self.r) / 2
        points = []
        while α < αmax:
            point = self.center[0] + self.r ** α * cos(self.θ * α), self.center[1] + self.r ** α * sin(self.θ * α)
            points.append(point)
            # α = jlBase.nextfloat(α)
            α += 0.03125 / 2  # TODO: optimize
        draw.lines(surface, COLOR, False, points)
