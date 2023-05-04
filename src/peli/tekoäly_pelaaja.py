import random
from copy import deepcopy
from tekoäly.minimax import Tekoaly


class TekoalyPelaaja:
    """Minimax algoritmin käyttöliittymä peliin
    """

    def __init__(
            self,
            merkit: list,
            lauta: list,
            siirrot: list,
            vapaat_ruudut: set,
            tarkista_voitto,
            maksimoiva_merkki: str,
            minimoiva_merkki: str,
            syvyys: int
    ) -> None:
        self.merkit = merkit  # kaikki tämän pelaajan ristit tai nollat
        self.lauta = lauta
        self.siirrot = siirrot  # kaikki siirrot jota pelissä on tehty
        self.vapaat_ruudut = vapaat_ruudut

        # tekoälylle etsittävät kaikki ruudut jotka
        # on 2 ruudun päässä nykyisistä ruuduista
        self.ruudut_joista_etsitaan_siirtoja = []

        # samat ruudut kuin ruudut_joista_etsitaan_siirtoja
        # mutta hajautustaulu nopeuttaa etsimistä
        self.siirroissa_olevat_ruudut = set()
        self.tekoaly = Tekoaly(
            tarkista_voitto,
            maksimoiva_merkki,
            minimoiva_merkki,
            syvyys)
        self.merkki = maksimoiva_merkki
        self.syvyys = syvyys

    def valitse_ruutu(self) -> tuple:
        if len(self.siirrot) == 0:
            return self._aloitus_siirto(n=len(self.lauta))
        viimeisin_siirto = self.siirrot[-1]
        lauta = deepcopy(self.lauta)

        heuristinen_arvo = self.tekoaly.heuristinen_funktio(lauta)

        vapaat_ruudut = self.vapaat_ruudut.copy()

        # poistaa edellisen pelaajan siirron mahdollisista siiroista
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(
            viimeisin_siirto)

        self.ruudut_joista_etsitaan_siirtoja, self.siirroissa_olevat_ruudut = self._lisaa_etsittavat_siirrot_tekoalylle(
            viimeisin_siirto)

        alfa = float("-infinity")
        beeta = float("infinity")
        self.jarjesta_siirrot_ennen_minimax_algoritmia(lauta)
        arvo, siirto = self.tekoaly.minimax(
            self.syvyys,
            lauta,
            self.ruudut_joista_etsitaan_siirtoja,
            set(),
            vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            alfa,
            beeta,
            True,
            heuristinen_arvo)

        self.ruudut_joista_etsitaan_siirtoja, self.siirroissa_olevat_ruudut = self._lisaa_etsittavat_siirrot_tekoalylle(
            siirto)

        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(siirto)
        return siirto

    def _aloitus_siirto(self, n):
        siirto = random.randrange(3, n - 3), random.randrange(3, n - 3)
        self.ruudut_joista_etsitaan_siirtoja, self.siirroissa_olevat_ruudut = self._lisaa_etsittavat_siirrot_tekoalylle(
            siirto)
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(siirto)

        return siirto

    def jarjesta_siirrot_ennen_minimax_algoritmia(self, lauta):
        self.ruudut_joista_etsitaan_siirtoja.sort(
            key=lambda siirto: self.siirron_heuristinen_arvo(siirto, lauta))

    def _lisaa_etsittavat_siirrot_tekoalylle(
            self, viimeisin_siirto: tuple) -> tuple:
        """Tekoäly etsii kaikki ruudut, jotka ovat kahden ruudun pääsää jo laudalla olevista ruuduista
            Tämä metodi pitää kutsua jokaisen oikean siirron jälkeen jotta

        Args:
            viimeisin_siirto (tuple): x ja y koordinaatti

        Returns:
            _type_: (list, set)
        """
        return Tekoaly.etsi_siirrot(
            viimeisin_siirto,
            self.vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            self.ruudut_joista_etsitaan_siirtoja)

    def _poista_etsittavista_siirroista_viimeisin_oikea_siirto(
            self, viimeisin_siirto: tuple):
        if viimeisin_siirto in self.siirroissa_olevat_ruudut:
            self.ruudut_joista_etsitaan_siirtoja.remove(viimeisin_siirto)
            self.siirroissa_olevat_ruudut.remove(viimeisin_siirto)

    def siirron_heuristinen_arvo(self, siirto: tuple, lauta: list):
        lauta[siirto[1]][siirto[0]] = self.merkki
        heuristinen_arvo = self.tekoaly.heuristinen_funktio(lauta)
        lauta[siirto[1]][siirto[0]] = None
        return heuristinen_arvo

    @staticmethod
    def nimi() -> str:
        return "Tekoäly pelaaja"
