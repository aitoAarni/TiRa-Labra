import pygame


class Nappi(pygame.sprite.Sprite):
    """Esittää valikon nappia"""

    def __init__(self, leveys, korkeus, keskipiste, tapahtuma, napin_teksti) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect((0, 0), (leveys, korkeus))
        self.rect.center = keskipiste
        self.tapahtuma = tapahtuma
        self.napin_teksti = napin_teksti
        self.image = None

    def havaitse_hiiren_leijuminen(self, hiiren_pos):
        """Havaitsee jos hiiiri on napin päällä"""
        if self.rect.collidepoint(hiiren_pos):
            return self.rect
        None

    def aktivoi_tapahtuma(self):
        """Aktivoi nappiin linkitetty tapahtuma"""
        self.tapahtuma()
