from konfiguraatio import get_konfiguraatio
from peli.ihmis_pelaaja import Pelaaja
from peli.tekoäly_pelaaja import TekoalyPelaaja
from peli.tapahtumat import Tapahtumat
from käyttöliittymä.lauta_ui import LautaUI
import pygame.display

konffi = get_konfiguraatio()


class Peli:
    """Pelilogiikka on tämän luokan sisällä."""

    def __init__(
        self,
        tapahtumat: Tapahtumat,
        pelaaja1: Pelaaja | TekoalyPelaaja,
        pelaaja2: Pelaaja | TekoalyPelaaja,
        lauta: LautaUI,
        ikkuna: pygame.display,
    ) -> None:
        self.tapahtumat = tapahtumat
        self.ristit = []
        self.nollat = []
        self.lauta_ui = lauta(ikkuna, self.ristit, self.nollat)
        self.lauta = [
            [None for _ in range(konffi.ruutujen_maara)]
            for _ in range(konffi.ruutujen_maara)
        ]
        self.vapaat_ruudut = set()
        for x in range(konffi.ruutujen_maara):
            for y in range(konffi.ruutujen_maara):
                self.vapaat_ruudut.add((x, y))
        self.siirrot = []
        pelaaja1 = self._alusta_pelaaja(pelaaja1, "x", self.ristit)
        pelaaja2 = self._alusta_pelaaja(pelaaja2, "0", self.nollat)
        self.pelaajat = [pelaaja1, pelaaja2]

    def _alusta_pelaaja(self, pelaaja, merkki, merkit):
        saa_minimoiva_merkki = {"x": "0", "0": "x"}
        if pelaaja is Pelaaja:
            return pelaaja(
                self.tapahtumat.hiirta_klikattu,
                self.tapahtumat.get_hiiren_paikka,
                merkki,
                merkit,
                konffi.ruutujen_maara,
            )

        elif pelaaja is TekoalyPelaaja:
            return pelaaja(
                merkit,
                self.lauta,
                self.siirrot,
                self.vapaat_ruudut,
                Peli.tarkista_voitto,
                merkki,
                saa_minimoiva_merkki[merkki],
                3,
            )

    @staticmethod
    def tarkista_voitto(viimeisin_siirto: tuple, merkki: str, lauta: list) -> bool:
        x, y = viimeisin_siirto
        n = konffi.ruutujen_maara - 1

        a = min(y, n - x)
        x_vino_oikea = x + a
        y_vino_oikea = y - a

        b = min(y, x)
        x_vino_vasen = x - b
        y_vino_vasen = y - b

        pysty = 0
        vaaka = 0
        vino_vasen = 0
        vino_oikea = 0

        for i in range(konffi.ruutujen_maara):
            if lauta[i][x] == merkki:
                pysty += 1
            else:
                pysty = 0

            if lauta[y][i] == merkki:
                vaaka += 1
            else:
                vaaka = 0
            if (
                x_vino_vasen + i <= n
                and y_vino_vasen + i <= n
                and lauta[y_vino_vasen + i][x_vino_vasen + i] == merkki
            ):
                vino_vasen += 1
            else:
                vino_vasen = 0
            if (
                x_vino_oikea - i >= 0
                and y_vino_oikea + i <= n
                and lauta[y_vino_oikea + i][x_vino_oikea - i] == merkki
            ):
                vino_oikea += 1
            else:
                vino_oikea = 0

            if 5 in (pysty, vaaka, vino_vasen, vino_oikea):
                return True
        return False

    def tarkista_tasapeli(self) -> bool:
        return konffi.ruutujen_maara**2 <= len(self.siirrot)

    def tarkista_onko_peli_paattynyt(
        self, viimeisin_siirto: tuple, merkki: str, lauta: list
    ) -> tuple:
        if self.tarkista_voitto(viimeisin_siirto, merkki, lauta):
            return True, merkki
        if self.tarkista_tasapeli():
            return True, "-"
        return False, None

    def valitse_ruutu(self, vuoro: int) -> tuple | None:
        pelaaja = self.pelaajat[vuoro]
        ruutu = pelaaja.valitse_ruutu()
        if ruutu:
            if self.lauta[ruutu[1]][ruutu[0]] is None:
                self.lauta[ruutu[1]][ruutu[0]] = pelaaja.merkki
                self.siirrot.append(ruutu)
                self.vapaat_ruudut.remove(ruutu)
                pelaaja.merkit.append((ruutu[1], ruutu[0]))

                return ruutu
        return None

    def pelaa_vuoro(self, vuoro: int):
        return self.valitse_ruutu(vuoro)

    def vaihda_vuoroa(self, vuoro: int):
        return (vuoro + 1) % 2
