import pygame
import random 

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('microsofttaile', 30) 
gameOverfont = pygame.font.SysFont('microsofttaile', 50, bold = True) 
  
screen = pygame.display.set_mode((600, 600))

done = False

backgroundImage = pygame.image.load("background.jpg")

playerImage = pygame.image.load("player.png")

player_x = 200
player_y = 500

enemyImage = pygame.image.load("enemy.png")

enemy_x = random.randint(0,536)
enemy_y = random.randint(20, 50)

enemy_dx = 5
enemy_dy = 15

bulletImage = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 600
bullet_dy = 10

shoot = False
hit = False

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def bullet(x, y):
    screen.blit(bulletImage, (x, y))

def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    if (bullet_x >= enemy_x and bullet_x <= enemy_x + 64) and (bullet_y <= enemy_y + 64 and bullet_y >= enemy_y):
        return True
    return False

def death(player_x, player_y, enemy_x, enemy_y):
    if (player_x >= enemy_x and player_x <= enemy_x + 64) and (player_y <= enemy_y + 64):
        return True
    return False


score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: 
        player_x -= 3
    
    if pressed[pygame.K_RIGHT]: 
        player_x += 3
    
    enemy_x += -enemy_dx
    if enemy_x < 0 or enemy_x > 536:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy

    if pressed[pygame.K_SPACE] and shoot is False:
        bullet_x = player_x + 35
        bullet_y = player_y
        shoot = True
    
    coll = collision(enemy_x, enemy_y, bullet_x, bullet_y)

    if coll is True :
        bullet_x = 0
        bullet_y = 600
        enemy_x, enemy_y = random.randint(0, 536) , random.randint(20, 50)
        shoot = False
        hit = True 
    
    if hit is True:
        score += 1
        hit = False

    if bullet_y < 0:
        bullet_x = 0
        bullet_y = 600
        shoot = False

    if shoot is not False:
        bullet_y -= bullet_dy
    
    gover= death(player_x, player_y, enemy_x, enemy_y)
    if gover :
        done = True
    
    screen.blit(backgroundImage, (0, 0))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    bullet(bullet_x, bullet_y)
    textsurface = myfont.render(f'Score: {score}', False, (165, 211, 87)) #False - 
    screen.blit(textsurface, (420, 0))
    pygame.display.set_caption(f'Your Score: {score} points!')
    pygame.display.flip()

done = False

gameoverText = gameOverfont.render('Game over', False, (144, 180, 11))
screen.blit(gameoverText, (200, 250))
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()