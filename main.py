import pygame
 
FPS = 60
LEVEL = []
BACKGROUND_COLOR = ("black")
WIDTH,HEIGHT = 1250,490
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #window
pygame.display.set_caption("Pac-Man")
 
BLOCK_SIZE = 32
 
char_to_image = {
    '.': 'dot.png',
    '=': 'wall.png',
    '*': 'power.png',
}
 
class Pacman(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([1,3])
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

        pygame.display.update()


def loadMap(number): #load in the text file into the array LEVEL 
    file = "map-%s.txt" % number
    with open(file) as f:
        for line in f:
            row = []
            for char in line.strip():
                if char != " ":
                    screen_char = pygame.image.load(char_to_image[char])
                    row.append(screen_char)
                else:
                    row.append(0)
            LEVEL.append(row)
 
    for row in LEVEL:
        for char in row:
            print(char)
    
def draw(number): # trying to use blit to take the char array and change it to string
    x = y = 0
    for row in LEVEL:
        for char in row:
            if char != 0:
                screen.blit(char, (x,y))
            x += 32
        x = 0
        y += 32
 
    pygame.display.update()
 
def main():
 
    loadMap(1) # change the number to change the map

    moving_sprites = pygame.sprite.Group()
    pacman = Pacman(1250,0)
    moving_sprites.add(pacman)



    clock = pygame.time.Clock()
    play = True
    while play:
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                play = False
        draw(1)
        moving_sprites.draw(screen)
        
    
    
    pygame.quit()
 
 
 
if __name__ == "__main__":
    main()