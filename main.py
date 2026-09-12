import pygame
from setting import *
from ui import  Button

def main():
    pygame.init()
    pygame.display.set_caption("фортепіно")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    keys = []
    key_width = WIDTH // 8

    for i in range(7):

        x_pos = i * key_width + 45
        sound_path = SOUND_FILES[i]

        btn = Button(x=x_pos, y=100, width=key_width - 2, height=250, color=WHITE, sound_path=sound_path)
        keys.append(btn)


    while True:
        screen.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            for key in keys:
                key.handle_event(event)
        for key in keys:
            key.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


main()



