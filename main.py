import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 550
FPS = 60
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT)) #game window
pygame.display.set_caption("TIC TAC TOE!")  #Title of the game


BACKGROUND_COLOR = (255, 255, 255) # white
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'picture.jpg')), (WIDTH, 450))

# Define border size and color
border_size = 7
border_color = (0, 0, 0) # black

# Create a border surface
border = pygame.Surface((800 + border_size * 2, 600 + border_size * 2))
border.fill(border_color)

# Define font, text color and button color
font = pygame.font.Font(None, 50)

# Create a start button surface
start_button = pygame.Surface((150, 50))
start_button.fill(BACKGROUND_COLOR)

def draw_window():

    WINDOW.fill(BACKGROUND_COLOR)
    WINDOW.blit(border, (0 - border_size, 100 - border_size))
    WINDOW.blit(BACKGROUND, (0, 100))

    # Blit the start button onto the window and write the text "START" on it
    WINDOW.blit(start_button, (WIDTH // 2 - 50, 25))
    start_text = font.render("START", True, border_color)
    WINDOW.blit(start_text, (WIDTH // 2 - 40, 35))

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
