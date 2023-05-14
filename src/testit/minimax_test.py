import unittest
from unittest.mock import Mock
from tekoäly.minimax import Tekoaly


class TestMinimax(unittest.TestCase):
    def palauta_minimaxin_arvo(self):
        pelatus_siirrot = [(4, 4, "x"), (5, 4, "x"), (4, 3, "0"), (3, 3, "0")]
        vapaa_ruudut = set()
        for x in range(self.n):
            for y in range(self.n):
                vapaa_ruudut.add((x, y))
        lauta = [[None for _ in range(self.n)] for _ in range(self.n)]
        for x, y, merkki in pelatus_siirrot:
            vapaa_ruudut.remove((x, y))
            lauta[y][x] = merkki
        etsittavat_siirrot = []
        etsittavat_siirrot_h_taulu = set()
        for x, y, _ in pelatus_siirrot:
            etsittavat_siirrot, etsittavat_siirrot_h_taulu = Tekoaly.etsi_siirrot(
                (x, y), vapaa_ruudut, etsittavat_siirrot_h_taulu, etsittavat_siirrot
            )
        etsittavat_siirrot.remove((3, 5))
        etsittavat_siirrot_h_taulu.remove((3, 5))
        h_arvo = self.tekoaly.heuristinen_funktio(lauta, 2)
        arvo = self.tekoaly.minimax(
            1,
            lauta,
            etsittavat_siirrot,
            set((3, 5)),
            vapaa_ruudut,
            etsittavat_siirrot_h_taulu,
            float("-infinity"),
            float("infinity"),
            True,
            h_arvo,
            (3, 5),
        )
        return arvo

    def setUp(self):
        self.tarkista_voitto = Mock(return_value=False)
        self.n = 15
        self.tekoaly = Tekoaly(self.tarkista_voitto, "x", "0", 2)
        self.tekoaly.n = self.n

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.tekoaly), Tekoaly)

    def test_etsi_siirrot_palauttaa_oikeat_siirrot(self):
        siirrot = [(4, 5), (5, 7)]
        oikeat_siirrot = []
        oikeat_siirrot_hajautus_taulu = set()
        for x, y in siirrot:
            for x_delta in range(-2, 3):
                for y_delta in range(-2, 3):
                    siirto = x + x_delta, y + y_delta
                    if siirto in oikeat_siirrot_hajautus_taulu:
                        continue
                    oikeat_siirrot.append(siirto)
                    oikeat_siirrot_hajautus_taulu.add(siirto)

        vapaa_ruudut = set()
        for x in range(self.n):
            for y in range(self.n):
                vapaa_ruudut.add((x, y))
        saadut_siirrot = []
        saadut_siirrot_hajautus_taulu = set()
        for siirto in siirrot:
            saadut_siirrot, saadut_siirrot_hajautus_taulu = Tekoaly.etsi_siirrot(
                siirto, vapaa_ruudut, saadut_siirrot_hajautus_taulu, saadut_siirrot
            )
        saadut_siirrot.sort()
        oikeat_siirrot.sort()
        self.assertEqual(
            (saadut_siirrot, saadut_siirrot_hajautus_taulu),
            (oikeat_siirrot, oikeat_siirrot_hajautus_taulu),
        )

    def test_minimax_palauttaa_oikeat_arvot(self):
        self.tekoaly.aloita_vuoro()
        arvo = self.palauta_minimaxin_arvo()
        self.assertEqual(arvo, 1358.0)

    def test_minimax_pysahtyy_kun_aika_loppuu(self):
        self.tekoaly.aloita_vuoro()
        self.tekoaly.vuoron_alkuaika = -21
        arvo = self.palauta_minimaxin_arvo()
        self.assertEqual(arvo, None)
