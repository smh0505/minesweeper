import pygame as pg

class UI:
    def __init__(self, size, color_b):
        self.background = pg.Surface(size).convert()
        self.background.fill(color_b)

        self.menu = []
        self.selected = 0

    def selectUp(self):
        self.selected -= 1
        if self.selected < 0:
            self.selected = len(self.menu) - 1
    
    def selectDown(self):
        self.selected += 1
        if self.selected >= len(self.menu):
            self.selected = 0

    def printSelected(self, f_name=None, f_size=36, f_color1=(0, 0, 0), f_color2=(255, 255, 255)):
        font = pg.font.Font(f_name, f_size)
        for i in range(len(self.menu)):
            if i == self.selected:
                text = font.render(self.menu[i], 0, f_color2)
                self.background.blit(text, (20, 20 + (i * 56)))
            else:
                text = font.render(self.menu[i], 0, f_color1)
                self.background.blit(text, (20, 20 + (i * 56)))
    
    def resetSelected(self):
        while self.selected != 0:
            self.selectDown()

def titleScreen(size, color_b):
    title = UI(size, color_b)
    title.menu.append("New Game")
    title.menu.append("Options")
    title.menu.append("Records")
    title.menu.append("Quit")
    return title

def levelScreen(size, color_b):
    level = UI(size, color_b)
    level.menu.append("Beginner")
    level.menu.append("Intermediate")
    level.menu.append("Expert")
    level.menu.append("Back")
    return level

def optionScreen(size, color_b):
    option = UI(size, color_b)
    option.menu.append("Theme")
    option.menu.append("Volume")
    option.menu.append("Back")
    return option

def pauseScreen(size, color_b):
    pause = UI(size, color_b)
    pause.menu.append("Resume")
    pause.menu.append("New Game")
    pause.menu.append("Options")
    pause.menu.append("Records")
    pause.menu.append("Quit")
    return pause
