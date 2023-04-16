from konfiguraatio import get_konfiguraatio
import pygame
import os

konffi = get_konfiguraatio()

LEVEYS = konffi["leveys"]
KORKEUS = konffi["korkeus"]
RUUTUJEN_MAARA = konffi["ruutujen_määrä"]
LAUDAN_VIIVOJEN_VARI = konffi["laudan_viivojen_väri"]
NAPPULOIDEN_VARI = konffi["nappuloiden_väri"]
FONTTI = konffi["fontti"]
VOITTO_TEKSTIN_VARI = konffi["voitto_tekstin_väri"]
PELI_OHI_VARI = konffi["peli_ohi_väri"]
LAUDAN_VARI = konffi["laudan_väri"]

class Lauta:
    def __init__(self, ikkuna, ristit, nollat) -> None:
        self._ikkuna = ikkuna
        self._ristit = ristit
        self._nollat = nollat
        self._ruudun_leveys = LEVEYS / RUUTUJEN_MAARA
        self._ruudun_korkeus = KORKEUS / RUUTUJEN_MAARA
        self.voittoikkuna = None

    def _piirra_viivat(self):
        for i in range(1, RUUTUJEN_MAARA):
            x1 = self._ruudun_leveys * i
            y1 = 0
            x2 = 0
            y2= self._ruudun_korkeus * i
            # pysty viivat
            pygame.draw.line(self._ikkuna, LAUDAN_VIIVOJEN_VARI,
                             (x1, y1), (x1, KORKEUS))
            # vaaka viivat 
            pygame.draw.line(
                self._ikkuna, LAUDAN_VIIVOJEN_VARI, (x2, y2), (LEVEYS, y2))

    def _piirra_nollat(self):
        vari = NAPPULOIDEN_VARI
        for i, ruutu in enumerate(self._nollat):
            rivi, sarake = ruutu
            if i == len(self._nollat) - 1:
                vari = (0, 255, 10)
            keskipiste = (
                sarake *
                self._ruudun_leveys +
                self._ruudun_leveys /
                2,
                rivi *
                self._ruudun_korkeus +
                self._ruudun_korkeus /
                2)
            r = min(self._ruudun_korkeus, self._ruudun_leveys) / 3
            pygame.draw.circle(self._ikkuna, vari,
                               keskipiste, r, 3)

    def _piirra_ristit(self):
        vari = NAPPULOIDEN_VARI
        r = min(self._ruudun_korkeus, self._ruudun_leveys) / 3

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
                (x_keski + r, y_keski + r), 3)
            pygame.draw.line(
                self._ikkuna,
                vari,
                (x_keski + r, y_keski - r),
                (x_keski - r, y_keski + r), 3)

    def tee_voittoteksti(self, merkki):
        self.voittoikkuna = pygame.Surface(
            (LEVEYS, KORKEUS))
        if merkki.lower() == "x":
            merkkijono = "RISTIT VOITTI!"
        
        elif merkki == "-":
            merkkijono = "TASAPELI -_-"
        
        else:
            merkkijono = "NOOLAT VOITTI!"

        fontti = pygame.font.Font(os.path.join(
            "materiaalit", "Wedgie Regular.ttf"), FONTTI)
        
        teksti = fontti.render(merkkijono, True, VOITTO_TEKSTIN_VARI)
        teksti_rect = teksti.get_rect()
        teksti_rect.center = (LEVEYS / 2, KORKEUS / 2)
        self.voittoikkuna.set_alpha(200)
        self.voittoikkuna.fill(PELI_OHI_VARI)
        self.voittoikkuna.blit(teksti, teksti_rect)

    def _piirra_voittonakyma(self):
        vari = PELI_OHI_VARI
        pygame.draw.rect(
            self._ikkuna,
            vari,
            (0,
             0,
             LEVEYS,
                KORKEUS))

    def piirra_lauta(self):

        self._ikkuna.fill(LAUDAN_VARI)
        self._piirra_viivat()
        self._piirra_nollat()
        self._piirra_ristit()
        if self.voittoikkuna:
            self._ikkuna.blit(self.voittoikkuna, (0, 0))
        pygame.display.flip()
