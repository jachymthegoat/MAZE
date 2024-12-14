from vector2 import Vector2

"""
Jáchym Nácovský
9.12.2024
"""

class Gui:
    """Pohyb postavy"""
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.clear()

    def draw(self, x: int, y: int, symbol: str):
        self.canvas[y][x] = symbol

    def show(self):
        print("\n".join("".join(row) for row in self.canvas))

    def clear(self):
        self.canvas = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def input_direction(self) -> Vector2:
        directions = {"8": Vector2(0, -1), "2": Vector2(0, 1), "4": Vector2(-1, 0), "6": Vector2(1, 0)}
        move = input("Směr (8/2/4/6): ")
        return directions.get(move, Vector2(0, 0))