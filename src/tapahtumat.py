import pygame


class Tapahtumat:
    """Luokka joka hoitaa hiiren ja näppäimistön interaktiot"""

    def __init__(self) -> None:
        self.hiiren_paikka = None
        self._hiirta_klikattu = False

    def get_tapahtumat(self) -> dict:
        """kerää hiiren ja näppäimistön tapahtumat

        Returns:
            dict: avain: näppäimistön komennot (str), arvo: bool
        """
        tapahtumat = {"lopeta": False, "takaisin": False, "pelaa_uudelleen": False}
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                tapahtumat["lopeta"] = True

            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_ESCAPE:
                    tapahtumat["takaisin"] = True

                if tapahtuma.key == pygame.K_r:
                    tapahtumat["pelaa_uudelleen"] = True

            if tapahtuma.type == pygame.MOUSEBUTTONDOWN and tapahtuma.button == 1:
                self._hiirta_klikattu = True
        return tapahtumat

    def hiirta_klikattu(self) -> bool:
        """Kertoo onko hiirta klikattu viimeisen tarkistuksen jälkeen"""
        muisti = self._hiirta_klikattu
        self._hiirta_klikattu = False
        return muisti

    def get_hiiren_paikka(self):
        """Palauttaa hiiren paikan ruudulla"""
        return pygame.mouse.get_pos()

    def palauta_nappaimiston_komento(self):
        """Palauttaa avain-arvo parin jossa on napin nimi-aktio"""
        tapahtumat = self.get_tapahtumat()
        for avain, arvo in tapahtumat.items():
            if arvo:
                return avain
        return None
