import pygame
import sys
from constants import *
from pause import pause_loop

def run_game(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_speed = [4, 3]
    ball_radius = 20

    running = True
    while running:
        screen.fill(DARK_GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_loop(screen)
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Ball movement + bounds checking
        for i in (0, 1):
            ball_pos[i] += ball_speed[i]
            if ball_pos[i] - ball_radius < 0 or ball_pos[i] + ball_radius > (WIDTH if i == 0 else HEIGHT):
                ball_speed[i] *= -1

        pygame.draw.circle(screen, RED, ball_pos, ball_radius)
        pygame.display.flip()
        clock.tick(60)
