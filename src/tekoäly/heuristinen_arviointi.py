VOITTO_ARVO = 10**10


class HeurestisenArvonLaskija:
    """ Luokkan metodit arvioi pelilaudan tilannetta
    """
    yksi_perakkain = set()

    def __init__(
            self,
            maksimoiva_merkki: str,
            minimoiva_merkki: str
    ) -> None:
        self.maksimoiva_merkki = maksimoiva_merkki
        self.minimoiva_merkki = minimoiva_merkki
        self.heuristinen_arvo = 0
        self.viimeinen_tyhja_ruutu = None
        self.maksimoivia_palasia_perakkain = None
        self.minimoivia_palasia_perakkain = None
        self._ruutu_numero = 0

    def perakkaisten_ruutujen_arvot(
            self,
            n_perakkain: int,
            molemmilla_puolilla_tyhja: bool = False) -> float:
        """Palauttaa numeerisen arvion peräkkäisten ruutujen arvosta

        Args:
            n_perakkain (int): montako ruutua on peräkkäin
            molemmilla_puolilla_tyhja (bool, optional):
            onko n_perakkain jonon molemmilla puolilla tyhjä ruutu. Defaults to False.

        Returns:
            float: arvio
        """
        arvot = {2: 10, 3: 150, 4: 2500, 5: VOITTO_ARVO}
        if molemmilla_puolilla_tyhja:
            arvot = {2: 95, 3: 1500, 4: 100000, 5: VOITTO_ARVO}

        if n_perakkain in arvot:
            arvo = arvot[n_perakkain]
        elif n_perakkain < 2:
            arvo = 0
        else:
            arvo = VOITTO_ARVO

        return arvo

    def laske_arvo(self, merkki: str, edeltava_ruutu: tuple):
        """Metodi saa aina yhden ruudun merkin kerrallaan peräkkäisistä ruuduista,
        jonka avulla metodi arvioi ruudun arvoa isommassa kokonaisuudessa

        Args:
            merkki (str): risti tai nolla
            edeltava_ruutu (tuple): edeltävän ruudun koordinaatit,
            jotta yhden pituisia jonoja ei lasketa useaan kertaan mukaan heurestiseen arvioon
        """
        if merkki == self.maksimoiva_merkki:
            self.maksimoivia_palasia_perakkain += 1

            # if katsoo onko molemmilla puolilla minimoivia palasia maksimoiva merkki,
            # jos on, niin heuristinen_arvo == 0 ja skippaa loppuun
            if (self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 -
                    self.minimoivia_palasia_perakkain and self.minimoivia_palasia_perakkain > 1) or self.minimoivia_palasia_perakkain >= 5:
                # jos minimoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen maksivoiva merkki
                # niin vähennä heurestista arvoa
                self.heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                    self.minimoivia_palasia_perakkain)
            self.minimoivia_palasia_perakkain = 0

        elif merkki == self.minimoiva_merkki:
            self.minimoivia_palasia_perakkain += 1
            # if katsoo onko molemmilla puolilla minimoivia palasia maksimoiva merkki,
            # jos on, niin heuristinen_arvo == 0 ja skippaa loppuun
            if (self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 -
                    self.maksimoivia_palasia_perakkain and self.maksimoivia_palasia_perakkain > 1) or self.maksimoivia_palasia_perakkain >= 5:
                # jos maksivoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen minivoiva merkki
                # niin lisää heurestista arvoa
                self.heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                    self.maksimoivia_palasia_perakkain)
            self.maksimoivia_palasia_perakkain = 0

        # jos jonon (ristejä tai nollia) molemmilla puolilla on tyhjä ruutu
        else:
            # jos minivoivia merkkejä on välissä ja molemmilla puolilla on tyhjä ruutu
            # niin vähennä heurestista arvoa
            if self.viimeinen_tyhja_ruutu == self._ruutu_numero - \
                    1 - self.minimoivia_palasia_perakkain:

                if self.minimoivia_palasia_perakkain == 1:
                    if edeltava_ruutu in self.yksi_perakkain:
                        pass
                    else:
                        self.yksi_perakkain.add(edeltava_ruutu)
                        self.heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                            self.minimoivia_palasia_perakkain, molemmilla_puolilla_tyhja=True)
                else:
                    self.heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                        self.minimoivia_palasia_perakkain, molemmilla_puolilla_tyhja=True)

            # jos maskivoivia merkkejä on välissä ja molemmilla puolilla on tyhjä ruutu
            # niin lisää heurestista arvoa
            elif self.viimeinen_tyhja_ruutu == self._ruutu_numero - 1 - self.maksimoivia_palasia_perakkain:

                if self.maksimoivia_palasia_perakkain == 1:
                    if edeltava_ruutu in self.yksi_perakkain:
                        pass

                    else:
                        self.yksi_perakkain.add(edeltava_ruutu)
                        self.heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                            self.maksimoivia_palasia_perakkain, molemmilla_puolilla_tyhja=True)
                else:
                    self.heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                        self.maksimoivia_palasia_perakkain, molemmilla_puolilla_tyhja=True)

            # jos samoja merkkejä peräkkäin jono on alkanut laudan reunalta
            elif 1 not in (self.maksimoivia_palasia_perakkain, self.minimoivia_palasia_perakkain):
                self.heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                    self.minimoivia_palasia_perakkain)
                self.heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                    self.maksimoivia_palasia_perakkain)

            self.viimeinen_tyhja_ruutu = self._ruutu_numero
            self.minimoivia_palasia_perakkain = self.maksimoivia_palasia_perakkain = 0
        self._ruutu_numero += 1

    def laskemisen_alustus(self):
        """kutsutaan kun aloitetaan uuden rivin tutkiminen
        """
        self.viimeinen_tyhja_ruutu = float("-infinity")
        self.maksimoivia_palasia_perakkain = 0
        self.minimoivia_palasia_perakkain = 0
        self._ruutu_numero = 0

    def viimeisen_ruudun_tarkistus(self):
        """viimeinen ruutu rivistä pitää aina tutkia erikseen
        """
        if self.viimeinen_tyhja_ruutu == self._ruutu_numero - \
                1 - self.minimoivia_palasia_perakkain:
            self.heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                self.minimoivia_palasia_perakkain)
        if self.viimeinen_tyhja_ruutu == self._ruutu_numero - \
                1 - self.maksimoivia_palasia_perakkain:
            self.heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                self.maksimoivia_palasia_perakkain)
