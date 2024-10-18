import pygame #pygame is a library used for writing video games, includes CG and sound lib.
import time # for managing time related function
import random # random is used to generate random numbers , here for food at any random place

# Initialize pygame
pygame.init()  #initializes all the Pygame modules required to run the game

# Define colors. these are RGB colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (102, 0, 204)
orange = (255, 165, 0)

# Set display dimensions
width = 600
height = 400
display = pygame.display.set_mode((width, height))  #creates the game window with the specified dimensions.
pygame.display.set_caption('Snake Game') #sets the title of the game window as "Snake Game.

# Set up game clock and other parameters
clock = pygame.time.Clock()  #clock controls the frame rate, how fast the game runs
snake_block = 10 # size of each block that makes snake and food and in my game it is 10x10 px.
snake_speed = 15  # speed how fast snake will move

# Define fonts for aesthetic GUI
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, orange)
    display.blit(value, [0, 0])

# Define the snake rendering function
def our_snake(snake_block, snake_list): #This function is responsible for drawing the snake on the screen
    for x in snake_list:
        pygame.draw.rect(display, purple, [x[0], x[1], snake_block, snake_block])

# Define the message display function for game over screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop(): #game_loop() function contains the logic for the entire game
    game_over = False
    game_close = False

#The initial position of the snake (center of the screen)
    x1 = width / 2
    y1 = height / 2

#Variables that store how much the snake moves after each frame (either left, right, up, or down)
    x1_change = 0
    y1_change = 0

    snake_list = []  #list of coordinates that represent the positions of all the blocks that make up the snake.
    length_of_snake = 1  #The length of the snake (starts with 1 block)

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        # Handling the game close scenario
        while game_close:
            display.fill(black)
            message("Haar Gye Ho Tum😴! Press C-Play Again or Q-Quit", red)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handling keypresses for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Snake movement boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        # Background and borders
        display.fill(blue)
        pygame.draw.rect(display, black, [0, 0, width, 10])  # Top border
        pygame.draw.rect(display, black, [0, 0, 10, height])  # Left border
        pygame.draw.rect(display, black, [0, height - 10, width, 10])  # Bottom border
        pygame.draw.rect(display, black, [width - 10, 0, 10, height])  # Right border

        # Draw food
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])

        # Snake body logic
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Collision detection with snake's own body
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        show_score(length_of_snake - 1)  # Show current score

        pygame.display.update()

        # Detect if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
