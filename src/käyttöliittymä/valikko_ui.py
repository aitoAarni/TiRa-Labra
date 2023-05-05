import pygame
from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()


class ValikkoUI:

    def __init__(self, ikkuna, napit) -> None:
        self.ikkuna = ikkuna
        self.napit = napit
        self.luo_nappien_kuvat()
        self.aktiivisen_napin_tausta = pygame.Surface((0, 0))

    def luo_nappien_kuvat(self):
        pygame.font.init()

        fontin_koko = konffi.leveys // 25
        for nappi in self.napit.sprites():
            fontti = pygame.font.SysFont(None, fontin_koko)
            teksti = fontti.render(
                nappi.napin_teksti, True, konffi.nappien_vari)
            teksti_skaalattuna = pygame.transform.smoothscale(
                teksti, (nappi.rect.width, nappi.rect.height))
            nappi.image = teksti_skaalattuna

    def tee_hiiri_napin_paalla_effekti(self, nappi):
        if nappi:
            self.aktiivisen_napin_tausta = pygame.transform.scale(
                self.aktiivisen_napin_tausta, (nappi.rect.width, nappi.rect.height))
            self.aktiivisen_napin_tausta.fill((192, 192, 192))

            self.ikkuna.blit(self.aktiivisen_napin_tausta,
                             (nappi.rect.x, nappi.rect.y))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def luo_tekstit(
            self,
            leveys,
            korkeus,
            pelaaj1_teksti,
            pelaaja2_teksti,
            ruutujen_maara):
        
        n_korkeus = korkeus / 30
        fontin_koko = konffi.leveys // 25

        keski_x = leveys / 2
        keski_y = korkeus / 2

        y_alkukorkeus = keski_y - n_korkeus * 8
        fontti = pygame.font.SysFont(None, fontin_koko)
        testi_dict = {
            "Ruutujen maara": ruutujen_maara,
            "Ristit": pelaaj1_teksti,
            "Nollat": pelaaja2_teksti
        }
        i = 0
        for otsikko, teksti in (testi_dict.items()):
            teksti = fontti.render(teksti, True, konffi.nappien_vari)
            otsikko = fontti.render(otsikko, True, (255, 255, 255))
            x = keski_x - teksti.get_width() / 2
            y = y_alkukorkeus + n_korkeus * (6 * i)
            self.ikkuna.blit(
                otsikko, (keski_x - otsikko.get_width() / 2, y - n_korkeus * 2))
            self.ikkuna.blit(teksti, (x, y))
            i += 1

    def piirra_valikko(
            self,
            nappi_jonka_paalla_on_hiiri,
            pelaaj1_teksti,
            pelaaja2_teksti,
            ruutujen_maara):
        self.ikkuna.fill("black")
        self.tee_hiiri_napin_paalla_effekti(nappi_jonka_paalla_on_hiiri)
        self.napit.draw(self.ikkuna)
        self.luo_tekstit(
            konffi.leveys,
            konffi.korkeus,
            pelaaj1_teksti,
            pelaaja2_teksti,
            ruutujen_maara)
        pygame.display.flip()
