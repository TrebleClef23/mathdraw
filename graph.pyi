from types import FunctionType
from collections.abc import Iterable
from typing import Tuple
from constants import *
from pygame import Surface
from pygame.rect import Rect

class Graph:
    def __init__(self, func: FunctionType, iterable: Iterable) -> None: ...
    def draw(self, surface: Surface) -> None: ...

class Controller(Graph):
    pos: Tuple[int, int]
    def __init__(self, pos: Tuple[int, int]) -> None: ...
    def collidepos(self, pos: Tuple[int, int]) -> bool: ...
    def motion(self, pos: Tuple[int, int]) -> None: ...

class Line(Graph):
    startpos: Tuple[float, float]
    endpos: Tuple[float, float]

    def __init__(self, startpos: Tuple[float, float], endpos: Tuple[float, float]) -> None: ...

class MyHelix(Graph):
    center: Tuple[float, float]
    r: float
    θ: float
    rect: Rect

    def __init__(self, center: Tuple[float, float], r: float, θ: float, rect: Rect) -> None: ...
