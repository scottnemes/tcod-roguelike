from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self._entities = entities
        self._event_handler = event_handler
        self._game_map = game_map
        self._player = player


    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self._event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self._player)


    def render(self, console: Console, context: Context) -> None:
        self._game_map.render(console)

        for entity in self._entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)
        
        context.present(console)
        
        console.clear()
    
    @property
    def game_map(self):
        return self._game_map