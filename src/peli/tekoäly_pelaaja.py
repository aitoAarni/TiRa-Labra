import random
from copy import deepcopy
from tekoäly.minimax import Tekoaly


class TekoalyPelaaja:
    def __init__(
            self,
            merkit,
            lauta,
            siirrot,
            vapaat_ruudut,
            tarkista_voitto,
            maksimoiva_merkki,
            minimoiva_merkki,
            syvyys
    ) -> None:
        self.merkit = merkit
        self.lauta = lauta
        self.siirrot = siirrot
        self.vapaat_ruudut = vapaat_ruudut
        self.ruudut_joista_etsitaan_siirtoja = []
        self.siirroissa_olevat_ruudut = set()
        self.tekoaly = Tekoaly(
            tarkista_voitto,
            maksimoiva_merkki,
            minimoiva_merkki, syvyys)
        self.merkki = maksimoiva_merkki
        self.syvyys = syvyys

    def valitse_ruutu(self):
        print(self.merkki, "laskee siirtoa...")

        if len(self.siirrot) == 0:
            return self._aloitus(n=len(self.lauta))
        viimeisin_siirto = self.siirrot[-1]

        lauta = deepcopy(self.lauta)
        vapaat_ruudut = self.vapaat_ruudut.copy()
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(
            viimeisin_siirto)
        self.ruudut_joista_etsitaan_siirtoja, self.siirroissa_olevat_ruudut = self._lisaa_etsittavat_siirrot_tekoalylle(
            viimeisin_siirto)
        alfa = float("-infinity")
        beeta = float("infinity")

        heurestinen_arvo, siirto = self.tekoaly.minimax(
            self.syvyys,
            lauta,
            self.ruudut_joista_etsitaan_siirtoja,
            set(),
            vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            alfa,
            beeta, True)
        self.ruudut_joista_etsitaan_siirtoja, self.siirroissa_olevat_ruudut = self._lisaa_etsittavat_siirrot_tekoalylle(
            siirto)
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(siirto)

        return siirto

    def _aloitus(self, n):
        siirto = random.randrange(0, n), random.randrange(0, n)
        self.ruudut_joista_etsitaan_siirtoja, self.siirroissa_olevat_ruudut = self._lisaa_etsittavat_siirrot_tekoalylle(
            siirto)
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(siirto)

        return siirto

    def _lisaa_etsittavat_siirrot_tekoalylle(self, viimeisin_siirto):

        return Tekoaly.etsi_siirrot(
            viimeisin_siirto,
            self.vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            self.ruudut_joista_etsitaan_siirtoja)

    def _poista_etsittavista_siirroista_viimeisin_oikea_siirto(
            self, viimeisin_siirto):
        if viimeisin_siirto in self.siirroissa_olevat_ruudut:
            self.ruudut_joista_etsitaan_siirtoja.remove(viimeisin_siirto)
            self.siirroissa_olevat_ruudut.remove(viimeisin_siirto)
