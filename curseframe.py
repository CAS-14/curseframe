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
    
scheme_defaults = {
    "menu_vertical": {
        "prev": "KEY_UP",
        "next": "KEY_DOWN",
        "select": "\n",
        "break": ""
    }
}

class Menu:
    def __init__(self, app: App, *, items: tuple[MenuItem], controls: dict = scheme_defaults["menu_vertical"]):
        self.items = items
        self.selected = -1
        self.controls = controls

    def render(self, y: int = None, x: int = None):
        for i in range(len(self.items)):
            style = curses.A_STANDOUT if self.selected == i else curses.A_NORMAL
            self.parent.stdscr.addstr(y + i, x, self.items[i].name, style)

    def focus(self, y: int = None, x: int = None):
        while True:
            self.render(y, x)
            key = self.parent.stdscr.getkey()
            for action in self.controls:
                if key in self.controls[action]:
                    do_action = action
                    break

            