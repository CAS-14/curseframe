import curses

class App:
    def __init__(self):
        pass

    def run(self):
        pass

class MenuItem:
    def __init__(self, name: str, func: callable, args: tuple):
        self.name = name
        self.func = func
        self.args = args

    def place(self, y: int, x: int, state: bool):
        pass

    def run(self):
        return self.func(*self.args)

class Menu:
    def __init__(self, *, items: list[MenuItem]):
        self.items = items

    