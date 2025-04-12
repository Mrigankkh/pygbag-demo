import pygame
import sys
from constants import *

def show_menu(screen):
    font = pygame.font.SysFont(None, 48)
    running = True

    while running:
        screen.fill(BLACK)
        text = font.render("Press SPACE to Start", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
