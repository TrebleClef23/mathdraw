from constants import *
from typing import List
from graph import Graph

class Displayer:
    graphs: List[Graph]
    def __init__(self) -> None: ...
    def save(self, filename, namehint: str="") -> None: ...
