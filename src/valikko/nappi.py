import pygame

class Nappi(pygame.sprite.Sprite):
    def __init__(self, leveys, korkeus, keskipiste, tapahtuma, napin_teksti) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect((0, 0), (leveys, korkeus))
        self.rect.center = keskipiste
        self.tapahtuma = tapahtuma
        self.napin_teksti = napin_teksti
        self.image = None
    

    def havaitse_hiiren_leijuminen(self, hiiren_pos):
        if self.rect.collidepoint(hiiren_pos):
            return self.rect
        None
    
    def aktivoi_tapahtuma(self):
        self.tapahtuma()