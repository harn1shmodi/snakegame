import pygame
import random
pygame.init()

# Colours
green = (135,234,85)
black = (0,0,0)
blue = (0,107,255)
red = (255,0,0)


# Creating Window
screen_width = 900
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width , screen_height))

# Game Title
pygame.display.set_caption("Snake Game by Harnish")
pygame.display.update()

# Game Specification variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,50)
def text_screen(text,colour,x,y):
    screen_text =font.render(text,True,colour)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow , colour,snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,colour, [x , y , snake_size, snake_size])

# Game loop
def gameloop() :
    exit_game = False
    game_over = False
    snake_x = 46
    snake_y = 56
    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height / 2)
    Score = 0
    velocity_x = 0
    velocity_y = 0
    snake_size = 13
    init_velocity = 5
    fps = 45
    snake_list = []
    snake_length = 1
    # Add new variables for second snake
    second_snake_x = 0
    second_snake_y = 0
    second_snake_velocity_x = 0
    second_snake_velocity_y = 0
    second_snake_list = []
    second_snake_length = 3


    while not exit_game :
        if game_over :
            gamewindow.fill(green)
            text_screen("Your Score : "+ str(Score*15), black , 325, 150)
            text_screen("Game Over! Press enter to continue", red , 150, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT :
                        velocity_x = 5
                        velocity_y = 0
                    if event.key == pygame.K_LEFT :
                        velocity_x = -5
                        velocity_y = 0
                    if event.key == pygame.K_UP :
                        velocity_y = -5
                        velocity_x = 0

                    if event.key == pygame.K_DOWN :
                        velocity_y = 5
                        velocity_x = 0
                # New controls for second snake using 1234 keys
                    elif event.key == pygame.K_1:  # Right
                        second_snake_velocity_x = init_velocity
                        second_snake_velocity_y = 0
                    elif event.key == pygame.K_2:  # Left
                        second_snake_velocity_x = -init_velocity
                        second_snake_velocity_y = 0
                    elif event.key == pygame.K_3:  # Up
                        second_snake_velocity_y = -init_velocity
                        second_snake_velocity_x = 0
                    elif event.key == pygame.K_4:  # Down
                        second_snake_velocity_y = init_velocity
                        second_snake_velocity_x = 0


            # Second snake movement (new code)
            second_snake_x += second_snake_velocity_x
            second_snake_y += second_snake_velocity_y


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x -food_x)<8 and abs(snake_y - food_y)<8 :
                Score = Score+1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length = snake_length + 3.2
            gamewindow.fill(green)
            text_screen("Score: " + str(Score * 15), black, 5, 5)
            pygame.draw.rect(gamewindow, red,[food_x, food_y, snake_size, snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length :
                del snake_list[0]

            if head in snake_list[0:-1] :
                game_over = True

            if snake_x <0 or snake_x > screen_width or snake_y <0 or snake_y > screen_width:
                game_over = True
            # Drawing and collision detection for second snake
            # Similar to first snake, but with separate variables
            if Score >= 300:  # Activate second snake at score 300
                # Draw second snake
                pygame.draw.rect(gameWindow, red, [second_snake_x, second_snake_y, snake_size, snake_size])
                
                # Collision detection for second snake
                # Add logic to detect collisions with boundaries, itself, and first snake
                
                # Update second snake list (similar to first snake logic)
                second_snake_head = []
                second_snake_head.append(second_snake_x)
                second_snake_head.append(second_snake_y)
                second_snake_list.append(second_snake_head)
                
                if len(second_snake_list) > second_snake_length:
                    del second_snake_list[0]
            plot_snake(gamewindow, blue, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()
