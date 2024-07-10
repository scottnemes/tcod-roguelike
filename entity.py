from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self._x = x
        self._y = y
        self._char = char
        self._color = color
    

    def move(self, dx: int, dy: int) -> None:
        self._x += dx
        self._y += dy

    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def char(self):
        return self._char
    @property
    def color(self):
        return self._color