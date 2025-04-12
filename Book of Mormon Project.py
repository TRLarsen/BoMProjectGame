import pygame

# homemade dependencies
import player
import initializegame
import enemies

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)#(0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

health = 5
score = 0
player_pos = initializegame.startScreen(screen) # start screen
fullscreen = False # if fullscreen is toggled

enemiesList = [] # list of enemies

while running:
    keys = pygame.key.get_pressed() # get pressed keys
    initializegame.quitCheck() # check for quit command
    fullscreen = initializegame.fullscreenToggle(fullscreen, keys) # toggle fullscreen if f is pressed

    if pygame.key.get_pressed()[pygame.K_ESCAPE]: # if escape is pressed, quit the playthrough
        enemiesList.clear()
        health = 5
        score = 0
        player_pos = initializegame.startScreen(screen)

    if health <= 0: # if health is 0, player dies, then reset position and health
        enemiesList.clear() # clear enemies list
        player_pos = initializegame.playerDeath(screen)
        health = 5
        score = 0
                 
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")

    player.healthBar(health, screen) # Draw the health bar
    player.playerRender(player_pos, dt, screen, keys) # draw and move the player
 
    if 0 == len(enemiesList): # if there are no enemies, spawn enemies
        for i in range(int(score/3) + 1): # spawn enemies based on score, always spawn at least 1
            enemies.enemySpawn(enemiesList, player_pos)
    
    for enemy in enemiesList: # check if enemy is too far from player, delete if so
        if 40000 < enemy.pos.distance_to(pygame.Vector2(player_pos.x, player_pos.y)):
            enemies.killEnemy(enemiesList, enemiesList.index(enemy))

    # draw and move enemies
    enemies.enemyRender(enemiesList, player_pos, dt, screen) 

    # select and draw attack, increment score if enemy killed
    if player.selectAttack(keys, screen, player_pos, enemiesList):
        score += 1

    # check for collision: decrement health and remove enemy if detected
    playerRect = pygame.Rect(player_pos.x - 40, player_pos.y - 40, 80, 80)
    collisionIndex = player.collisionCheck(playerRect, enemiesList)
    if collisionIndex != -1:
        enemies.killEnemy(enemiesList, collisionIndex)
        health -= 1

    # draw score
    initializegame.drawScore(score, screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()