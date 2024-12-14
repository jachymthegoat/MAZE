from vector2 import Vector2
from gui import Gui

"""
Jáchym Nácovský
9.12.2024
"""

class World:
    """Herní svět"""
    def __init__(self, data: list[list[int]], symbols: list[str]):
        self.data = data
        self.symbols = symbols

    @property
    def width(self) -> int:
        return len(self.data[0])

    @property
    def height(self) -> int:
        return len(self.data)

    def is_empty(self, position: Vector2) -> bool:
        return self.data[position.y][position.x] == 0

    def draw(self, gui: Gui):
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                gui.draw(x, y, self.symbols[cell])
