from tkinter import messagebox, Tk
import pygame
import sys 

window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width,window_height))

columns  = 50
rows = 50

box_width = window_width // columns
box_height = window_height // rows

grid = []

class Box():
    def __init__(self, i ,j):
        self.x = i
        self.y = j
        self.start = False #? flags 
        self.wall = False
        self.target = False
        
    def draw (self,win,color):
        pygame.draw.rect(win,color,(self.x * box_width, self.y *box_height, box_width - 2, box_height - 2))

#! FULL GRID 
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i,j)) #! creating instances of the class object for each rows/columns 
    grid.append(arr)
    
start_box = grid[0][0] #! START POSITION 

def main():
    begin_search = False
    target_box_set = False
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            #mouse control
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                
                #Draw wall
                if event.buttons[0]:
                    i = x // box_width
                    j = y // box_height
                    grid[i][j].wall = True
                    
                # Set Target
                if event.buttons[2] and not target_box_set:
                    i = x // box_width
                    j = y // box_height
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
                    
            # Start Algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True
    
        window.fill((0,0,0))
    
        
        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (20,20,20) )
                
                if box.start:
                    box.draw(window, (0, 200, 200))
                    
                if box.wall:
                    box.draw(window, (90, 90, 90))
                
                if box.target:
                    box.draw(window, (200, 200, 0))
                        
             

        pygame.display.flip()

    
main()