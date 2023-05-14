from konfiguraatio import get_konfiguraatio
import pygame
import os

konffi = get_konfiguraatio()


class LautaUI:
    """Pelilaudan graaffinen esitys"""

    def __init__(self, ikkuna: pygame.display, ristit: list, nollat: list) -> None:
        self._ikkuna = ikkuna
        self._ristit = ristit
        self._nollat = nollat
        self._ruudun_leveys = konffi.leveys / konffi.ruutujen_maara
        self._ruudun_korkeus = konffi.korkeus / konffi.ruutujen_maara
        self.voittoikkuna = None

    def _piirra_viivat(self):
        """piirtaa laudan ruudut"""
        for i in range(1, konffi.ruutujen_maara):
            x1 = self._ruudun_leveys * i
            y1 = 0
            x2 = 0
            y2 = self._ruudun_korkeus * i

            # pysty viivat
            pygame.draw.line(
                self._ikkuna,
                konffi.laudan_viivojen_vari,
                (x1, y1),
                (x1, konffi.korkeus),
            )
            # vaaka viivat
            pygame.draw.line(
                self._ikkuna, konffi.laudan_viivojen_vari, (x2, y2), (konffi.leveys, y2)
            )

    def _piirra_nollat(self):
        """Piirttää laudalle nollat"""
        vari = konffi.nappuloiden_vari
        for i, ruutu in enumerate(self._nollat):
            rivi, sarake = ruutu
            if i == len(self._nollat) - 1:
                vari = (0, 255, 10)
            keskipiste = (
                sarake * self._ruudun_leveys + self._ruudun_leveys / 2,
                rivi * self._ruudun_korkeus + self._ruudun_korkeus / 2,
            )
            r = min(self._ruudun_korkeus, self._ruudun_leveys) / 3  # r = säde
            pygame.draw.circle(self._ikkuna, vari, keskipiste, r, 3)

    def _piirra_ristit(self):
        """Piirtää laudalle ristit"""
        vari = konffi.nappuloiden_vari
        r = min(self._ruudun_korkeus, self._ruudun_leveys) / 3  # r = säde

        for i, ruutu in enumerate(self._ristit):
            rivi, sarake = ruutu
            if i == len(self._ristit) - 1:
                vari = (255, 105, 180)

            x, y = sarake * self._ruudun_leveys, rivi * self._ruudun_korkeus
            x_keski, y_keski = x + self._ruudun_leveys / 2, y + self._ruudun_korkeus / 2

            pygame.draw.line(
                self._ikkuna,
                vari,
                (x_keski - r, y_keski - r),
                (x_keski + r, y_keski + r),
                3,
            )
            pygame.draw.line(
                self._ikkuna,
                vari,
                (x_keski + r, y_keski - r),
                (x_keski - r, y_keski + r),
                3,
            )

    def tee_voittoteksti(self, merkki: str):
        """Pelin loputtua tämä metodi tekee tekstin joka näkyy laudalla"""
        self.voittoikkuna = pygame.Surface((konffi.leveys, konffi.korkeus))
        if merkki.lower() == "x":
            merkkijono = "RISTIT VOITTI!"

        elif merkki == "-":
            merkkijono = "TASAPELI"

        else:
            merkkijono = "NOLLAT VOITTI!"

        fontin_koko = round(min(konffi.leveys, konffi.korkeus) / 8)

        fontti = pygame.font.SysFont(None, fontin_koko)

        teksti = fontti.render(merkkijono, True, konffi.voitto_tekstin_vari)
        teksti_rect = teksti.get_rect()
        teksti_rect.center = (konffi.leveys / 2, konffi.korkeus / 2)
        self.voittoikkuna.set_alpha(200)
        self.voittoikkuna.fill(konffi.peli_ohi_vari)
        self.voittoikkuna.blit(teksti, teksti_rect)

    def _piirra_voittonakyma(self):
        """Piirtää pelin loputtua informaatiota"""
        vari = konffi.peli_ohi_vari
        pygame.draw.rect(self._ikkuna, vari, (0, 0, konffi.leveys, konffi.korkeus))

    def piirra_lauta(self):
        """Piirtää pelilaudan kaikki komponentit"""
        self._ikkuna.fill(konffi.laudan_vari)
        self._piirra_viivat()
        self._piirra_nollat()
        self._piirra_ristit()
        if self.voittoikkuna:
            self._ikkuna.blit(self.voittoikkuna, (0, 0))
        pygame.display.flip()
