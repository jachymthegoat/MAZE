from vector2 import Vector2
from gui import Gui

"""
Jáchym Nácovský
9.12.2024
"""

class GameObject:
    """Zapsání pozice"""
    def __init__(self, position: Vector2, symbol: str):
        self._position = position
        self._symbol = symbol

    @property
    def position(self) -> Vector2:
        return self._position

    def move(self, direction: Vector2):
        self._position += direction

    def draw(self, gui: Gui):
        gui.draw(self.position.x, self.position.y, self._symbol)