from config import RUUTUJEN_MAARA


class Peli:
    def __init__(self, tapahtumat, pelaaja1, pelaaja2, lauta, ikkuna) -> None:
        self.tapahtumat = tapahtumat
        self.ristit = []
        self.nollat = []
        self.lauta = lauta(ikkuna, self.ristit, self.nollat)
        self.pelaajat = [

            {
                "pelaaja": pelaaja1,
                "nappulat": self.ristit,
                "merkki": "x"
            },
            {
                "pelaaja": pelaaja2,
                "nappulat": self.nollat,
                "merkki": "0"
            }
        ]

        self.ristit_ja_nollat = [[None for _ in range(
            RUUTUJEN_MAARA)] for _ in range(RUUTUJEN_MAARA)]

    def tarkista_voitto(self, viimeisin_siirto, merkki):
        x, y = viimeisin_siirto

        n = RUUTUJEN_MAARA - 1

        a = min(y, n-x)
        x_vino_oikea = x+a
        y_vino_oikea = y-a

        b = min(y, x)
        x_vino_vasen = x - b
        y_vino_vasen = y - b

        pysty = 0
        vaaka = 0
        vino_vasen = 0
        vino_oikea = 0

        for i in range(RUUTUJEN_MAARA):
            if self.ristit_ja_nollat[i][x] == merkki:
                pysty += 1
            else:
                pysty = 0

            if self.ristit_ja_nollat[y][i] == merkki:
                vaaka += 1
            else:
                vaaka = 0
            if x_vino_vasen + i <= n and y_vino_vasen + i <= n and self.ristit_ja_nollat[y_vino_vasen + i][x_vino_vasen + i] == merkki:
                vino_vasen += 1
            else:
                vino_vasen = 0
            if x_vino_oikea - i >= 0 and y_vino_oikea + i <= n and self.ristit_ja_nollat[y_vino_oikea + i][x_vino_oikea-i] == merkki:
                vino_oikea += 1
            else:
                vino_oikea = 0

            if 5 in (pysty, vaaka, vino_vasen, vino_oikea):
                return True
        return False

    def valitse_ruutu(self, vuoro):
        pelaaja = self.pelaajat[vuoro]
        ruutu = pelaaja["pelaaja"].get_ruutu()
        if ruutu:
            if self.ristit_ja_nollat[ruutu[1]][ruutu[0]] is None:
                self.ristit_ja_nollat[ruutu[1]][ruutu[0]] = pelaaja["merkki"]
                pelaaja["nappulat"].append((ruutu[1], ruutu[0]))
                return ruutu
        return None

    def pelaa_vuoro(self, vuoro):
        return self.valitse_ruutu(vuoro)

    def vaihda_vuoroa(self, vuoro):
        return (vuoro + 1) % 2

    def pelaa(self):
        self.lauta.piirra_lauta()
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
                    if self.tarkista_voitto(siirto, self.pelaajat[vuoro]["merkki"]):
                        loppu = True
                    break
            if loppu:
                break
            vuoro = self.vaihda_vuoroa(vuoro)
            self.lauta.piirra_lauta()
        self.lauta.tee_voittoteksti(self.pelaajat[vuoro]["merkki"])
        while True:
            self.lauta.piirra_lauta()
            tapahtumat = self.tapahtumat.get_tapahtumat()
            if tapahtumat["lopeta"] or tapahtumat["takaisin"]:
                break
