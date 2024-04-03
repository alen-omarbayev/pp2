import pygame

def main():
    pygame.init()  #initialize pygame
    screen = pygame.display.set_mode((640, 480))  #set up display
    clock = pygame.time.Clock()  #create a clock to control the frame rate
    
    #initialize variables
    radius = 15
    mode = 'blue'
    points = []
    drawing = False
    eraser = False
    current_color = (255, 255, 255)  #initial color is white
    
    running = True  #flag to control the main loop
    while running:  
        for event in pygame.event.get():  
            
            if event.type == pygame.QUIT:  
                running = False  
                
            if event.type == pygame.KEYDOWN:  #check if a key is pressed
                
                #change drawing mode based on key pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:  #toggle eraser mode
                    eraser = not eraser
                elif event.key == pygame.K_c:  #change current color
                    current_color = pygame.color.THECOLORS['black']  #default color is black
            
            if event.type == pygame.MOUSEBUTTONDOWN:  #check if a mouse button is pressed
                
                #start drawing or erasing based on the mouse button clicked
                if event.button == 1:  #left click grows radius
                    drawing = True
                elif event.button == 3:  #right click shrinks radius and activates eraser
                    drawing = True
                    eraser = True
            
            if event.type == pygame.MOUSEMOTION:  #check if mouse is moved
                
                if drawing:  #if drawing flag is True
                    
                    #add current mouse position to points list
                    position = event.pos
                    points.append(position)
                    points = points[-256:]  #limit points list to last 256 points
                
            if event.type == pygame.MOUSEBUTTONUP:  #check if a mouse button is released
                drawing = False  
        
        screen.fill((0, 0, 0))  
        #draw based on mode and eraser state
        if not eraser:
            draw_with_mode(screen, points, radius, mode, current_color)
        else:
            draw_eraser(screen, points, radius)
        
        pygame.display.flip()  
        clock.tick(60)  
    
    pygame.quit()  

def draw_with_mode(screen, points, radius, mode, color):
    #draw lines between points on the screen
    i = 0
    while i < len(points) - 1:
        drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, color)
        i += 1

def drawLineBetween(screen, index, start, end, width, color_mode, color):
    #draw a line between two points on the screen
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    #determine color based on mode
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    #calculate the difference between start and end points
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    #iterate over the line and draw circles
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def draw_eraser(screen, points, radius):
    #draw circles on the screen to act as an eraser.
    for point in points:
        pygame.draw.circle(screen, (0, 0, 0), point, radius)

main()  
