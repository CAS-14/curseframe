import curses

class App:
    def __init__(self):
        pass

    def _runner(self, stdscr):
        self.stdscr = stdscr
        pass

    def run(self):
        curses.wrapper(self._runner)

class MenuItem:
    def __init__(self, name: str, func: callable, args: tuple):
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        return self.func(*self.args)

class ControlScheme:
    def __init__(self, binds: dict):
        for action in binds:
            if isinstance(action, str):
                action = (action,)
            if not isinstance(action, tuple):
                raise Exception("Every keybind must be a string or tuple")
            
            setattr(self, action, binds[action])

default_vertical_menu_control_scheme = ControlScheme({
    "prev": "KEY_UP",
    "next": "KEY_DOWN",
    "select": "\n",
    "break": ""
})

class Menu:
    def __init__(self, app: App, *, items: tuple[MenuItem], controls: ControlScheme = menu_control_scheme):
        self.items = items
        self.selected = -1

    def render(self, y: int = None, x: int = None):
        for i in range(len(self.items)):
            style = curses.A_STANDOUT if self.selected == i else curses.A_NORMAL
            self.parent.stdscr.addstr(y + i, x, self.items[i].name, style)

    def focus(self, y: int = None, x: int = None):
        while True:
            self.render(y, x)
            key = self.parent.stdscr.getkey()
