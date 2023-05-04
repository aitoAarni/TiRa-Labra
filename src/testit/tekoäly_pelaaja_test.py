import unittest
from peli.tekoäly_pelaaja import TekoalyPelaaja
from konfiguraatio import get_konfiguraatio
from peli.peli_logiikka import Peli

konffi = get_konfiguraatio()
RUUTUJEN_MAARA = konffi["ruutujen_määrä"]


def tee_pelitilanne(*siirrot):
    lauta = [[None for _ in range(RUUTUJEN_MAARA)]
             for _ in range(RUUTUJEN_MAARA)]
    vapaat_ruudut = set()
    for x in range(RUUTUJEN_MAARA):
        for y in range(RUUTUJEN_MAARA):
            vapaat_ruudut.add((x, y))
    merkit = ["x", "0"]
    for i, siirto in enumerate(siirrot):
        vapaat_ruudut.remove((siirto))
        lauta[siirto[1]][siirto[0]] = merkit[i % 2]
    return lauta, merkit, siirrot[::2], vapaat_ruudut


class TestTekoalyPelaaja(unittest.TestCase):
    def setUp(self):
        lauta, merkit, siirrot, vapaat_ruudut = tee_pelitilanne(
            (5, 5), (5, 6), (4, 5), (5, 7))
        self.tekoaly_pelaaja = TekoalyPelaaja(
            merkit,
            lauta,
            siirrot,
            vapaat_ruudut,
            Peli.tarkista_voitto,
            "x",
            "0",
            2)

    def test_valitse_ruutu_palauttaa_siirron(self):
        ruutu = self.tekoaly_pelaaja.valitse_ruutu()
        self.assertEqual(ruutu, (6, 5))

    def test_tyhjalle_laudalle_siirto_onnistuu(self):
        lauta, m, s, vapaat_ruudut = tee_pelitilanne()
        tko_aly = TekoalyPelaaja(
            [],
            lauta,
            [],
            vapaat_ruudut,
            Peli.tarkista_voitto,
            "x",
            "0",
            1)
        siirto = tko_aly.valitse_ruutu()
        self.assertEqual(type(siirto), tuple)
