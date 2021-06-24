import pygame,sys
 
FPS = 60
LEVEL = []
BACKGROUND_COLOR = ("black")
WIDTH,HEIGHT = 1250,490
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #window
pygame.display.set_caption("Pac-Man")
 
BLOCK_SIZE = 32

PMAN_START_X,PMAN_START_Y = 32,32*13

char_to_image = {
    '.': 'dot.png',
    '=': 'wall.png',
    '*': 'power.png',
}
 
class Pacman(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        self.sprites.append(pygame.image.load('pacman_c.png'))
        self.sprites.append(pygame.image.load('pacman_o.png'))
        self.curr = 0
        self.image = self.sprites[self.curr]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def update(self):
        
        if self.is_animating == True:
            self.curr += 0.05
            if self.curr >= len(self.sprites):
                self.curr = 0
                self.is_animating = False
            self.image = self.sprites[int(self.curr)]
            

    def animate(self):
        self.is_animating = True




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
    pacman = Pacman(PMAN_START_X,PMAN_START_Y)
    moving_sprites.add(pacman)



    clock = pygame.time.Clock()
    play = True
    while play:
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                pacman.animate()
        draw(1)
        moving_sprites.draw(screen)
        pacman.update()
        pygame.display.flip()
    
    
    pygame.quit()
 
 
 
if __name__ == "__main__":
    main()
