import pygame
from config import lEVEYS, KORKEUS
from peli.tapahtumat import Tapahtumat
from peli.main import Peli
from peli.ihmis_pelaaja import Pelaaja
from kayttoliiittyma.lauta import Lauta
FPS = 144


class Sovellus:
    def __init__(self) -> None:
        pygame.init()
        ikkuna = pygame.display.set_mode((lEVEYS, KORKEUS))
        pygame.display.set_caption("Ristinolla")
        self.tapahtumat = Tapahtumat()
        self.peli = Peli(self.tapahtumat, Pelaaja(self.tapahtumat.hiirta_klikattu, self.tapahtumat.get_hiiren_paikka), Pelaaja(
            self.tapahtumat.hiirta_klikattu, self.tapahtumat.get_hiiren_paikka), Lauta, ikkuna)

    def main(self):
        kello = pygame.time.Clock()

        while True:
            kello.tick(FPS)
            self.peli.pelaa()
            break


sovellus = Sovellus()
sovellus.main()
