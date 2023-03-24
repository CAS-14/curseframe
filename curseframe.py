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
    def __init__(self, app: App, *, items: tuple[MenuItem], controls: dict = scheme_defaults["menu_vertical"], remember_state: bool = False):
        self.items = items
        self.selected = -1
        self.controls = controls
        self.remember = remember_state
        self.app = app

    def render(self, y: int = None, x: int = None):
        for i in range(len(self.items)):
            style = curses.A_STANDOUT if self.selected == i else curses.A_NORMAL
            self.app.stdscr.addstr(y + i, x, self.items[i].name, style)

    def focus(self, y: int = None, x: int = None):
        if self.selected == -1 or not self.remember:
            self.selected = 0

        while True:
            self.render(y, x)
            key = self.app.stdscr.getkey()
            for action in self.controls:
                if key in self.controls[action]:
                    do_action = action
                    break

            if do_action == "next":
                if self.selected < len(self.items) - 2:
                    self.selected += 1
                else:
                    self.selected = 0

            elif do_action == "prev":
                if self.selected > 0:
                    self.selected -= 1
                else:
                    self.selected = len(self.items) - 1

            elif do_action == "select":
                self.items[self.selected].run()

            elif do_action == "break":
                self.selected = -1
                break