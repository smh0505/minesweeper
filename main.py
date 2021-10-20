import os
import pygame as pg
from pygame.constants import FULLSCREEN
import ui
import cell

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

C1 = (223, 223, 229)
C2 = (212, 214, 200)
C3 = (154, 155, 148)
C4 = (82, 82, 78)

fontname = os.path.join(data_dir, "ARCADE_N.TTF")

def main():
    pg.init()
    screen = pg.display.set_mode((0, 0), FULLSCREEN)
    pg.display.set_caption("Minesweeper")
    pg.mouse.set_visible(0)

    # Title screen
    title = ui.titleScreen(screen.get_size(), C4)
    title.printSelected(fontname, 36, C2, C3)

    # Level screen
    level = ui.levelScreen(screen.get_size(), C4)
    level.printSelected(fontname, 36, C2, C3)

    # Options Screen
    option = ui.optionScreen(screen.get_size(), C4)
    option.printSelected(fontname, 36, C2, C3)

    # Paused Screen
    pause = ui.pauseScreen(screen.get_size(), C4)
    pause.printSelected(fontname, 36, C2, C3)

    # Game board
    board = pg.Surface(screen.get_size()).convert()
    board.fill(C1)

    # Init
    screen.blit(title.background, (0, 0))
    pg.display.flip()
    currentMode = 0
    diff = 0
    isPlaying = False

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
                        elif title.selected == 1:
                            currentMode = 2
                        elif title.selected == 3:
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
                            isPlaying = True
                            grid = cell.newBoard(10, 10)
                            grid = cell.setMine(grid, 10)
                            cell.printBoard(grid)
                            currentMode = 4
                        elif level.selected == 1:
                            isPlaying = True
                            grid = cell.newBoard(16, 16)
                            grid = cell.setMine(grid, 40)
                            cell.printBoard(grid)
                            currentMode = 4
                        elif level.selected == 2:
                            isPlaying = True
                            grid = cell.newBoard(30, 16)
                            grid = cell.setMine(grid, 99)
                            cell.printBoard(grid)
                            currentMode = 4
                        else:
                            if isPlaying: currentMode = 3
                            else: currentMode = 0
                        level.resetSelected()
                        level.printSelected(fontname, 36, C2, C3)
            elif currentMode == 2:  # Options Screen
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        option.selectUp()
                        option.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_DOWN:
                        option.selectDown()
                        option.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_SPACE:
                        if option.selected == 2:
                            if isPlaying: currentMode = 3
                            else: currentMode = 0
                            option.resetSelected()
                            option.printSelected(fontname, 36, C2, C3)
            elif currentMode == 3:  # Paused Screen
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        pause.selectUp()
                        pause.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_DOWN:
                        pause.selectDown()
                        pause.printSelected(fontname, 36, C2, C3)
                    if event.key == pg.K_SPACE:
                        if pause.selected == 0:
                            currentMode = 4
                        elif pause.selected == 1:
                            currentMode = 1
                        elif pause.selected == 2:
                            currentMode = 2
                        elif pause.selected == 4:
                            going = False

            else:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        currentMode = 3

        # Switching screens
        if currentMode == 1:
            screen.blit(level.background, (0, 0))
        elif currentMode == 2:
            screen.blit(option.background, (0, 0))
        elif currentMode == 3:
            screen.blit(pause.background, (0, 0))
        elif currentMode == 4:
            screen.blit(board, (0, 0))
        else:
            screen.blit(title.background, (0, 0))
        pg.display.flip()
    
    pg.quit()

if __name__ == "__main__":
    main()
