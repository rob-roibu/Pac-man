import pygame

FPS = 60
LEVEL = []
BACKGROUND_COLOR = ("black")
WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #window
pygame.display.set_caption("Pac-Man")

BLOCK_SIZE = 32

char_to_image = {
    '.': 'dot.png',
    '=': 'wall.png',
    '*': 'power.png',
}

def loadMap(number): #load in the text file into the array LEVEL 
    file = "map-%s.txt" % number
    with open(file) as f:
        for line in f:
            row = []
            for block in line.strip():
                row.append(block)
            LEVEL.append(row)

    
    
def draw(number): # trying to use blit to take the char array and change it to string
    file = "map-%s.txt" % number
    col,row = 0,0
    with open(file, "r") as f:
        for line in f:
            for char in line:
                screen_char = pygame.image.load(char_to_image[char])
                WIN.blit(screen_char, (col, row))
                col += 1
        row += 1

    pygame.display.update()

def main():

    loadMap(1) # change the number to change the map
   
    clock = pygame.time.Clock()
    play = True
    while play:
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                play = False
        draw(1)
        
    #testing github link
    
    pygame.quit()



if __name__ == "__main__":
    main()