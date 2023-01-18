from graph import *
from displayer import Displayer
import math

displayer = Displayer()

displayer.graphs.append(MyHelix((100, 100), 1.1, math.pi / 4, GRAPHS_RECT))
displayer.display()
