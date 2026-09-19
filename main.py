import pygame
from setting import *
from ui import  Button, Slider

def main():
    pygame.init()
    pygame.display.set_caption("фортепіно")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    volume_slider = Slider(45, 50, 200, 20, val=0.5)

    keys = []
    key_width = WIDTH // 8

    for i in range(7):

        x_pos = i * key_width + 45
        sound_path = SOUND_FILES[i]

        btn = Button(x=x_pos, y=100, width=key_width - 2, height=250, color=WHITE, sound_path=sound_path)
        btn.sound.set_volume(0.5)
        keys.append(btn)


    while True:
        screen.fill(GRAY)


        font = pygame.font.SysFont(None, 24)
        img = font.render(f"Гучність: {int(volume_slider.val * 100)}%", True, BLACK)
        screen.blit(img, (45, 25))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if volume_slider.handle_event(event):
                for key in keys:
                    key.sound.set_volume(volume_slider.val)

            for key in keys:
                key.handle_event(event)
        volume_slider.draw(screen)
        for key in keys:
            key.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


main()



