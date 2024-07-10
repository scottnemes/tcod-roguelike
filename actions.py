from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from engine import Engine
   from entity import Entity


class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Perform this action with the objects needed to determine its scope

        'engine': the scope this action is being performed in      
        'entity': the object performing the action
        """
        raise NotImplementedError()


class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self._dx = dx
        self._dy = dy


    def perform(self, engine: Engine, entity: Entity) -> None:
        _dest_x = entity.x + self._dx
        _dest_y = entity.y + self._dy

        if not engine.game_map.in_bounds(_dest_x, _dest_y):
            return
        if not engine.game_map.tiles["walkable"][_dest_x, _dest_y]:
            return
        
        entity.move(self._dx, self._dy)


    @property
    def dx(self):
        return self._dx   
    @property
    def dy(self):
        return self._dy