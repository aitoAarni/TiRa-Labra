from konfiguraatio import get_konfiguraatio
from peli.tapahtumat import Tapahtumat
konffi = get_konfiguraatio()
LEVEYS = konffi["leveys"]
KORKEUS = konffi["korkeus"]


class Pelaaja:
    """Luokka antaa käyttäjälle rajapinnan peliin,
    sekä säilöö joitakin tietoja pelaajan tilasta
    """

    def __init__(
            self,
            hiiren_klikki: Tapahtumat.hiirta_klikattu,
            hiiren_paikka: tuple,
            merkki: str,
            merkit: list,
            ruutujen_maara: int) -> None:
        self.hiirta_klikattu = hiiren_klikki
        self.hiiren_paikka = hiiren_paikka
        self.merkki = merkki
        self.merkit = merkit
        self.ruutujen_maara = ruutujen_maara

    def valitse_ruutu(self) -> tuple | None:
        x, y = self.hiiren_paikka()

        if self.hiirta_klikattu():
            x, y = self.hiiren_paikka()
            ruudun_leveys = LEVEYS / self.ruutujen_maara
            ruudun_korkeus = KORKEUS / self.ruutujen_maara
            rivi = round(x // ruudun_leveys)
            sarake = round(y // ruudun_korkeus)

            return rivi, sarake
        return None
