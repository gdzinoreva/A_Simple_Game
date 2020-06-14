#Welcome to game, Survivor 2020!

#This game consists of a single player that can move in 4 directions, up, down, left and right.
#To move player use UP,DOWN,LEFT,RIGHT keystrokes on the keyboard.
#This player is running from 'covid-19' enemies which will destroy him on collision, at which point player loses
#To win the game the player has to get to the various 'prizes' on the screen and make contact.
#The prizes are in form of a face-mask, sanitizer or gloves
#Pretty much like life these days!
#If 'covid-19' enemies are offscreen then the game ends due to time out.



import pygame               #Imports game library.
import random               #Generates random numbers.

pygame.init()               #Initializes the pygame modules to start.

print("Welcome to Survivor 2020!\n")

window_width = 1004         #Dimensions for screen of the game.
window_height = 680
window = pygame.display.set_mode((window_width, window_height))     #Creates the screen with above dimensions
pygame.display.set_caption("Survivor 2020 Game")                    #Labels the screen.



#The following section creates player, enemies, prize and background and gives them images in this folder.
gamer = pygame.image.load("player_1.png")
enemy_1 = pygame.image.load("enemy_1a.png")
enemy_2 = pygame.image.load("enemy_2a.png")
enemy_3 = pygame.image.load("enemy_3a.png")
prize_1 = pygame.image.load("prize_mask_2.png")
prize_2 = pygame.image.load("prize_gloves_2.jpg")
prize_3 = pygame.image.load("prize_sanitize_2.png")
background = pygame.image.load("image_2.jpg")



#This section get the width and height of all the images in order to do boundary detection of the images.
player_height = gamer.get_height()
player_width = gamer.get_width()

enemy_1_height = enemy_1.get_height()
enemy_1_width = enemy_1.get_width()
enemy_2_height = enemy_2.get_height()
enemy_2_width = enemy_2.get_width()
enemy_3_height = enemy_3.get_height()
enemy_3_width = enemy_3.get_width()

prize_mask_height = prize_1.get_height()
prize_mask_width = prize_1.get_width()
prize_gloves_height = prize_2.get_height()
prize_gloves_width = prize_2.get_width()
prize_sanitize_height = prize_3.get_height()
prize_sanitize_width = prize_3.get_width()



#Store positions of game variables to be called and changed.
#Different initial positions will be assigned to mix up the game parameters including positions generated at random
gamerXPosition = 500            #specified horizontal, 'X' position.
gamerYPosition = 350            #specified vertical, 'Y' position.

enemy_1XPosition =  window_width            #enemy starts at far right edge of the window.
enemy_1YPosition =  random.randint(0, window_height - enemy_1_height)       #'Y' position is generated randomly is this case.

enemy_2XPosition =  0                       
enemy_2YPosition =  random.randint(0, window_height - enemy_2_height)

enemy_3XPosition =  window_width
enemy_3YPosition =  random.randint(0, window_height - enemy_3_height)

prize_1XPosition =  random.randint(0, window_width - prize_mask_width)      #Prizes generate random positions everytime
prize_1YPosition =  15                                                      #Fixed position on 'Y', just a preference

prize_2XPosition =  random.randint(0, window_width - prize_gloves_width)
prize_2YPosition =  15

prize_3XPosition =  random.randint(0, window_width - prize_sanitize_width)
prize_3YPosition =  random.randint(0, window_height - prize_sanitize_height)




#This checks if the up or down key is pressed, True for pressed and False at the beginning because they have not been pressed.
keyUp= False
keyDown = False
keyLeft= False
keyRight = False




game_loop = True                            #Game loop begins
while game_loop:
    
    
    window.fill((255,255,255))              #Clears the screen.
    window.blit(background, (0, 0))         #Loads background to the screen.
    
    window.blit(gamer, (gamerXPosition, gamerYPosition))        #Draws players onto the screen at specified positions assigned above.        
    window.blit(enemy_1, (enemy_1XPosition, enemy_1YPosition))
    window.blit(enemy_2, (enemy_2XPosition, enemy_2YPosition))
    window.blit(enemy_3, (enemy_3XPosition, enemy_3YPosition))
    window.blit(prize_1, (prize_1XPosition, prize_1YPosition))
    window.blit(prize_2, (prize_2XPosition, prize_2YPosition))
    window.blit(prize_3, (prize_3XPosition, prize_3YPosition))
    pygame.display.flip()                                       #Updates the screen.



    for event in pygame.event.get():                    #This even checks if user quits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


        if event.type == pygame.KEYDOWN:                #This event checks if the user press a key down.
            if event.key == pygame.K_UP:                #pygame.K_UP represents a keyboard key constant same as pygame.K_DOWN and so on.
                keyUp = True  
            if event.key == pygame.K_DOWN:
                keyDown = True       
            if event.key == pygame.K_LEFT:
                keyLeft = True 
            if event.key == pygame.K_RIGHT:
                keyRight = True
                

        if event.type == pygame.KEYUP:                  #Checks if the key is not pressed by user.
            if event.key == pygame.K_UP:                #Is the right key released
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False


