from menu import show_menu
from game import run_game
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pygame WASM Demo")
    show_menu(screen)
    run_game(screen)

if __name__ == "__main__":
    main()
