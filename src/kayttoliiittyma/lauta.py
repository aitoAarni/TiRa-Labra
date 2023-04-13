from konfiguraatio import get_konfiguraatio
import pygame
import os

konffi = get_konfiguraatio()


class Lauta:
    def __init__(self, ikkuna, ristit, nollat) -> None:
        self._ikkuna = ikkuna
        self._ristit = ristit
        self._nollat = nollat
        self._ruudun_leveys = konffi["leveys"] / konffi["ruutujen_määrä"]
        self.voittoikkuna = None

    def _piirra_viivat(self):
        for i in range(1, konffi["ruutujen_määrä"]):
            x = self._ruudun_leveys * i
            y = 0

            pygame.draw.line(self._ikkuna, konffi["laudan_viivojen_väri"],
                             (x, y), (x, konffi["korkeus"]))
            pygame.draw.line(
                self._ikkuna, konffi["laudan_viivojen_väri"], (y, x), (konffi["leveys"], x))

    def _piirra_nollat(self):
        for rivi, sarake in self._nollat:
            keskipiste = (
                sarake *
                self._ruudun_leveys +
                self._ruudun_leveys /
                2,
                rivi *
                self._ruudun_leveys +
                self._ruudun_leveys /
                2)
            pygame.draw.circle(self._ikkuna, konffi["nappuloiden_väri"],
                               keskipiste, self._ruudun_leveys / 3, 3)

    def _piirra_ristit(self):
        for rivi, sarake in self._ristit:
            x, y = sarake * self._ruudun_leveys, rivi * self._ruudun_leveys
            pygame.draw.line(
                self._ikkuna,
                konffi["nappuloiden_väri"],
                (x, y),
                (x + self._ruudun_leveys, y + self._ruudun_leveys), 3)
            pygame.draw.line(
                self._ikkuna,
                konffi["nappuloiden_väri"],
                (x + self._ruudun_leveys, y),
                (x, y + self._ruudun_leveys), 3)

    def tee_voittoteksti(self, merkki):
        self.voittoikkuna = pygame.Surface(
            (konffi["leveys"], konffi["korkeus"]))
        if merkki == "x":
            merkin_nimi = "Ristit"
        else:
            merkin_nimi = "Nollat"
        merkkijono = f"{merkin_nimi} voitti!"
        fontti = pygame.font.Font(os.path.join(
            "materiaalit", "Wedgie Regular.ttf"), konffi["fontti"])
        teksti = fontti.render(merkkijono, True, konffi["voitto_tekstin_väri"])
        teksti_rect = teksti.get_rect()
        teksti_rect.center = (konffi["leveys"] / 2, konffi["korkeus"] / 2)
        self.voittoikkuna.set_alpha(200)
        self.voittoikkuna.fill(konffi["peli_ohi_väri"])
        self.voittoikkuna.blit(teksti, teksti_rect)

    def _piirra_voittonakyma(self):
        vari = konffi["peli_ohi_väri"]
        pygame.draw.rect(
            self._ikkuna,
            vari,
            (0,
             0,
             konffi["leveys"],
                konffi["korkeus"]))

    def piirra_lauta(self):

        self._ikkuna.fill(konffi["laudan_väri"])
        self._piirra_viivat()
        self._piirra_nollat()
        self._piirra_ristit()
        if self.voittoikkuna:
            self._ikkuna.blit(self.voittoikkuna, (0, 0))
        pygame.display.flip()
