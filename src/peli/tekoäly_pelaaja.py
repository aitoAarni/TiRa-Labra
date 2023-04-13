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
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(viimeisin_siirto)
        self._lisaa_etsittavat_siirrot_tekoalylle(viimeisin_siirto)
        print(f"viimeisin_ruutu {viimeisin_siirto} in self.ruudut_joista_etsitään_siirtoja: {viimeisin_siirto in self.ruudut_joista_etsitaan_siirtoja}")
        alfa = float("-infinity")
        beeta = float("infinity")
        print("laskee siirtoa...")
        try:
            siirto = self.tekoaly.minimax(
            3,
            lauta,
            self.ruudut_joista_etsitaan_siirtoja,
            set(),
            vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            alfa,
            beeta,
            True)[1]
        finally:
            print(f"laudalla olevat oikeet siirrot: {self.siirrot}")
            print(f"viimesin siirto {viimeisin_siirto} in self.vapaat_ruudut: {viimeisin_siirto in self.vapaat_ruudut}")
            print(f"self.ruudut_joista_etsitaan-siirtoja: {self.ruudut_joista_etsitaan_siirtoja}")
        #print("siirto laskettu:", siirto)
        self._lisaa_etsittavat_siirrot_tekoalylle(siirto)
        self._poista_etsittavista_siirroista_viimeisin_oikea_siirto(siirto)

        return siirto

    def _lisaa_etsittavat_siirrot_tekoalylle(self, viimeisin_siirto):
        
        Tekoaly.etsi_siirrot(
            viimeisin_siirto,
            self.vapaat_ruudut,
            self.siirroissa_olevat_ruudut,
            self.ruudut_joista_etsitaan_siirtoja)

    def _poista_etsittavista_siirroista_viimeisin_oikea_siirto(self, viimeisin_siirto):
        #print(f"viimeisin_siirto {viimeisin_siirto} in self.ruudut_joista_etsitään_siirtoja: {viimeisin_siirto in self.ruudut_joista_etsitaan_siirtoja}")
        if viimeisin_siirto in self.siirroissa_olevat_ruudut:
            try:
                #print(f"ruudut_joista_etsitaan_siirtoja.index(viimesin) {self.ruudut_joista_etsitaan_siirtoja.index(viimeisin_siirto)}")
                #print(f"poistetaan viimestä_siirtoa: {viimeisin_siirto}")
                self.ruudut_joista_etsitaan_siirtoja.remove(viimeisin_siirto)
                self.siirroissa_olevat_ruudut.remove(viimeisin_siirto)
                #print(f"ruudut_joista_etsitaan_siirtoja.index(viimesin) {self.ruudut_joista_etsitaan_siirtoja.index(viimeisin_siirto)}")
                #print(f"viimeisin_siirto {viimeisin_siirto} in self.ruudut_joista_etsitään_siirtoja: {viimeisin_siirto in self.ruudut_joista_etsitaan_siirtoja}")
            finally:
                print("value errori")
