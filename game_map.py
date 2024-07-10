from textwrap import fill
import numpy as np
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._tiles = np.full((width, height), fill_value=tile_types.floor, order="F")

        self.tiles[30:33, 22] = tile_types.wall


    def in_bounds(self, x:int, y: int) -> bool:
        """
        return True if coords are within the map boundaries
        """
        return 0 <= x < self._width and 0 <= y < self._height
    

    def render(self, console: Console) -> None:
        console.rgb[0:self._width, 0:self._height] = self.tiles["dark"]


    @property
    def tiles(self):
        return self._tiles