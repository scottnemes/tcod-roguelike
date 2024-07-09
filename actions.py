class Action:
    pass


class EscapeAction(Action):
    pass


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self._dx = dx
        self._dy = dy

    @property
    def dx(self):
        return self._dx
    
    @property
    def dy(self):
        return self._dy