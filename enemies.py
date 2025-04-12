import pygame
import random

SPEED_MODIFIER = 4000

class enemy:
    enemyTypes = [("red", 50), ("green", 100), ("grey", 150)] # list of enemy types
    def __init__(self, pos):
        self.type = random.choice(self.enemyTypes) # randomize enemy type
        self.pos = pos
        self.size = self.type[1]
        self.color = self.type[0]
        self.rect = pygame.Rect(pos.x - self.size / 2, pos.y - self.size / 2, self.size, self.size)
        self.alive = True
        

    def draw(self, screen): # draw method for enemy class
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, "black", self.rect, 1)
        else:
            pygame.draw.rect(screen, "red", self.rect)

def enemyRender(enemiesList, player_pos, dt, screen): # draw and move all enemies
        for enemy in enemiesList:
            if player_pos.x > enemy.pos.x:
                enemy.pos.x += SPEED_MODIFIER/enemy.size * dt
            elif player_pos.x < enemy.pos.x:
                enemy.pos.x -= SPEED_MODIFIER/enemy.size * dt
            if player_pos.y > enemy.pos.y:
                enemy.pos.y += SPEED_MODIFIER/enemy.size * dt
            elif player_pos.y < enemy.pos.y:
                enemy.pos.y -= SPEED_MODIFIER/enemy.size * dt
            enemy.rect = pygame.Rect(enemy.pos.x - enemy.size / 2, enemy.pos.y - enemy.size / 2, enemy.size, enemy.size)
            enemy.draw(screen)

def enemySpawn(enemiesList, player_pos): # spawn enemy
    w, h = pygame.display.get_surface().get_size()
    enemyStartingPos = pygame.Vector2(random.randint(0, w), random.randint(0, h)) # randomize enemy starting position
    while enemyStartingPos.distance_to(pygame.Vector2(player_pos.x, player_pos.y)) < 200: # if enemy starting position is too close to player, randomize again
        enemyStartingPos = pygame.Vector2(random.randint(0, w), random.randint(0, h))
    enemyTemp = enemy(enemyStartingPos)
    enemiesList.append(enemyTemp)

def killEnemy(enemiesList, index):
    enemiesList[index].alive = False
    enemiesList.pop(index)