#player movement
    if keyUp == True:                                   
        if gamerYPosition > 0:                          #Makes sure player does not move off screen upwards.
            gamerYPosition -= 1
    if keyDown == True:
        if gamerYPosition < window_height - player_height:      #Makes sure player does not move off screen dowwards.
            gamerYPosition += 1
    if keyLeft == True:
        if gamerXPosition > 0:                          #Makes sure player does not move off screen left.
            gamerXPosition -= 1
    if keyRight == True:
        if gamerXPosition < window_width - player_width:        #Makes sure player does not move off screen right.
            gamerXPosition += 1
            


#This section gets the bounding boxes around all game images, to be used to detect collisions.   
    gamerBox = pygame.Rect(gamer.get_rect())
    gamerBox.top = gamerYPosition
    gamerBox.left = gamerXPosition

    enemy_1Box = pygame.Rect(enemy_1.get_rect())
    enemy_1Box.top = enemy_1YPosition
    enemy_1Box.left = enemy_1XPosition

    enemy_2Box = pygame.Rect(enemy_2.get_rect())
    enemy_2Box.top = enemy_2YPosition
    enemy_2Box.left = enemy_2XPosition

    enemy_3Box = pygame.Rect(enemy_3.get_rect())
    enemy_3Box.top = enemy_3YPosition
    enemy_3Box.left = enemy_3XPosition

    prize_1Box = pygame.Rect(prize_1.get_rect())
    prize_1Box.top = prize_1YPosition
    prize_1Box.left = prize_1XPosition

    prize_2Box = pygame.Rect(prize_2.get_rect())
    prize_2Box.top = prize_2YPosition
    prize_2Box.left = prize_2XPosition

    prize_3Box = pygame.Rect(prize_3.get_rect())
    prize_3Box.top = prize_3YPosition
    prize_3Box.left = prize_3XPosition



#Collision checks:
    if gamerBox.colliderect(enemy_1Box) or gamerBox.colliderect(enemy_2Box) or gamerBox.colliderect(enemy_3Box):        #If player collides with any one of 3 enemies.
         print("You failed to protect yourself. You lose!")             #Display lose status

         pygame.quit()                  #Game ends if player loses, exit screen
         game_loop = False              #once game loop is False game window closes immdiately
         #exit(0)
        
    if gamerBox.colliderect(prize_1Box) or gamerBox.colliderect(prize_2Box) or gamerBox.colliderect(prize_3Box):        #If player collides with any one of 3 prizes
        print("Congratulations on protecting yourself! You win!!!")             #display win status
        
        pygame.quit()                   #game ends if player wins, exit screen
        game_loop = False               #once game loop is False game window closes immdiately
        #exit(0)
       
    if enemy_1XPosition < 0 - enemy_1_width or enemy_2XPosition > window_width + enemy_2_width or enemy_2XPosition < 0 - enemy_3_width:
        print("Time out, you were not quick enough to protect yourself. You lose!")

        pygame.quit()                   #game ends if player does not get to prize before enemy goes offscreen, exit screen
        game_loop = False
        #exit(0)
        
#enemies movement 
    enemy_1XPosition -= 1   
    enemy_2XPosition += 1               #enemy 2 moves in a different direction because it starts off a different side
    enemy_3XPosition -= 2


#Additional notes: my game characters move a bit slower because of the background that i have incoporated.It worlks for me like that because
#(cont) now i can use whole numbers to control speed movement 'enemy_1XPosition -= 1' as opposed to using floating points which will cause Runtime errors in other parts of the program that require int().
    
#The images used in this game are not original but were sourced from the following websites:
    
    #REFERENCES
    #face emoji: https://za.pinterest.com/pin/673428950504771510/ 
    #mask emoji: https://za.pinterest.com/pin/568368415466009154/ 
    #virus emoji: https://www.stickpng.com/img/nature/viruses/cartoon-virus-with-face 
    #sanitizer clipart: https://www.nicepng.com/ourpic/u2w7a9e6q8q8u2y3_soap-clipart-hand-soap-apply-soap-to-hands/
    #gloves clipart: https://www.clipart.email/clipart/surgical-glove-clipart-468210.html
    #background: https://www.vectorstock.com/royalty-free-vector/city-background-black-and-white-landscape-for-game-vector-13520306












