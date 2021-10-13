import os
import pygame as pg
import ui
from random import randint

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

C1 = (223, 223, 229)
C2 = (212, 214, 200)
C3 = (154, 155, 148)
C4 = (82, 82, 78)

fontname = os.path.join(data_dir, "ARCADE_N.TTF")

def main():
    pg.init()
    screen = pg.display.set_mode((1024, 768))
    pg.display.set_caption("Minesweeper")
    pg.mouse.set_visible(0)

    # Title screen
    title = ui.titleScreen(screen.get_size(), C4)
    title.printSelected(fontname, 36, C2, C3)

    # Level screen
    level = ui.levelScreen(screen.get_size(), C4)
    level.printSelected(fontname, 36, C2, C3)

    # Game board
    board = pg.Surface(screen.get_size()).convert()
    board.fill(C1)

    # Init
    screen.blit(title.background, (0, 0))
    pg.display.flip()
    currentMode = 0

    # Main function
    going = True
    while going:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif currentMode == 0:  # Title screen
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        title.selectUp()
                        title.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_DOWN:
                        title.selectDown()
                        title.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_SPACE:
                        if title.selected == 0:
                            currentMode = 1
                        if title.selected == 2:
                            going = False
            elif currentMode == 1:  # Level screen
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        level.selectUp()
                        level.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_DOWN:
                        level.selectDown()
                        level.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_SPACE:
                        if level.selected == 0:
                            currentMode = 2
                        elif level.selected == 1:
                            currentMode = 2
                        elif level.selected == 2:
                            currentMode = 2
                        else:
                            currentMode = 0
                        level.resetSelected()
                        level.printSelected(fontname, 36, C2, C3)
                            
            else:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        currentMode = 0

        # Switching screens
        if currentMode == 1:
            screen.blit(level.background, (0, 0))
        elif currentMode == 2:
            screen.blit(board, (0, 0))
        else:
            screen.blit(title.background, (0, 0))
        pg.display.flip()
    
    pg.quit()

if __name__ == "__main__":
    main()
