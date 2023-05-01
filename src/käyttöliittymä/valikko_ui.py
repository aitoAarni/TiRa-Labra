import pygame, os
from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()
LEVEYS, NAPPIEN_VARI = konffi["leveys"], konffi["nappien_väri"]

class ValikkoUI:

    def __init__(self, ikkuna, napit) -> None:
        self.ikkuna = ikkuna
        self.napit = napit
        self.luo_nappien_kuvat()

    def luo_nappien_kuvat(self):
        pygame.font.init()
        fontin_sijainti = os.path.join("materiaalit", "Wedgie Regular.ttf")
        fontin_koko = LEVEYS // 25
        for nappi in self.napit.sprites():
            
            print(nappi.napin_teksti)
            fontti = pygame.font.SysFont(None, fontin_koko)
            nappi.image = fontti.render(nappi.napin_teksti, True, NAPPIEN_VARI)


    def piirra_valikko(self):
        self.ikkuna.fill("black")
        self.napit.draw(self.ikkuna)
        pygame.display.flip()