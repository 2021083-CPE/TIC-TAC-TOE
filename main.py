import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 350, 450
FPS = 60
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT)) #game window
pygame.display.set_caption("TIC TAC TOE!")  #Title of the game



BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'image.jpg')), (WIDTH, HEIGHT))

def draw_window():
    WINDOW.blit(BACKGROUND, (0, 0))
    




    pygame.display.update()

def main():


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        draw_window()


    main()


if __name__ == "__main__":
    main()