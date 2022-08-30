#Ref: youtube
#used boiler plate code for initial structure. 

import pygame, sys, random
 
pygame.init()
 
WIDTH, HEIGHT = 1280, 720
 
FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
CLOCK = pygame.time.Clock()

#Paddles

player = pygame.Rect(WIDTH-110, HEIGHT/2-50, 10,100)
opponent = pygame.Rect(110, HEIGHT/2-50, 10,100)
p_score, o_score= 0,0 #player and oppoent scores
#Ball
ball = pygame.Rect(WIDTH/2-10, HEIGHT/2-10,20,20)
#initial velocity in horizontal and vertical directions
x_v, y_v = 1,1 



while True:
    keys_pressed = pygame.key.get_pressed()
    #player up motion
    if keys_pressed[pygame.K_UP]:
        if player.top>0:
            player.top -=2 #increaase y value goes down, reducing goes up) 
    #Player down motion
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom<HEIGHT:
            player.bottom +=2
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    #Ball logic
    #upper and lower wall reflection
    if ball.y>=HEIGHT:
        y_v=-1
    if ball.y<=0:
        y_v=1
    #left and right wall 
    if ball.x<=0:
        #player score is +1
        p_score+=1
       #reset ball to center with random direction and speed. 
        ball.center = (WIDTH/2, HEIGHT/2)
        x_v, y_v = random.choice([1,-1]),random.choice([1,-1])
    if ball.x>=WIDTH:
       #opponent score is +1
        o_score+=1
      #reset ball to center with random direction and speed. 
        ball.center = (WIDTH/2, HEIGHT/2)
        x_v, y_v = random.choice([1,-1]),random.choice([1,-1])
    #logic for ball reflection from player paddle     
    if player.x - ball.width <=ball.x<=player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):
        x_v=-1
    #logic for ball reflection from opponents paddle
    if opponent.x - ball.width <=ball.x<=opponent.x and ball.y in range(opponent.top-ball.width, opponent.bottom+ball.width):
        x_v=1
      
    #update ball position
    ball.x+=x_v
    ball.y+=y_v
    
    #opponent logic. position changes to change the ball in vertical plane
    if opponent.y < ball.y:
        opponent.top += 1.5
    if opponent.bottom > ball.y:
        opponent.bottom -= 1.5
    
    #scoring system
    player_score_text = FONT.render(str(p_score), True, "white")
    o_score_text = FONT.render(str(o_score), True, "white")
    
    #fills the screen with black colour after each action update. 
    SCREEN.fill("black") 
    
    
    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)
    pygame.draw.circle(SCREEN, "white", ball.center, 10)
    
    #display score texts
    SCREEN.blit(player_score_text, (WIDTH/2+50,50))
    SCREEN.blit(o_score_text, (WIDTH/2-50,50))
    
    pygame.display.update()
    CLOCK.tick(300)
