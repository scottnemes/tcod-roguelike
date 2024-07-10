from typing import Tuple

import numpy as np


# tile graphics struct compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # unicode code point
        ("fg", "3B"), # 3 unsigned bytes for RGB color codes
        ("bg", "3B"),
    ]
)

# tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), # true if tile may be walked on
        ("transparent", np.bool), # true if tile does not block field of view
        ("dark", graphic_dt), # graphic for when tile is not in field of view
    ]
)


def new_tile(
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """
    used to define individual tile types
    """
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (0, 0, 0)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), (255, 255, 255), (0, 0, 100)),
)
