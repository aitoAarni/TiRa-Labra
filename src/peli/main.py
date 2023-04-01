from config import RUUTUJEN_MAARA


class Peli:
    def __init__(self, tapahtumat, pelaaja1, pelaaja2, lauta, ikkuna) -> None:
        self.tapahtumat = tapahtumat
        self.lauta = lauta(ikkuna, self.ristit, self.nollat)
        self.ristit = []
        self.nollat = []

        self.risti = {
            "pelaaja": pelaaja1,
            "nappulat": self.ristit
        }

        self.nolla = {
            "pelaaja": pelaaja2,
            "nappulat": self.nollat
        }

        self.vuoro = 1
        self.vapaana = [[True for _ in range(
            RUUTUJEN_MAARA)] for _ in range(RUUTUJEN_MAARA)]

    def valitse_ruutu(self, pelaaja):

        while True:
            ruutu = pelaaja.get_ruutu()
            if ruutu:
                if self.vapaana[ruutu[1], ruutu[0]]:
                    self.vapaana[ruutu[1], ruutu[0]] = False
                if self.

    def vuoro(self, pelaaja):
        ruutu = self.valitse_ruutu(pelaaja)

    def pelaa(self):
        self.lauta.piirra_lauta()
        loppu = False
        while not loppu:
            tapahtumat = self.tapahtumat.get_tapahtumat()
            if tapahtumat["lopeta"]:
                loppu = True
            self.lauta.piirra_lauta()
