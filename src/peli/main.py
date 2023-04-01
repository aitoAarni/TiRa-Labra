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
                "nappulat": self.ristit
            },
            {
                "pelaaja": pelaaja2,
                "nappulat": self.nollat
            }
        ]

        self.vuoro = 0
        self.vapaana = [[True for _ in range(
            RUUTUJEN_MAARA)] for _ in range(RUUTUJEN_MAARA)]

    def valitse_ruutu(self, vuoro):
        pelaaja = self.pelaajat[vuoro]
        ruutu = pelaaja["pelaaja"].get_ruutu()
        if ruutu:
            if self.vapaana[ruutu[1]][ruutu[0]]:
                self.vapaana[ruutu[1]][ruutu[0]] = False
                pelaaja["nappulat"].append((ruutu[1], ruutu[0]))
                return True
        return False

    def pelaa_vuoro(self, vuoro):
        return self.valitse_ruutu(vuoro)

    def vaihda_vuoroa(self, vuoro):
        return (vuoro + 1) % 2

    def pelaa(self):
        self.lauta.piirra_lauta()
        self.loppu = False
        vuoro = 0
        while not self.loppu:
            while True:
                tapahtumat = self.tapahtumat.get_tapahtumat()
                if tapahtumat["lopeta"] or tapahtumat["takaisin"]:
                    self.loppu = True
                elif self.pelaa_vuoro(vuoro):
                    print("breakki")
                    break
            vuoro = self.vaihda_vuoroa(vuoro)
            self.lauta.piirra_lauta()
