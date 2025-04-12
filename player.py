import pygame
#custom dependencies
import enemies

playerSize = 40

def playerRender(player_pos, dt, screen, keys): # draw and move player
    pygame.draw.circle(screen, "blue", player_pos, playerSize)
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

def healthBar(health, screen): # draw health bar
    pygame.draw.rect(screen, "gray", (10, 10, 100, 20))
    pygame.draw.rect(screen, "red", (10, 10, (100 * (health) / 5), 20))     

def collisionCheck(collisionRect, enemies): # check for collision
    collideList = []
    for enemy in enemies:
        collideList.append(enemy.rect)
    index = collisionRect.collidelist(collideList)
    if index != -1:
        return index # return index of enemy if collision is detected
    else:
        return -1 # return -1 if no collision is detected
    
#============ ATTACKS =============#
# dictionary of attack types, name : [shape, size, color]
attackTypes = [ # to add new attack, add to this list, then add a key activation to the selectAttack function
    ("shield of faith", ["circle", 100, "light grey"]), 
    ("The Sword of Laban", ["attack rect", (100, 20), "orange"]),
    ("stratagem", ["attack rect", (20, 100), "black"])
    ]

# check which attack to use, then instantiate attack class and draw the attack
# return True if enemy killed, else return False
def selectAttack(keys, screen, player_pos, enemiesList):
    if keys[pygame.K_1]:
        return attack.drawAttack(attack(attackTypes[0], enemiesList), screen, player_pos) 
    elif keys[pygame.K_2]:
        return attack.drawAttack(attack(attackTypes[1], enemiesList), screen, player_pos)
    elif keys[pygame.K_3]:
        return attack.drawAttack(attack(attackTypes[2], enemiesList), screen, player_pos)  
    else:
        return False
        
class attack:    
    def __init__(self, type, enemiesList):
        self.type = type # type of attack
        self.typeIndex = attackTypes.index(type) # index of attack type for collision comparison
        self.size = type[1][1] # size of attack
        self.color = type[1][2] # color of attack
        self.enemies = enemiesList # list of enemies for collision comparison
        
    # draw attack and check collision
    #return True if correct collision is detected, else return False
    def drawAttack(self, screen, player_pos):
        if self.type[1][0] == "circle":
            pygame.draw.circle(screen, self.color, player_pos, self.size)
            return self.__collisionIndexCheck((player_pos.x - self.size, player_pos.y - self.size, self.size * 2, self.size * 2), self.enemies)
        elif self.type[1][0] == "attack rect":
            attackRectDim = self.__transformAttackVector(player_pos, self.type[1][1])
            pygame.draw.rect(screen, self.color, attackRectDim)
            return self.__collisionIndexCheck(attackRectDim, self.enemies)
        else: 
            return False
        
    # transform attack vector to be inline with player direction
    def __transformAttackVector(self, player_pos, rectDim):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return (player_pos.x - rectDim[1]/2, player_pos.y - playerSize - rectDim[0],
                     rectDim[1], rectDim[0])
        elif keys[pygame.K_DOWN]:
            return (player_pos.x - rectDim[1]/2, player_pos.y + playerSize,
                     rectDim[1], rectDim[0])
        elif keys[pygame.K_LEFT]:
            return (player_pos.x - playerSize - rectDim[0], player_pos.y - self.size[1] / 2,
                     self.size[0], self.size[1])
        else: # keys[pygame.K_RIGHT]: Default to right
            return (player_pos.x + playerSize, player_pos.y - self.size[1] / 2,
                     self.size[0], self.size[1])

    
    # check for collision with correct enemy type (index to index)
    def __collisionIndexCheck(self, rectDim, enemiesList):
        collisionIndex = collisionCheck(pygame.Rect(rectDim), enemiesList)
        if -1 != collisionIndex and self.typeIndex == enemies.enemy.enemyTypes.index(enemiesList[collisionIndex].type):
            enemies.killEnemy(enemiesList, collisionIndex)
            return True
        else:
            return False