

class Wizard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32)) # หน้าตา
        self.rect = self.image.get_rect()
        