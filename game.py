import pygame
import random
# import os
pygame.init()  # Initiate pygame
pygame.mixer.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# creating window

# Screen Dimensions
width = 1000
height = 500
gameWindow = pygame.display.set_mode((width, height))

# welcome image
wcimg = pygame.image.load("Fruity-Snake.jpeg")
wcimg = pygame.transform.scale(wcimg, (width, height)).convert_alpha()

# Background image
bgimg = pygame.image.load("bg.jpg")
bgimg = pygame.transform.scale(bgimg, (width, height)).convert_alpha()

# Game title
pygame.display.set_caption("Fruity Snake")
# pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
font1 = pygame.font.SysFont(None, 50)


# Creating a function for display text on welcome screen
def wc_screen(text, color, x, y):
    screen_text = font1.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# Creating a function for display text on Window
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Creating welcome screen
def welcome():
    exit_game = False
    while not exit_game:

        gameWindow.blit(wcimg, (0, 0))
        wc_screen("Welcome to Fruity Snake", blue, 315, 100)
        wc_screen("Press p To Play Game", black, 325, 380)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.load("Snake Game - Theme Song.mp3")
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(40)


# Creating a game loop
def game_loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 60
    snake_y = 30
    snake_size = 20
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(40, width // 2)
    food_y = random.randint(40, height // 2)
    food_size = 15
    score = 0
    snake_list = []
    snake_length = 1
    fps = 40  # Frame per second
    ''''# Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")'''

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            gameWindow.fill(green)
            text_screen("Game Over! Press Enter To Continue", red, 250, 200)
            text_screen("Your score is:" + str(score), red, 350, 230)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("Snake Game - Theme Song.mp3")
                        pygame.mixer.music.play()
                        game_loop()

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:  # for keyboard key event
                    if event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_a:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_w:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    # cheat code
                    if event.key == pygame.K_q:
                        score += 10

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(20, width // 2)
                food_y = random.randint(20, height // 2)
                snake_length += 5
                if score > int(hiscore):
                    hiscore = score
                    with open("hiscore.txt", "w") as f:
                        f.write(str(hiscore))

            snake_x += velocity_x
            snake_y += velocity_y

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Hiscore: " + str(hiscore), blue, 5, 5)  # displaying score on window
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("Game Over ! Sound.mp3")
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
                game_over = True
                pygame.mixer.music.load("Game Over ! Sound.mp3")
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


welcome()
pygame.quit()
quit()
