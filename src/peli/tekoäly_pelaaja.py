from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()


class Tekoaly:
    def __init__(self, pelitilanne=None) -> None:
        self.pelitilanne = pelitilanne
        self.maksimoiva_merkki = "x"
        self.minimoiva_merkki = "0"
        self.n = konffi["ruutujen_määrä"]

    def minimax(self, syvyys, a, b, maksimoiva_pelaaja):
        if syvyys == 0:
            return None

    def heurestinen_funktio(self, pelilauta):

        heurestinen_arvo = 0

        for x in range(self.n):
            maksimoivia_palasia_perakkain = 0
            minimoivia_palasia_perakkain = 0
            viimeinen_tyhja_ruutu = float("-infinity")
            for y in range(self.n):

                merkki = pelilauta[y][x]
                if merkki == self.maksimoiva_merkki:
                    maksimoivia_palasia_perakkain += 1
                    if viimeinen_tyhja_ruutu == y - 1 - minimoivia_palasia_perakkain:
                        heurestinen_arvo -= minimoivia_palasia_perakkain
                    minimoivia_palasia_perakkain = 0

                elif merkki == self.minimoiva_merkki:
                    minimoivia_palasia_perakkain += 1

                    if viimeinen_tyhja_ruutu == y - 1 - maksimoivia_palasia_perakkain:
                        heurestinen_arvo += maksimoivia_palasia_perakkain
                    maksimoivia_palasia_perakkain = 0

                else:
                    if viimeinen_tyhja_ruutu == y - 1 - minimoivia_palasia_perakkain:
                        heurestinen_arvo -= minimoivia_palasia_perakkain * 2
                    elif viimeinen_tyhja_ruutu == y - 1 - maksimoivia_palasia_perakkain:
                        heurestinen_arvo += maksimoivia_palasia_perakkain * 2
                    else:
                        heurestinen_arvo -= minimoivia_palasia_perakkain
                        heurestinen_arvo += maksimoivia_palasia_perakkain
                    viimeinen_tyhja_ruutu = y
                    minimoivia_palasia_perakkain = maksimoivia_palasia_perakkain = 0

            if viimeinen_tyhja_ruutu == y - 1 - minimoivia_palasia_perakkain:
                heurestinen_arvo -= minimoivia_palasia_perakkain
            if viimeinen_tyhja_ruutu == y - 1 - maksimoivia_palasia_perakkain:
                heurestinen_arvo += maksimoivia_palasia_perakkain

        return heurestinen_arvo


class Heurestiikka:
    def __init__(self, maksimoiva_merkki, minimoiva_merkki) -> None:
        self.maksimoiva_merkki = maksimoiva_merkki
        self.minimoiva_merkki = minimoiva_merkki
        self.heurestinen_arvo = 0
        self.viimeinen_tyhja_ruutu = None
        self.maksimoivia_palasia_perakkain = None
        self.minimoivia_palasia_perakkain = None
        self._ruutu_numero = 0

    def laske_arvo(self, merkki):
        self.viimeinen_tyhja_ruutu = float("-infinity")
        self.maksimoivia_palasia_perakkain = 0
        self.minimoivia_palasia_perakkain = 0

        if merkki == self.maksimoiva_merkki:
            self.maksimoivia_palasia_perakkain += 1
            if self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.minimoivia_palasia_perakkain:
                self.heurestinen_arvo -= self.minimoivia_palasia_perakkain
            self.minimoivia_palasia_perakkain = 0

        elif merkki == self.minimoiva_merkki:
            self.minimoivia_palasia_perakkain += 1

            if self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.maksimoivia_palasia_perakkain:
                self.heurestinen_arvo += self.maksimoivia_palasia_perakkain
            self.maksimoivia_palasia_perakkain = 0

        else:
            if self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.minimoivia_palasia_perakkain:
                self.heurestinen_arvo -= self.minimoivia_palasia_perakkain * 2
            elif self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.maksimoivia_palasia_perakkain:
                self.heurestinen_arvo += self.maksimoivia_palasia_perakkain * 2
            else:
                self.heurestinen_arvo -= self.minimoivia_palasia_perakkain
                self.heurestinen_arvo += self.maksimoivia_palasia_perakkain
            self.viimeinen_tyhja_ruutu = self._ruutu_numero
            self.minimoivia_palasia_perakkain = self.maksimoivia_palasia_perakkain = 0
        self._ruutu_numero += 1

    def alusta_ruutu_numero(self):
        self._ruutu_numero = 0

    def viimeisen_ruudun_tarkistus(self):
        if self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.minimoivia_palasia_perakkain:
            self.heurestinen_arvo -= self.minimoivia_palasia_perakkain
        if self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.maksimoivia_palasia_perakkain:
            self.heurestinen_arvo += self.maksimoivia_palasia_perakkain