from config import RUUTUJEN_MAARA, LAUDAN_VARI, LAUDAN_VIIVOJEN_VARI, lEVEYS, KORKEUS, NAPPLUOIDEN_VARI, PELI_OHI_VARI, VOITTO_TEKSTIN_VARI, FONTTI
import pygame
import os


class Lauta:
    def __init__(self, ikkuna, ristit, nollat) -> None:
        self._ikkuna = ikkuna
        self._ristit = ristit
        self._nollat = nollat
        self._ruudun_leveys = lEVEYS/RUUTUJEN_MAARA
        self.voittoikkuna = None

    def _piirra_viivat(self):
        for i in range(1, RUUTUJEN_MAARA):
            x = self._ruudun_leveys*i
            y = 0

            pygame.draw.line(self._ikkuna, LAUDAN_VIIVOJEN_VARI,
                             (x, y), (x, KORKEUS))
            pygame.draw.line(
                self._ikkuna, LAUDAN_VIIVOJEN_VARI, (y, x), (lEVEYS, x))

    def _piirra_nollat(self):
        for rivi, sarake in self._nollat:
            keskipiste = (sarake*self._ruudun_leveys+self._ruudun_leveys/2,
                          rivi*self._ruudun_leveys+self._ruudun_leveys/2)
            pygame.draw.circle(self._ikkuna, NAPPLUOIDEN_VARI,
                               keskipiste, self._ruudun_leveys/3, 3)

    def _piirra_ristit(self):
        for rivi, sarake in self._ristit:
            x, y = sarake*self._ruudun_leveys, rivi*self._ruudun_leveys
            pygame.draw.line(self._ikkuna, NAPPLUOIDEN_VARI, (x, y),
                             (x+self._ruudun_leveys, y+self._ruudun_leveys), 3)
            pygame.draw.line(self._ikkuna, NAPPLUOIDEN_VARI,
                             (x+self._ruudun_leveys, y), (x, y+self._ruudun_leveys), 3)

    def tee_voittoteksti(self, merkki):
        self.voittoikkuna = pygame.Surface((lEVEYS, KORKEUS))
        if merkki == "x":
            merkin_nimi = "Ristit"
        else:
            merkin_nimi = "Nollat"
        merkkijono = f"{merkin_nimi} voitti!"
        fontti = pygame.font.Font(os.path.join(
            "materiaalit", "Wedgie Regular.ttf"), FONTTI)
        teksti = fontti.render(merkkijono, True, VOITTO_TEKSTIN_VARI)
        teksti_rect = teksti.get_rect()
        teksti_rect.center = (lEVEYS/2, KORKEUS/2)
        self.voittoikkuna.set_alpha(200)
        self.voittoikkuna.fill(PELI_OHI_VARI)
        self.voittoikkuna.blit(teksti, teksti_rect)

    def _piirra_voittonakyma(self):
        vari = tuple(PELI_OHI_VARI + [50])
        print(vari)
        pygame.draw.rect(self._ikkuna, vari, (0, 0, lEVEYS, KORKEUS))

    def piirra_lauta(self):

        self._ikkuna.fill(LAUDAN_VARI)
        self._piirra_viivat()
        self._piirra_nollat()
        self._piirra_ristit()
        if self.voittoikkuna:
            self._ikkuna.blit(self.voittoikkuna, (0, 0))
        pygame.display.flip()
