import pygame
import sys
from constants import *

def pause_loop(screen):
    font = pygame.font.SysFont(None, 36)
    paused = True

    while paused:
        screen.fill(DARK_GRAY)
        msg = font.render("Paused - Press R to Resume", True, WHITE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    paused = False
