from config import RUUTUJEN_MAARA, LAUDAN_VARI, LAUDAN_VIIVOJEN_VARI, lEVEYS, KORKEUS, NAPPLUOIDEN_VARI
import pygame


class Lauta:
    def __init__(self, ikkuna, ristit, nollat) -> None:
        self._ikkuna = ikkuna
        self._ristit = ristit
        self._nollat = nollat
        self._ruudun_leveys = lEVEYS/RUUTUJEN_MAARA

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
                               keskipiste, self._ruudun_leveys/3)

    def _piirra_ristit(self):
        for rivi, sarake in self._ristit:
            x, y = sarake*self._ruudun_leveys, rivi*self._ruudun_leveys
            pygame.draw.line(self._ikkuna, NAPPLUOIDEN_VARI, (x, y),
                             (x+self._ruudun_leveys, y+self._ruudun_leveys))
            pygame.draw.line(self._ikkuna, NAPPLUOIDEN_VARI,
                             (x+self._ruudun_leveys, y), (x, y+self._ruudun_leveys))

    def piirra_lauta(self):

        self._ikkuna.fill(LAUDAN_VARI)
        self._piirra_viivat()
        self._piirra_nollat()
        self._piirra_ristit()
        pygame.display.flip()
