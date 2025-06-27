import pygame
import sys
import random

def main_menu():
    play1 = pygame.image.load('play1.png')
    play1 = pygame.transform.scale(play1,(150,50))
    play2 = pygame.image.load('play2.png')
    play2 = pygame.transform.scale(play2,(150,50))
    play1_rect = pygame.Rect(260,350, 150,50)
    game = pygame.image.load('snakegame.jpg')
    game = pygame.transform.scale(game,(400,221))
    
    while True:
        grass.fill((0,0,0))

        if play1_rect.collidepoint(pygame.mouse.get_pos()):
            grass.blit(play2, play1_rect)
        else:
            grass.blit(play1, play1_rect)

        grass.blit(game, pygame.Rect(150,100, 300,166))  
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play1_rect.collidepoint(event.pos):
                    return 


def game_over():
    go = pygame.image.load('gameover.png')
    go = pygame.transform.scale(go,(300,150))
    subtext = pygame.font.SysFont(None, 30).render("Press R to Restart or Esc to exit", True, (0, 0, 0))
    grass.blit(subtext, (170+25, 290+50))
    grass.blit(go,(150+50, 125+50))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # R for Restart
                    return "RESTART"
                elif event.key == pygame.K_ESCAPE:  # Esc to quit
                    pygame.quit()
                    sys.exit()


def play_game():
    x_pos=200
    y_pos=250
    speed=4
    direction='RIGHT'
    snake_body = [(x_pos, y_pos)]
    limit = 570

    fruit_x = random.randint(0, limit-30)
    fruit_y = random.randint(0, limit-30)

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        keys = pygame.key.get_pressed()  
    #controlling snake
        if keys[pygame.K_UP] and direction != 'DOWN':
            direction = 'UP'
        elif keys[pygame.K_DOWN] and direction != 'UP':
            direction = 'DOWN'
        elif keys[pygame.K_LEFT] and direction != 'RIGHT':
            direction = 'LEFT'
        elif keys[pygame.K_RIGHT] and direction != 'LEFT':
            direction = 'RIGHT'
    
        if direction == 'UP':
            y_pos -= speed 
            rotated_head = pygame.transform.rotate(head, 90)
        elif direction == 'DOWN':
            y_pos += speed
            rotated_head = pygame.transform.rotate(head, -90)
        elif direction == 'LEFT':
            x_pos -= speed
            rotated_head = pygame.transform.rotate(head, 180)
        else:  # RIGHT
            x_pos += speed
            rotated_head = head

        #Updating snake body
        snake_body.insert(0, (x_pos, y_pos))  # adding new head at the start

        head_center = (x_pos + 15, y_pos + 15)  #making center of 30x30 head
        fruit_rect = pygame.Rect(fruit_x + 10, fruit_y + 10, 20, 20)  # tighter hitbox
    
    #fruit collision
        if fruit_rect.collidepoint(head_center):
            fruit_x = random.randint(0, limit-30)
            fruit_y = random.randint(0, limit-30)    
            score += 1
            eat_sound.play()
        else:
            snake_body.pop() #grow when eating

    #gameover
        if x_pos < 0 or x_pos > limit-30 or y_pos < 0 or y_pos > limit-30:
            gameover_sound.play()
            result = game_over()
            if result == "RESTART":
                return True
            else:
                return False

        if (x_pos, y_pos) in snake_body[1:]: #ignoring head
            gameover_sound.play()
            result = game_over()
            if result == "RESTART":
                return True
            else:
                return False


        grass.fill((135, 206, 235))
        grass.blit(fruit,(fruit_x+50,fruit_y+50) )

    #draw snake
        for i, segment in enumerate(snake_body[1:], start=1):
            grass.blit(body, (segment[0] + 50, segment[1] + 50))


        grass.blit(rotated_head,(x_pos+50,y_pos+50))

        pygame.draw.rect(grass, (0,0,0),[50,50,570,570],5)
    
        font = pygame.font.SysFont(None,36)
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        grass.blit(score_text,(50,10))
   
        pygame.display.update()
        clock.tick(60)


pygame.init()
grass = pygame.display.set_mode((680,700))
pygame.display.set_caption("Snake Game")

#snake 
head = pygame.image.load('snakehead.png')
head = pygame.transform.scale(head, (30, 30))

body = pygame.image.load('snakebody.png')
body = pygame.transform.scale(body, (30, 30))

fruit = pygame.image.load('apple.png')
fruit = pygame.transform.scale(fruit, (30,30))

pygame.mixer.init()
eat_sound = pygame.mixer.Sound('crunch.wav')
gameover_sound = pygame.mixer.Sound('gameover.wav')

clock = pygame.time.Clock()

main_menu()
while True:
    main_menu()
    while True:
        restart = play_game()
        if not restart:
            pygame.quit()
            sys.exit()