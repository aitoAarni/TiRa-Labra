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

        pysty = HeurestisenArvonLaskija(
            self.maksimoiva_merkki, self.minimoiva_merkki)
        vaaka = HeurestisenArvonLaskija(
            self.maksimoiva_merkki, self.minimoiva_merkki)
        vino_oikea = HeurestisenArvonLaskija(
            self.maksimoiva_merkki, self.minimoiva_merkki)
        vino_vasen = HeurestisenArvonLaskija(
            self.maksimoiva_merkki, self.minimoiva_merkki)

        for a in range(self.n):
            pysty.laskemisen_alustus()
            vaaka.laskemisen_alustus()
            vino_oikea.laskemisen_alustus()
            vino_vasen.laskemisen_alustus()
            for b in range(self.n):

                pysty_merkki = pelilauta[b][a]
                vaaka_merkki = pelilauta[a][b]

                pysty.laske_arvo(pysty_merkki, (a, b - 1))
                vaaka.laske_arvo(vaaka_merkki, (b - 1, a))
            pysty.viimeisen_ruudun_tarkistus()
            vaaka.viimeisen_ruudun_tarkistus()

        # Looppaa kaikki vinot rivit läpi jossa voi olla 5 merkkiä peräkkäin
        for i in range(self.n * 2 - 10 + 1):
            # tämä looppaa aina oikean verran ruutuja per vino rivi
            # 5, 6, 7, ..., self.n-1, self.n, self.n-1,..., 7, 6, 5 ruutua
            for j in range(self.n - abs(self.n - 5 - i)):

                x_akseli1 = min(i + 4, self.n - 1) - j
                y_akseli1 = max(0, -self.n + 5 + i) + j
                x_akseli2 = max(0, self.n - 5 - i) + j
                y_akseli2 = max(0, -self.n + 5 + i) + j

                vino_oikea_merkki = pelilauta[y_akseli1][x_akseli1]
                vino_vasen_merkki = pelilauta[y_akseli2][y_akseli2]

                vino_oikea.laske_arvo(
                    vino_oikea_merkki, (x_akseli1 + 1, y_akseli1 - 1))
                vino_vasen.laske_arvo(
                    vino_vasen_merkki, (x_akseli2 - 1, y_akseli2 - 1))
            vino_oikea.viimeisen_ruudun_tarkistus()
            vino_vasen.viimeisen_ruudun_tarkistus()

        HeurestisenArvonLaskija.yksi_perakkain.clear()
        return pysty.heurestinen_arvo + vaaka.heurestinen_arvo + \
            vino_oikea.heurestinen_arvo + vino_vasen.heurestinen_arvo


class HeurestisenArvonLaskija:

    yksi_perakkain = set()

    def __init__(self, maksimoiva_merkki, minimoiva_merkki) -> None:
        self.maksimoiva_merkki = maksimoiva_merkki
        self.minimoiva_merkki = minimoiva_merkki
        self.heurestinen_arvo = 0
        self.viimeinen_tyhja_ruutu = None
        self.maksimoivia_palasia_perakkain = None
        self.minimoivia_palasia_perakkain = None
        self._ruutu_numero = 0

    def laske_arvo(self, merkki, edeltava_ruutu):

        if merkki == self.maksimoiva_merkki:
            self.maksimoivia_palasia_perakkain += 1
            # jos minimoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen maksivoiva merkki
            # niin vähennä heurestista arvoa palasten pituudella
            if self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - \
                    self.minimoivia_palasia_perakkain and self.minimoivia_palasia_perakkain > 1:

                self.heurestinen_arvo -= self.minimoivia_palasia_perakkain
            self.minimoivia_palasia_perakkain = 0

        elif merkki == self.minimoiva_merkki:
            self.minimoivia_palasia_perakkain += 1
            # jos maksivoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen minivoiva merkki
            # niin lisää heurestiseen arvoon palasten pituus
            if self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - \
                    self.maksimoivia_palasia_perakkain and self.maksimoivia_palasia_perakkain > 1:

                self.heurestinen_arvo += self.maksimoivia_palasia_perakkain
            self.maksimoivia_palasia_perakkain = 0

        else:
            # jos minivoivia merkkejä on välissä ja molemmilla puolilla on tyhjä ruutu
            # niin vähennä heurestisesta arvosta 2 * pituus
            if self.viimeinen_tyhja_ruutu == self._ruutu_numero - \
                    1 - self.minimoivia_palasia_perakkain:

                if self.minimoivia_palasia_perakkain == 1:
                    if edeltava_ruutu in self.yksi_perakkain:
                        pass
                    else:
                        self.yksi_perakkain.add(edeltava_ruutu)
                        self.heurestinen_arvo -= self.minimoivia_palasia_perakkain * 2
                else:
                    self.heurestinen_arvo -= self.minimoivia_palasia_perakkain * 2

            # jos maskivoivia merkkejä on välissä ja molemmilla puolilla on tyhjä ruutu
            # niin lisää heurestiseen arvoon 2 * pituus
            elif self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.maksimoivia_palasia_perakkain:

                if self.maksimoivia_palasia_perakkain == 1:
                    if edeltava_ruutu in self.yksi_perakkain:
                        pass
                    else:
                        self.yksi_perakkain.add(edeltava_ruutu)
                        self.heurestinen_arvo += self.maksimoivia_palasia_perakkain * 2
                else:
                    self.heurestinen_arvo += self.maksimoivia_palasia_perakkain * 2

            elif 1 not in (self.maksimoivia_palasia_perakkain, self.minimoivia_palasia_perakkain):
                self.heurestinen_arvo -= self.minimoivia_palasia_perakkain
                self.heurestinen_arvo += self.maksimoivia_palasia_perakkain

            self.viimeinen_tyhja_ruutu = self._ruutu_numero
            self.minimoivia_palasia_perakkain = self.maksimoivia_palasia_perakkain = 0
        self._ruutu_numero += 1

    def laskemisen_alustus(self):
        self.viimeinen_tyhja_ruutu = float("-infinity")
        self.maksimoivia_palasia_perakkain = 0
        self.minimoivia_palasia_perakkain = 0
        self._ruutu_numero = 0

    def viimeisen_ruudun_tarkistus(self):
        if self.viimeinen_tyhja_ruutu == self._ruutu_numero - \
                1 - self.minimoivia_palasia_perakkain:
            self.heurestinen_arvo -= self.minimoivia_palasia_perakkain
        if self.viimeinen_tyhja_ruutu == self._ruutu_numero - \
                1 - self.maksimoivia_palasia_perakkain:
            self.heurestinen_arvo += self.maksimoivia_palasia_perakkain
