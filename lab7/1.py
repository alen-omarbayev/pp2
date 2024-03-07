import pygame

pygame.init()

done = False

X = 600
Y = 600
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('image')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\DELL\\Downloads\\gfg.png").convert()
 
# Using blit to copy content from one surface to other
scrn.blit(imp, (0, 0))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()

