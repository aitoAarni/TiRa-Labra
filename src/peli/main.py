from konfiguraatio import get_konfiguraatio
from tekoäly.minimax import Tekoaly
from peli.ihmis_pelaaja import Pelaaja
from peli.tekoäly_pelaaja import TekoalyPelaaja
konffi = get_konfiguraatio()

RUUTUJEN_MAARA = konffi["ruutujen_määrä"]


class Peli:
    def __init__(self, tapahtumat, pelaaja1, pelaaja2, lauta, ikkuna) -> None:
        self.ai = Tekoaly(Peli.tarkista_voitto)
        self.tapahtumat = tapahtumat
        self.ristit = []
        self.nollat = []
        self.lauta_ui = lauta(ikkuna, self.ristit, self.nollat)
        self.lauta = [[None for _ in range(
            RUUTUJEN_MAARA)] for _ in range(RUUTUJEN_MAARA)]
        self.vapaat_ruudut = set()
        for x in range(RUUTUJEN_MAARA):
            for y in range(RUUTUJEN_MAARA):
                self.vapaat_ruudut.add((x,y))
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
                RUUTUJEN_MAARA)

        elif pelaaja is TekoalyPelaaja:
            return pelaaja(
                merkit,
                self.lauta,
                self.siirrot,
                self.vapaat_ruudut,
                Peli.tarkista_voitto,
                merkki,
                saa_minimoiva_merkki[merkki])

    @staticmethod
    def tarkista_voitto(viimeisin_siirto, merkki, lauta):
        x, y = viimeisin_siirto
        n = RUUTUJEN_MAARA - 1

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

        for i in range(konffi["ruutujen_määrä"]):
            if lauta[i][x] == merkki:
                pysty += 1
            else:
                pysty = 0

            if lauta[y][i] == merkki:
                vaaka += 1
            else:
                vaaka = 0
            if x_vino_vasen + i <= n and y_vino_vasen + \
                    i <= n and lauta[y_vino_vasen + i][x_vino_vasen + i] == merkki:
                vino_vasen += 1
            else:
                vino_vasen = 0
            if x_vino_oikea - i >= 0 and y_vino_oikea + \
                    i <= n and lauta[y_vino_oikea + i][x_vino_oikea - i] == merkki:
                vino_oikea += 1
            else:
                vino_oikea = 0

            if 5 in (pysty, vaaka, vino_vasen, vino_oikea):
                return True
        return False

    def valitse_ruutu(self, vuoro):
        pelaaja = self.pelaajat[vuoro]
        ruutu = pelaaja.valitse_ruutu()
        if ruutu:
            if self.lauta[ruutu[1]][ruutu[0]] is None:
                self.lauta[ruutu[1]][ruutu[0]] = pelaaja.merkki
                self.siirrot.append(ruutu)
                self.vapaat_ruudut.remove(ruutu)
                pelaaja.merkit.append((ruutu[1], ruutu[0]))

                print(self.ai.heurestinen_funktio(self.lauta))
                return ruutu
        return None

    def pelaa_vuoro(self, vuoro):
        return self.valitse_ruutu(vuoro)

    def vaihda_vuoroa(self, vuoro):
        return (vuoro + 1) % 2

    def pelaa(self):
        self.lauta_ui.piirra_lauta()
        loppu = False
        vuoro = 0
        while True:
            while True:
                tapahtumat = self.tapahtumat.get_tapahtumat()
                if tapahtumat["lopeta"] or tapahtumat["takaisin"]:
                    loppu = True
                    break
                siirto = self.pelaa_vuoro(vuoro)
                if siirto:
                    if self.tarkista_voitto(
                            siirto,
                            self.pelaajat[vuoro].merkki,
                            self.lauta):
                        loppu = True
                    break
            if loppu:
                break
            vuoro = self.vaihda_vuoroa(vuoro)
            self.lauta_ui.piirra_lauta()
        self.lauta_ui.tee_voittoteksti(self.pelaajat[vuoro].merkki)
        while True:
            self.lauta_ui.piirra_lauta()
            tapahtumat = self.tapahtumat.get_tapahtumat()
            if tapahtumat["lopeta"] or tapahtumat["takaisin"]:
                break
