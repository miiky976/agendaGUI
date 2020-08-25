class Controller:
    def __init__(self, win):
        self.win = win

    def create_window(self):
        win = self.win.make_window()
        self.win.set_select()
        win.mainloop()
