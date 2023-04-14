from copy import copy, deepcopy
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
            minimoiva_merkki) -> None:

        self.lauta = lauta
        self.siirrot = siirrot
        self.vapaat_ruudut = vapaat_ruudut
        self.ruudut_joista_etsitaan_siirtoja = []
        self.siirroissa_olevat_ruudut = set()
        self.tekoaly = Tekoaly(
            tarkista_voitto,
            maksimoiva_merkki,
            minimoiva_merkki)
        self.merkki = maksimoiva_merkki
        self.merkit = merkit

    def valitse_ruutu(self):
        lauta = deepcopy(self.lauta)
        vapaat_ruudut = self.vapaat_ruudut.copy()
        viimeisin_siirto = self.siirrot[-1]
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(
            viimeisin_siirto)
        self._lisaa_etsittavat_siirrot_tekoalylle(viimeisin_siirto)
        alfa = float("-infinity")
        beeta = float("infinity")
        print("laskee siirtoa...")

        heurestinen_arvo, siirto = self.tekoaly.minimax(
            2,
            lauta,
            self.ruudut_joista_etsitaan_siirtoja,
            set(),
            vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            alfa,
            beeta,
            True)
        print(
            "siirto laskettu:",
            siirto,
            "  heurestinen arvo:",
            heurestinen_arvo)
        self._lisaa_etsittavat_siirrot_tekoalylle(siirto)
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(siirto)

        print(f"ruutu valittu. len(etsittavat_ruudut): {len(self.ruudut_joista_etsitaan_siirtoja)}")
        print("self.ruudut_joista_etsitaan_siirtoja")
        print(self.ruudut_joista_etsitaan_siirtoja)
        print()

        return siirto

    def _lisaa_etsittavat_siirrot_tekoalylle(self, viimeisin_siirto):

        Tekoaly.etsi_siirrot(
            viimeisin_siirto,
            self.vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            self.ruudut_joista_etsitaan_siirtoja)

    def _poista_etsittavista_siirroista_viimeisin_oikea_siirto(
            self, viimeisin_siirto):
        if viimeisin_siirto in self.siirroissa_olevat_ruudut:
            self.ruudut_joista_etsitaan_siirtoja.remove(viimeisin_siirto)
            self.siirroissa_olevat_ruudut.remove(viimeisin_siirto)
