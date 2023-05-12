class HeurestisenArvonLaskija:
    """Luokkan metodit arvioi pelilaudan tilannetta"""

    VOITTO_ARVO = 10**11

    def __init__(
        self, maksimoiva_merkki: str, minimoiva_merkki: str, maksimi_syvyys: int
    ) -> None:
        self.maksimoiva_merkki = maksimoiva_merkki
        self.minimoiva_merkki = minimoiva_merkki
        self.maksimi_syvyys = maksimi_syvyys

    def perakkaisten_ruutujen_arvot(
        self, n_perakkain: int, syvyys: int, molemmilla_puolilla_tyhja: bool = False
    ) -> float:
        """Palauttaa numeerisen arvion peräkkäisten ruutujen arvosta

        Args:
            n_perakkain (int): montako ruutua on peräkkäin
            molemmilla_puolilla_tyhja (bool, optional):
            onko n_perakkain jonon molemmilla puolilla tyhjä ruutu. Defaults to False.

        Returns:
            float: arvio
        """
        arvot = {2: 10, 3: 100, 4: 1500}
        if molemmilla_puolilla_tyhja:
            arvot = {2: 100, 3: 1500, 4: 100_000}

        if n_perakkain in arvot:
            arvo = arvot[n_perakkain]
        elif n_perakkain < 2:
            arvo = 0
        else:
            arvo = HeurestisenArvonLaskija.VOITTO_ARVO - 10 ** (
                self.maksimi_syvyys - syvyys
            )

        return arvo

    def etsi_paras_arvo_katkenneesta_perakkaisista_ruuduista(
        self, paikat: dict, rivi: list, toinen_merkki: str, syvyys: int
    ):
        """Etsii parhaan arvojakauman kaikista saman merkin jonoista (sillä niitä voi muodostaa monella tapaa)
        joissa on yksi tyhjä ruutu välissä
        esim. xx-xx-x-x, missä x on merkki ja - on tyhjä ruutu

        Args:
            paikat (dict): avain: josta jono alkaa, arvo: josta jono alkaa uudestaan tyhjän ruudun jälkeen
            rivi (list): yksi rivi ruudukosta
            toinen_merkki (str): merkki jonka jonot eivät ole tarkastelussa
            syvyys (int): syvys miltä tätä metodia kutsutaan

        Returns:
            float: paras heursitinen arvo, jonka rikkinäisistä jonoista voi muodostaa
        """
        paikat_lista = list(paikat.items())
        return self._iteraattori(paikat_lista, rivi, 0, None, toinen_merkki, syvyys)

    def _iteraattori(
        self,
        paikat: list,
        rivi: list,
        indeksi: int,
        varattu: int | None,
        toinen_merkki: str,
        syvyys: int,
    ):
        """iteroi kaikki kombinaatiot läpi, miten saman merkkiset jonot,
          joissa on yksi tyhjä ruutu välissä voi arvioida.
          jos esim jono on 'xx xx', niin se arvioidaan neljän pitkänä

        Args:
            paikat (list):
            rivi (list):
            indeksi (int):
            varattu (int | None):
            toinen_merkki (str):
            syvyys (int):

        Returns:
            float: Palauttaa parhaan mahdollisen kombinaation
        """
        etu_blokki = True
        if indeksi == len(paikat):
            return 0
        alku = paikat[indeksi][0]
        if alku > 0 and rivi[alku - 1] == None:
            etu_blokki = False
        if alku == varattu:
            return self._iteraattori(
                paikat, rivi, indeksi + 1, None, toinen_merkki, syvyys
            )

        loppu = paikat[indeksi][1]
        taka_blokki = True
        loppu_pituus = len(rivi) - 1 - loppu
        for i, merkki in enumerate(rivi[loppu:]):
            if merkki in (None, toinen_merkki):
                loppu_pituus = i - 1
                break

        if (
            loppu + loppu_pituus < len(rivi) - 1
            and rivi[loppu + loppu_pituus + 1] == None
        ):
            taka_blokki = False
        maksimi_arvo = 0
        if not (etu_blokki and taka_blokki and loppu + loppu_pituus - alku < 4):
            arvo = self.perakkaisten_ruutujen_arvot(
                loppu + loppu_pituus - alku, syvyys, not (etu_blokki or taka_blokki)
            )
            arvo = round(arvo * 0.85, 2)
            varattu = loppu
            arvo += self._iteraattori(
                paikat, rivi, indeksi + 1, varattu, toinen_merkki, syvyys
            )
            maksimi_arvo = arvo

        arvo = self.perakkaisten_ruutujen_arvot(
            loppu - alku - 1, syvyys, molemmilla_puolilla_tyhja=not etu_blokki
        )
        arvo += self._iteraattori(
            paikat, rivi, indeksi + 1, None, toinen_merkki, syvyys
        )
        maksimi_arvo = max(maksimi_arvo, arvo)

        return maksimi_arvo

    def laske_heuristinen_arvo(self, rivi_ruutuja, syvyys):
        """Metodi saa aina rivin, jonka se arvioi heuristiikan avulla numeerisesti

        Args:
            rivi_ruutuja (list): ruudut voi olla ristejä, nollia sekä tyhjiä
            syvyys (int): syvyys jolta tätä metodia kutsuttin

        Returns:
            float: heuristinen arvo
        """
        rivin_pituus = len(rivi_ruutuja)
        heuristinen_arvo = 0
        maksimoivia_palasia_perakkain = 0
        minimoivia_palasia_perakkain = 0
        viimeinen_tyhja_ruutu = None
        edeltava_merkki = -1
        skipattava_merkki = False
        yksi_tyhja_ruutu_maksimoivien_merkkien_valissa = {}
        yksi_tyhja_ruutu_minimoivien_merkkien_valissa = {}
        tyhja_ruutu_merkkien_valissa = set()
        seuraava_merkki = -1

        for ruudun_num, merkki in enumerate(rivi_ruutuja):
            if merkki == skipattava_merkki:
                edeltava_merkki = merkki
                if merkki == self.maksimoiva_merkki:
                    maksimoivia_palasia_perakkain += 1
                else:
                    minimoivia_palasia_perakkain += 1
                continue
            skipattava_merkki = False
            if rivin_pituus - 1 > ruudun_num:
                seuraava_merkki = rivi_ruutuja[ruudun_num + 1]
            else:
                seuraava_merkki = False
            if merkki == self.maksimoiva_merkki:
                maksimoivia_palasia_perakkain += 1

                # if katsoo onko molemmilla puolilla minimoivia palasia maksimoiva merkki,
                # jos on, niin heuristinen_arvo == 0 ja skippaa loppuun
                if (
                    viimeinen_tyhja_ruutu
                    == ruudun_num - 1 - minimoivia_palasia_perakkain
                    and minimoivia_palasia_perakkain > 1
                ) or minimoivia_palasia_perakkain >= 5:
                    # jos minimoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen maksivoiva merkki
                    # niin vähennä heurestista arvoa
                    if (
                        ruudun_num - minimoivia_palasia_perakkain
                        not in tyhja_ruutu_merkkien_valissa
                    ):
                        heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                            minimoivia_palasia_perakkain, syvyys
                        )
                minimoivia_palasia_perakkain = 0

            elif merkki == self.minimoiva_merkki:
                minimoivia_palasia_perakkain += 1
                # if katsoo onko molemmilla puolilla minimoivia palasia maksimoiva merkki,
                # jos on, niin heuristinen_arvo == 0 ja skippaa loppuun
                if (
                    viimeinen_tyhja_ruutu
                    == ruudun_num - 1 - maksimoivia_palasia_perakkain
                    and maksimoivia_palasia_perakkain > 1
                ) or maksimoivia_palasia_perakkain >= 5:
                    # jos maksimoivia palasia on useita peräkkäin ja niitä blokkaa nykyinen minivoiva merkki
                    # niin lisää heurestista arvoa
                    if (
                        ruudun_num - maksimoivia_palasia_perakkain
                        not in tyhja_ruutu_merkkien_valissa
                    ):
                        heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                            maksimoivia_palasia_perakkain, syvyys
                        )
                maksimoivia_palasia_perakkain = 0

            # jos jonon (ristejä tai nollia) molemmilla puolilla on tyhjä ruutu
            else:
                # jos minimoivia merkkejä on välissä ja molemmilla puolilla on tyhjä ruutu
                # niin vähennä heurestista arvoa
                if (
                    seuraava_merkki == edeltava_merkki
                    and not None
                    in (
                        seuraava_merkki,
                        edeltava_merkki,
                    )
                    and minimoivia_palasia_perakkain < 5
                    and maksimoivia_palasia_perakkain < 5
                ):
                    if edeltava_merkki == self.minimoiva_merkki:
                        yksi_tyhja_ruutu_minimoivien_merkkien_valissa[
                            ruudun_num - minimoivia_palasia_perakkain
                        ] = (ruudun_num + 1)
                        tyhja_ruutu_merkkien_valissa.add(ruudun_num + 1)
                        skipattava_merkki = self.minimoiva_merkki
                    else:
                        yksi_tyhja_ruutu_maksimoivien_merkkien_valissa[
                            ruudun_num - maksimoivia_palasia_perakkain
                        ] = (ruudun_num + 1)
                        tyhja_ruutu_merkkien_valissa.add(ruudun_num + 1)
                        skipattava_merkki = self.maksimoiva_merkki
                elif (
                    viimeinen_tyhja_ruutu
                    == ruudun_num - 1 - minimoivia_palasia_perakkain
                ):
                    if (
                        ruudun_num - minimoivia_palasia_perakkain
                        not in tyhja_ruutu_merkkien_valissa
                    ):
                        heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                            minimoivia_palasia_perakkain,
                            syvyys,
                            molemmilla_puolilla_tyhja=True,
                        )

                # jos maskivoivia merkkejä on välissä ja molemmilla puolilla on tyhjä ruutu
                # niin lisää heurestista arvoa
                elif (
                    viimeinen_tyhja_ruutu
                    == ruudun_num - 1 - maksimoivia_palasia_perakkain
                ):
                    if (
                        ruudun_num - maksimoivia_palasia_perakkain
                        not in tyhja_ruutu_merkkien_valissa
                    ):
                        heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                            maksimoivia_palasia_perakkain,
                            syvyys,
                            molemmilla_puolilla_tyhja=True,
                        )

                # jos samoja merkkejä peräkkäin jono on alkanut laudan reunalta
                elif 1 not in (
                    maksimoivia_palasia_perakkain,
                    minimoivia_palasia_perakkain,
                ):
                    heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                        minimoivia_palasia_perakkain, syvyys
                    )
                    heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                        maksimoivia_palasia_perakkain, syvyys
                    )

                viimeinen_tyhja_ruutu = ruudun_num
                minimoivia_palasia_perakkain = maksimoivia_palasia_perakkain = 0

            edeltava_merkki = merkki
        if (
            viimeinen_tyhja_ruutu == ruudun_num - minimoivia_palasia_perakkain
            and ruudun_num - minimoivia_palasia_perakkain + 1
            not in tyhja_ruutu_merkkien_valissa
        ):
            heuristinen_arvo -= self.perakkaisten_ruutujen_arvot(
                minimoivia_palasia_perakkain, syvyys
            )
        if (
            viimeinen_tyhja_ruutu == ruudun_num - maksimoivia_palasia_perakkain
            and ruudun_num - maksimoivia_palasia_perakkain + 1
            not in tyhja_ruutu_merkkien_valissa
        ):
            heuristinen_arvo += self.perakkaisten_ruutujen_arvot(
                maksimoivia_palasia_perakkain, syvyys
            )
        heuristinen_arvo -= self.etsi_paras_arvo_katkenneesta_perakkaisista_ruuduista(
            yksi_tyhja_ruutu_minimoivien_merkkien_valissa,
            rivi_ruutuja,
            self.maksimoiva_merkki,
            syvyys,
        )
        heuristinen_arvo += self.etsi_paras_arvo_katkenneesta_perakkaisista_ruuduista(
            yksi_tyhja_ruutu_maksimoivien_merkkien_valissa,
            rivi_ruutuja,
            self.minimoiva_merkki,
            syvyys,
        )
        return heuristinen_arvo
