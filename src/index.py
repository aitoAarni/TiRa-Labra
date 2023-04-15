import pygame
from konfiguraatio import get_konfiguraatio
from peli.tapahtumat import Tapahtumat
from peli.main import Peli
from peli.ihmis_pelaaja import Pelaaja
from kayttoliiittyma.lauta import Lauta
from peli.tekoäly_pelaaja import TekoalyPelaaja
FPS = 30

konffi = get_konfiguraatio()


class Sovellus:
    def __init__(self) -> None:
        pygame.init()
        ikkuna = pygame.display.set_mode((konffi["leveys"], konffi["korkeus"]))
        pygame.display.set_caption("Ristinolla")
        self.tapahtumat = Tapahtumat()
        self.peli = Peli(
            self.tapahtumat,
            TekoalyPelaaja,
            TekoalyPelaaja,
            Lauta,
            ikkuna
        )

    def main(self):
        kello = pygame.time.Clock()

        while True:
            kello.tick(FPS)
            self.peli.pelaa()
            break


if __name__ == "__main__":
    sovellus = Sovellus()
    sovellus.main()
