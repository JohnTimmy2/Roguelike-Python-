from typing import Tuple

import numpy as np

graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

title_dt = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("dark", graphic_dt),
    ]
)

def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark:Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark), dtype=title_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)