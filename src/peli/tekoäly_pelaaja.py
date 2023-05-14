import random
from copy import deepcopy
from tekoäly.minimax import Tekoaly
from apuvälineet import lataus_baari_cli, jarjesta_lista_toisen_listan_avulla


class TekoalyPelaaja:
    """Tekoälyn käyttöliittymä peliin"""

    def __init__(
        self,
        merkit: list,
        lauta: list,
        tarkista_voitto,
        maksimoiva_merkki: str,
        minimoiva_merkki: str,
        maksimi_syvyys: int,
    ) -> None:
        self.merkit = merkit  # kaikki tämän pelaajan ristit tai nollat
        self.lauta = lauta

        self.tekoaly = Tekoaly(
            tarkista_voitto, maksimoiva_merkki, minimoiva_merkki, maksimi_syvyys
        )
        self.merkki = maksimoiva_merkki
        self.syvyys = maksimi_syvyys

    def valitse_ruutu(self) -> tuple:
        """Palauttaa ruudun, johon seuraava siirto tehdään"""
        lauta = deepcopy(self.lauta)

        if self.onko_ensimmäinen_siirto(lauta):
            return self._aloitus_siirto(n=len(self.lauta))

        heuristinen_arvo = self.tekoaly.heuristinen_funktio(lauta, self.syvyys)

        pelin_siirrot, vapaat_ruudut = self.etsi_siirrot_ja_vapaat_ruudut(lauta)

        (
            tekoalyn_etsittavat_ruudut,
            tekoalyn_etsittavat_ruudut_hajautus_taulu,
        ) = self._lisaa_etsittavat_siirrot_tekoalylle(pelin_siirrot, vapaat_ruudut)
        self.tekoaly.aloita_vuoro()
        for syvyys in range(2, self.syvyys + 1):
            print(" " * 122, end="\r")
            siirtojen_arvot = self.palauta_siirtojen_arvot(
                syvyys,
                lauta,
                tekoalyn_etsittavat_ruudut,
                tekoalyn_etsittavat_ruudut_hajautus_taulu,
                vapaat_ruudut,
                heuristinen_arvo,
            )
            if siirtojen_arvot == None:
                break
            tekoalyn_etsittavat_ruudut = jarjesta_lista_toisen_listan_avulla(
                tekoalyn_etsittavat_ruudut, siirtojen_arvot
            )

            paras_siirto = tekoalyn_etsittavat_ruudut[-1]
        return paras_siirto

    def palauta_siirtojen_arvot(
        self,
        syvyys,
        lauta,
        etsittavat_ruudut,
        etsittavat_ruudut_hajautus_taulu,
        vapaat_ruudut,
        heuristinen_arvo,
    ):
        alfa = float("-infinity")
        siirtojen_arvot = []
        for indeksi, siirto in enumerate(etsittavat_ruudut[::-1]):
            lataus_baari_cli(indeksi + 1, len(etsittavat_ruudut), syvyys)
            arvo = self.laske_siirron_paras_arvo(
                syvyys,
                siirto,
                lauta,
                etsittavat_ruudut,
                vapaat_ruudut,
                etsittavat_ruudut_hajautus_taulu,
                alfa,
                heuristinen_arvo,
            )
            siirtojen_arvot.append(arvo)
            if arvo == None:
                return None

            alfa = max(arvo, alfa)
        siirtojen_arvot.reverse()
        return siirtojen_arvot

    def laske_siirron_paras_arvo(
        self,
        syvyys,
        siirto,
        lauta,
        etsittavat_ruudut,
        vapaat_ruudut,
        etsittavat_ruudut_hajautus_taulu,
        alfa,
        heuristinen_arvo,
    ):
        (
            uudet_etsittavat_ruudut,
            uudet_etsittavat_ruudut_hajautus_taulu,
        ) = self.tekoaly.etsi_siirrot(
            siirto, vapaat_ruudut, etsittavat_ruudut_hajautus_taulu, etsittavat_ruudut
        )

        lauta[siirto[1]][siirto[0]] = self.merkki
        vapaat_ruudut.remove(siirto)
        uusi_heuristinen_arvo = heuristinen_arvo + self.tekoaly.heurstisen_arvon_delta(
            lauta, syvyys, siirto
        )
        arvo = self.tekoaly.minimax(
            syvyys - 1,
            lauta,
            uudet_etsittavat_ruudut,
            {siirto},
            vapaat_ruudut,
            uudet_etsittavat_ruudut_hajautus_taulu,
            alfa,
            float("infinity"),
            False,
            uusi_heuristinen_arvo,
            siirto,
        )
        lauta[siirto[1]][siirto[0]] = None
        vapaat_ruudut.add(siirto)
        return arvo

    def etsi_siirrot_ja_vapaat_ruudut(self, lauta):
        vapaat_ruudut = set()
        siirrot = []
        for y, rivi in enumerate(lauta):
            for x, ruutu in enumerate(rivi):
                if ruutu == None:
                    vapaat_ruudut.add((x, y))
                else:
                    siirrot.append((x, y))
        return siirrot, vapaat_ruudut

    def onko_ensimmäinen_siirto(self, lauta):
        for rivi in lauta:
            for merkki in rivi:
                if merkki != None:
                    return False
        return True

    def _aloitus_siirto(self, n):
        """Kun tekoäly on X ja tekee ensimmäistä siirtoa"""
        siirto = random.randrange(4, n - 4), random.randrange(4, n - 4)
        return siirto

    def _lisaa_etsittavat_siirrot_tekoalylle(
        self, siirrot: tuple, vapaat_ruudut
    ) -> tuple:
        """Tekoäly etsii kaikki ruudut, jotka ovat kahden ruudun pääsää
        viimeisimmästä siirrosta, joten metodi pitää kutsua jokaisen oikean siirron jälkeen

        Args:
            viimeisin_siirto (tuple): x ja y koordinaatti

        Returns:
            tuple: (list, set)
        """
        etsittavat_siirrot = []
        siirroissa_olevat_ruudut = set()
        for siirto in siirrot:
            etsittavat_siirrot, siirroissa_olevat_ruudut = Tekoaly.etsi_siirrot(
                siirto, vapaat_ruudut, siirroissa_olevat_ruudut, etsittavat_siirrot
            )
        return etsittavat_siirrot, siirroissa_olevat_ruudut

    @staticmethod
    def nimi() -> str:
        return "Tekoäly pelaaja"
