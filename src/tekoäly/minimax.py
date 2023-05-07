from konfiguraatio import get_konfiguraatio
from tekoäly.heuristinen_arviointi import HeurestisenArvonLaskija

konffi = get_konfiguraatio()


class Tekoaly:
    """Luokka parhaan seuraavan ruudun etsimiseen käyttäen minimax algoritmia"""

    def __init__(
        self,
        tarkista_voitto,
        maksimoiva_merkki: str,
        minimoiva_merkki: str,
        maksimi_syvyys: int,
    ) -> None:
        self.tarkista_voitto = tarkista_voitto
        self.maksimoiva_merkki = maksimoiva_merkki
        self.minimoiva_merkki = minimoiva_merkki
        self.n = konffi.ruutujen_maara
        self.maksimi_syvyys = maksimi_syvyys

    def minimax(
        self,
        syvyys: int,
        pelilauta: list,
        siirrot: list,
        varatut_siirrot: set,
        vapaat_ruudut: set,
        siirroissa_olevat_ruudut: set,
        alfa: float,
        beeta: float,
        maksimoiva_pelaaja: bool,
        heuristinen_arvo: float,
        viimeisin_siirto: tuple | None = None,
    ) -> tuple:
        """Minimax algoritmi, jossa on relatiivinen heuristinen arviointi,
        joka perustuu aina ylemmän syvyyden heuristiseen arviointiin"""

        edellinen_merkki = (
            self.minimoiva_merkki if maksimoiva_pelaaja else self.maksimoiva_merkki
        )
        # tätä ei toteuteta ensimmäisellä kutsuntakerralla
        if viimeisin_siirto:
            if (
                self.tarkista_voitto(viimeisin_siirto, edellinen_merkki, pelilauta)
                or syvyys == 0
            ):
                return heuristinen_arvo, None

        if maksimoiva_pelaaja:
            arvo = float("-infinity")

            for siirto in siirrot[::-1]:
                if siirto in varatut_siirrot:
                    continue
                varatut_siirrot.add(siirto)

                # lisää tutkittavia siirtoja seuraavaa minimax kutsua varten
                uudet_siirrot, uudet_siirroissa_olevat_ruudut = self.etsi_siirrot(
                    siirto, vapaat_ruudut, siirroissa_olevat_ruudut, siirrot
                )

                pelilauta[siirto[1]][siirto[0]] = self.maksimoiva_merkki
                vapaat_ruudut.remove(siirto)
                uusi_heuristinen_arvo = heuristinen_arvo + self.heurstisen_arvon_delta(
                    pelilauta, syvyys, siirto
                )

                arviointi = self.minimax(
                    syvyys - 1,
                    pelilauta,
                    uudet_siirrot,
                    varatut_siirrot,
                    vapaat_ruudut,
                    uudet_siirroissa_olevat_ruudut,
                    alfa,
                    beeta,
                    False,
                    uusi_heuristinen_arvo,
                    siirto,
                )[0]
                if arviointi > arvo:
                    paras_siirto = siirto
                arvo = max(arvo, arviointi)
                pelilauta[siirto[1]][siirto[0]] = None
                varatut_siirrot.remove(siirto)
                vapaat_ruudut.add(siirto)
                alfa = max(alfa, arvo)
                if arvo >= beeta:
                    break
            return arvo, paras_siirto

        else:
            arvo = float("infinity")
            for siirto in siirrot[::-1]:
                if siirto in varatut_siirrot:
                    continue

                varatut_siirrot.add(siirto)
                uudet_siirrot, uudet_siirroissa_olevat_ruudut = self.etsi_siirrot(
                    siirto, vapaat_ruudut, siirroissa_olevat_ruudut, siirrot
                )
                pelilauta[siirto[1]][siirto[0]] = self.minimoiva_merkki
                vapaat_ruudut.remove(siirto)

                uusi_heuristinen_arvo = heuristinen_arvo + self.heurstisen_arvon_delta(
                    pelilauta, syvyys, siirto
                )

                arviointi = self.minimax(
                    syvyys - 1,
                    pelilauta,
                    uudet_siirrot,
                    varatut_siirrot,
                    vapaat_ruudut,
                    uudet_siirroissa_olevat_ruudut,
                    alfa,
                    beeta,
                    True,
                    uusi_heuristinen_arvo,
                    siirto,
                )[0]

                arvo = min(arvo, arviointi)
                pelilauta[siirto[1]][siirto[0]] = None
                varatut_siirrot.remove(siirto)
                vapaat_ruudut.add(siirto)

                beeta = min(beeta, arvo)
                if arvo <= alfa:
                    break

            return arvo, None

    @staticmethod
    def etsi_siirrot(
        edellinen_siirto: tuple,
        vapaat_ruudut: set,
        siirroissa_olevat_ruudut: set,
        siirrot: list,
    ):
        """Palauttaa tekoälylle ruudut, joista se etsii siirtoja

        Args:
            siirroissa_olevat_ruudut (set): samat ruudut kuin siirroissa,
                                            tietorakenne nopeuttaa etsimistä
        Returns:
            _type_: _description_
        """
        uudet_siirrot = siirrot.copy()
        uudet_siirroissa_olevat_ruudut = siirroissa_olevat_ruudut.copy()
        x, y = edellinen_siirto

        for x_delta in (2, -2, 1, -1, 0):
            for y_delta in (2, -2, 1, -1, 0):
                ruutu = x + x_delta, y + y_delta

                if ruutu in vapaat_ruudut:
                    if ruutu in uudet_siirroissa_olevat_ruudut:
                        uudet_siirrot.remove(ruutu)
                    else:
                        uudet_siirroissa_olevat_ruudut.add(ruutu)

                    uudet_siirrot.append(ruutu)
        return uudet_siirrot, uudet_siirroissa_olevat_ruudut

    def _tee_tarkistettava_suunta_dict(
        self, x_alku: int, y_alku: int, x_seuraava: int, y_seuraava: int, teksti
    ):
        """_summary_

        Args:
            x_alku (int): mistä x arvosta rivin tarkistus alkaa
            y_alku (int): mistä y arvosta rivin tarkistus alkaa
            x_seuraava (int): missä x koordinantin suunnassa seuraava rivin ruut on
            y_seuraava (int): missä y koordinantin suunnassa seuraava rivin ruutu on

        Returns:
            dict: palauttaa sanakirjan, jonka avulla voidaan laskea rivin heuristinen arvo
        """
        suunnan_laskija = HeurestisenArvonLaskija(
            self.maksimoiva_merkki, self.minimoiva_merkki
        )

        suunta_dict = {
            "arvon laskija": suunnan_laskija,
            "x alku": x_alku,
            "y alku": y_alku,
            "x seuraava": x_seuraava,
            "y seuraava": y_seuraava,
        }
        return suunta_dict

    def heurstisen_arvon_delta(
        self, pelilauta: list, syvyys: int, ruutu: tuple
    ) -> float:
        """arvioi kaikki vaaka, pysty, ja molemmat vinot rivit, joidenka pituus on 5 tai yli

        Args:
            pelilauta (list):
            syvyys (int): minimax algoritmin syvyys, kun se kutsuu tätä metodia
            ruutu (tuple): viimeiseksi lisätyn ruudun koordinaatit
        Returns:
            float: heuristinen arvo
        """
        x, y = ruutu
        uusin_merkki = pelilauta[y][x]
        pelilauta[y][x] = None
        tarkistettavat_suunnat = []
        # lisätään pysty suunta
        tarkistettavat_suunnat.append(
            self._tee_tarkistettava_suunta_dict(x, 0, 0, 1, "pysty")
        )
        # lisätään vaaka suunta
        tarkistettavat_suunnat.append(
            self._tee_tarkistettava_suunta_dict(0, y, 1, 0, "vaaka")
        )

        # lisätään vino rivi joka kallistuu oikealle
        x_alku1 = min(y + x, self.n)
        y_alku1 = max(y - (self.n - x), 0)
        if x_alku1 >= 4 and y_alku1 <= self.n - 5:
            tarkistettavat_suunnat.append(
                self._tee_tarkistettava_suunta_dict(
                    x_alku1, y_alku1, -1, 1, "vino oikea"
                )
            )

        # lisätään vino rivi, joka kallistuu vasemmalle
        x_alku2 = max(x - y, 0)
        y_alku2 = max(y - x, 0)
        if x_alku2 <= self.n - 5 and y_alku2 <= self.n - 5:
            tarkistettavat_suunnat.append(
                self._tee_tarkistettava_suunta_dict(
                    x_alku2, y_alku2, 1, 1, "vino vasen"
                )
            )

        heurestiset_arvot = []
        for _ in range(2):
            taulu = [[0 for _ in range(self.n)] for _ in range(self.n)]
            arvo = 0
            for rivin_suunta in tarkistettavat_suunnat:
                rivin_suunta["arvon laskija"].laskemisen_alustus()

                for i in range(self.n):
                    x_akseli = rivin_suunta["x alku"] + rivin_suunta["x seuraava"] * i
                    y_akseli = rivin_suunta["y alku"] + rivin_suunta["y seuraava"] * i
                    if 0 <= x_akseli < self.n and 0 <= y_akseli < self.n:
                        taulu[y_akseli][x_akseli] += 1
                        merkki = pelilauta[y_akseli][x_akseli]
                        rivin_suunta["arvon laskija"].laske_arvo(
                            merkki,
                            (
                                x_akseli - rivin_suunta["x seuraava"],
                                y_akseli - rivin_suunta["y seuraava"],
                            ),
                        )
                rivin_suunta["arvon laskija"].viimeisen_ruudun_tarkistus()
                arvo += rivin_suunta["arvon laskija"].heuristinen_arvo
                rivin_suunta["arvon laskija"].heuristinen_arvo = 0
            HeurestisenArvonLaskija.yksi_perakkain.clear()
            pelilauta[y][x] = uusin_merkki
            heurestiset_arvot.append(arvo)
        heuristinen_arvo = heurestiset_arvot[1] - heurestiset_arvot[0]
        kerroin = (10 - (self.maksimi_syvyys - syvyys)) / 10
        return heuristinen_arvo * kerroin

    def heuristinen_funktio(self, pelilauta: list) -> float:
        """arvioi kaikki vaaka, pysty, ja molemmat vinot rivit, joidenka pituus on 5 tai yli
        Args:
            pelilauta (list):
            syvyys (int): minimax algoritmin syvyys, kun se kutsuu tätä metodia
        Returns:
            float: heuristinen arvo
        """
        pysty = HeurestisenArvonLaskija(self.maksimoiva_merkki, self.minimoiva_merkki)
        vaaka = HeurestisenArvonLaskija(self.maksimoiva_merkki, self.minimoiva_merkki)
        vino_oikea = HeurestisenArvonLaskija(
            self.maksimoiva_merkki, self.minimoiva_merkki
        )
        vino_vasen = HeurestisenArvonLaskija(
            self.maksimoiva_merkki, self.minimoiva_merkki
        )

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
                vino_vasen_merkki = pelilauta[y_akseli2][x_akseli2]

                vino_oikea.laske_arvo(
                    vino_oikea_merkki, edeltava_ruutu=(x_akseli1 + 1, y_akseli1 - 1)
                )
                vino_vasen.laske_arvo(
                    vino_vasen_merkki, edeltava_ruutu=(x_akseli2 - 1, y_akseli2 - 1)
                )
            vino_oikea.viimeisen_ruudun_tarkistus()
            vino_vasen.viimeisen_ruudun_tarkistus()
        HeurestisenArvonLaskija.yksi_perakkain.clear()
        return (
            pysty.heuristinen_arvo
            + vaaka.heuristinen_arvo
            + vino_oikea.heuristinen_arvo
            + vino_vasen.heuristinen_arvo
        )
