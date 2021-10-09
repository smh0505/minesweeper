import os
import pygame as pg
from random import randint

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Minesweeper")
    pg.mouse.set_visible(1)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((82, 82, 78))

    screen.blit(background, (0, 0))
    pg.display.flip()

    going = True
    while going:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
        screen.blit(background, (0, 0))
        pg.display.flip()
    
    pg.quit()

if __name__ == "__main__":
    main()
