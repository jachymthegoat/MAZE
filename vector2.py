from __future__ import annotations

"""
Jáchym Nácovský
9.12.2024
"""

class Vector2:
    """ Vrací souřadnice """
    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
    
    def __init__(self,x:int,y:int):
        self._x = x
        self._y = y

    def __add__(self,other:Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self)-> str:
        return f"{self.x}; {self.y}"
