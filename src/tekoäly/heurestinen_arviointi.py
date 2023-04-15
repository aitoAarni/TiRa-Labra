VOITTO_ARVO = 10**10


class HeurestisenArvonLaskija:

    yksi_perakkain = set()

    def __init__(
            self,
            maksimoiva_merkki,
            minimoiva_merkki,
            syvyys,
            maksimi_syvyys) -> None:
        self.maksimoiva_merkki = maksimoiva_merkki
        self.minimoiva_merkki = minimoiva_merkki
        self.heurestinen_arvo = 0
        self.viimeinen_tyhja_ruutu = None
        self.maksimoivia_palasia_perakkain = None
        self.minimoivia_palasia_perakkain = None
        self._ruutu_numero = 0
        self.syvyys = syvyys
        self.maksimi_syvyys = maksimi_syvyys

    def perakkaisten_ruutujen_arvot(self, perakkain, arvokas=False):
        voitto_arvo = VOITTO_ARVO - (self.maksimi_syvyys - self.syvyys) * 10**6

        arvot = {2: 10, 3: 100, 4: 1000, 5: voitto_arvo}
        if arvokas:
            arvot = {1: 10, 2: 100, 3: 1000, 4: 100000, 5: voitto_arvo}
        if perakkain in arvot.keys():
            return arvot[perakkain]
        if perakkain < 2:
            return 0
        return voitto_arvo

    def laske_arvo(self, merkki, edeltava_ruutu):

        if merkki == self.maksimoiva_merkki:
            self.maksimoivia_palasia_perakkain += 1
            # jos minimoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen maksivoiva merkki
            # niin vähennä heurestista arvoa palasten pituudella
            if (self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 -
                    self.minimoivia_palasia_perakkain and self.minimoivia_palasia_perakkain > 1) or self.minimoivia_palasia_perakkain >= 5:

                self.heurestinen_arvo -= self.perakkaisten_ruutujen_arvot(
                    self.minimoivia_palasia_perakkain)
            self.minimoivia_palasia_perakkain = 0

        elif merkki == self.minimoiva_merkki:
            self.minimoivia_palasia_perakkain += 1
            # jos maksivoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen minivoiva merkki
            # niin lisää heurestiseen arvoon palasten pituus
            if (self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 -
                    self.maksimoivia_palasia_perakkain and self.maksimoivia_palasia_perakkain > 1) or self.maksimoivia_palasia_perakkain >= 5:

                self.heurestinen_arvo += self.perakkaisten_ruutujen_arvot(
                    self.maksimoivia_palasia_perakkain)
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
                        self.heurestinen_arvo -= self.perakkaisten_ruutujen_arvot(
                            self.minimoivia_palasia_perakkain, True)
                else:
                    self.heurestinen_arvo -= self.perakkaisten_ruutujen_arvot(
                        self.minimoivia_palasia_perakkain, True)

            # jos maskivoivia merkkejä on välissä ja molemmilla puolilla on tyhjä ruutu
            # niin lisää heurestiseen arvoon 2 * pituus
            elif self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.maksimoivia_palasia_perakkain:

                if self.maksimoivia_palasia_perakkain == 1:
                    if edeltava_ruutu in self.yksi_perakkain:
                        pass
                    else:
                        self.yksi_perakkain.add(edeltava_ruutu)
                        self.heurestinen_arvo += self.perakkaisten_ruutujen_arvot(
                            self.maksimoivia_palasia_perakkain, True)
                else:
                    self.heurestinen_arvo += self.perakkaisten_ruutujen_arvot(
                        self.maksimoivia_palasia_perakkain, True)

            elif 1 not in (self.maksimoivia_palasia_perakkain, self.minimoivia_palasia_perakkain):
                self.heurestinen_arvo -= self.perakkaisten_ruutujen_arvot(
                    self.minimoivia_palasia_perakkain)
                self.heurestinen_arvo += self.perakkaisten_ruutujen_arvot(
                    self.maksimoivia_palasia_perakkain)

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
            self.heurestinen_arvo -= self.perakkaisten_ruutujen_arvot(
                self.minimoivia_palasia_perakkain)
        if self.viimeinen_tyhja_ruutu == self._ruutu_numero - \
                1 - self.maksimoivia_palasia_perakkain:
            self.heurestinen_arvo += self.perakkaisten_ruutujen_arvot(
                self.maksimoivia_palasia_perakkain)
