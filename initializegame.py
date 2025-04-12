import pygame
import textRect

def quitCheck(): # check for quit command
    for event in pygame.event.get(): # poll for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            pygame.display.set_mode((1280, 720), pygame.RESIZABLE) # set the window to resizable
            pygame.display.update() # update the display
            pygame.quit()
            exit()

def startScreen(screen): # start screen
    while not pygame.key.get_pressed()[pygame.K_s]: # stay on screen until s or i is pressed
        screen.fill("light blue") # background color
        font = pygame.font.Font(None, 74) # define font for title
        midSizeFont = pygame.font.Font(None, 50) # subtitle font
        smallFont = pygame.font.Font(None, 37) # options font
        title = font.render("In Defense of the Faith", True, "black") # title text
        subtitle = midSizeFont.render("A Book of Mormon Project", True, "black") # subtitle text
        # options text
        text = smallFont.render("Press S to Start", True, "black")
        text2 = smallFont.render("Press I for Instructions", True, "black")
        # render text
        screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, screen.get_height() / 2 - (title.get_height() / 2 + 200)))
        screen.blit(subtitle, (screen.get_width() / 2 - subtitle.get_width() / 2, screen.get_height() / 2 - (subtitle.get_height() / 2 + 150)))
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
        screen.blit(text2, (screen.get_width() / 2 - text2.get_width() / 2, screen.get_height() / 2 + text.get_height()))
        pygame.display.flip() # paint on screen

        if pygame.key.get_pressed()[pygame.K_i]:
            instructionScreen(screen)
        quitCheck() # check for quit command
    return pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) # return player position to center of screen

def playerDeath(screen): # death screen
        screen.fill("black") # background color
        font = pygame.font.Font(None, 74) # define font
        text = font.render("You couldn't respond...", True, "red")
        text2 = font.render("   time to go study some more.", True, "red")
        # render text
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
        screen.blit(text2, (screen.get_width() / 2 - text2.get_width() / 2, screen.get_height() / 2 - text2.get_height() / 2 + 50))
        pygame.display.flip() # paint text to screen
        pygame.time.wait(2000) # delay on death screen
        return startScreen(screen) # return to start screen after death

def drawScore(score, screen): # draw score
    w, h = pygame.display.get_surface().get_size()
    font = pygame.font.Font(None, 37)
    text = font.render("Score: " + str(score), True, "black")
    screen.blit(text, (w - (text.get_width() + 10), 10))

def instructionScreen(screen): # instruction screen
    # instructions/inspiration text
    TextLines = """     
        Instructions: \n 
                Use arrow keys to move. \n
                Use 1, 2, & 3 to attack -- careful, each enemy can only be harmed by one type of attack! \n 
                Press F to toggle fullscreen while in-game. \n
        Inspiration: \n
                On my mission I realized the importance of having scriptures readily available from memory. 
                I remembered how impactful games had been in my learning, and started brainstorming ways 
                to combine my passion for technology and my love for the scriptures. \n
                Red enemies represent the miriad annoyances and distractions that assault us on a day-to-day 
                basis, the "shafts in the whirlwind" (Helaman 5:12).
                They are countered by attack 1, the shield of faith, which represents building our 
                foundation (Ibid.) upon Jesus Christ through temple attendence, prayer,
                and scripture study -- putting on the armor of righteousness (2 Nephi 1:23). \n
                Green enemies represent substantiated, targeted attacks on our testimony (see Jacob 7, Alma 1, and Alma 30).
                They must be targeted with attack 2, the Sword of Laban (Jacob 1:10), which represents the power of 
                the word of God (1 Nephi 12:18, Alma 1:7) backed by the power of pure testimony (Alma 4:19). \n
                Grey enemies represent major, persistent doubts cast on the validity of the Church of Jesus Christ 
                of Latter-day Saints. 
                They are countered by attack 3, Stratagem (Alma 43:30), which represents the need to get back to the center of our testimony.
                It represents the building blocks of the words of Christ and his prophets and apostles (Mosiah 15:11, 3 Nephi 20:25). \n
                I testify of Jesus Christ and his restored Church. I know he lives and that the Book of Mormon is his word. \n
                "...feast upon the words of Christ; for behold, the words of Christ will tell you all things what ye should do" (2 Nephi 32:3). \n
                - Tyler Larsen
        """
    w, h = pygame.display.get_surface().get_size() # get the width and height of the screen
    while not pygame.key.get_pressed()[pygame.K_b]: # while the user doesn't press b, render the instruction screen
        screen.fill("light blue") # background color
        # define fonts
        font = pygame.font.Font(None, 30)
        textFont = pygame.font.Font(None, 25)
        # Define the text to be rendered
        # instructionsText uses the textRect module to render the text with word wrap
        instructionsText = textRect.render_textrect(TextLines, textFont, pygame.Rect(0, 0, w, h), "black", "light blue")
        text = font.render("Press B to go back", True, "black") 
        # render the text
        screen.blit(instructionsText, (screen.get_width() / 2 - instructionsText.get_width() / 2, screen.get_height() / 2 - instructionsText.get_height() / 2))
        screen.blit(text, (screen.get_width() - (text.get_width() + 10), screen.get_height() - (text.get_height() + 10)))
        pygame.display.flip() # paint to the screen
        quitCheck() # check for quit command

def fullscreenToggle(fullscreen, keys): # toggle fullscreen, return true if fullscreen, false if not
    if keys[pygame.K_f] and fullscreen: # if toggled and already in fullscreen
        pygame.display.set_mode((1280, 720), pygame.RESIZABLE) # set the window to resizable
        pygame.display.update() # update the display
        return False # set fullscreen to false
    elif keys[pygame.K_f] and not fullscreen: # if toggled and not in fullscreen
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # set the window to fullscreen
        pygame.display.update() # update the display
        return True # set fullscreen to true