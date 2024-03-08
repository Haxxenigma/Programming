import pygame as pg
from lib.styles import *


class InputBox:
    def __init__(self, x, y, w, h, text=""):
        self.rect = pg.Rect(x, y, w, h)
        self.color = blue
        self.text = text
        self.text_surf = font32.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, num, index, players_info, prompts_len):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = azure if self.active else blue
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    players_info.append(self.text)
                    self.text = ""
                    if index == prompts_len - 1:
                        num += 1
                        index = 0
                    else:
                        index += 1
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surf = font32.render(self.text, True, self.color)
        return num, index

    def draw(self, screen):
        screen.blit(self.text_surf, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 1, 5)
