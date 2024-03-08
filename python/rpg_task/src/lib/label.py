from lib.styles import *


class Label:
    def __init__(self, x, y, color, center=False):
        self.x = x
        self.y = y
        self.color = color
        self.center = center

    def render(self, screen, text):
        self.label = font32.render(text, True, self.color)
        if self.center:
            self.w = self.label.get_width()
            self.screen_w = screen.get_width()
            self.x = (self.screen_w - self.w) / 2
        screen.blit(self.label, (self.x, self.y))
