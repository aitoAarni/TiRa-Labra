from konfiguraatio import get_konfiguraatio
from tekoäly.heurestinen_arviointi import HeurestisenArvonLaskija
konffi = get_konfiguraatio()

RUUTUJEN_MAARA = konffi["ruutujen_määrä"]


class Tekoaly:
    """Luokka parhaan seuraavan ruudun etsimiseen käyttäen minimax algoritmia
    """

    def __init__(
            self,
            tarkista_voitto,
            maksimoiva_merkki: str,
            minimoiva_merkki: str, maksimi_syvyys: int) -> None:
        self.tarkista_voitto = tarkista_voitto
        self.maksimoiva_merkki = maksimoiva_merkki
        self.minimoiva_merkki = minimoiva_merkki
        self.n = RUUTUJEN_MAARA
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
            viimeisin_siirto: tuple | None=None) -> tuple:

        edellinen_merkki = self.minimoiva_merkki if maksimoiva_pelaaja else self.maksimoiva_merkki

        if viimeisin_siirto:
            if self.tarkista_voitto(
                    viimeisin_siirto,
                    edellinen_merkki,
                    pelilauta) or syvyys == 0:
                return self.heurestinen_funktio(pelilauta, syvyys), None

        if maksimoiva_pelaaja:
            arvo = float("-infinity")

            for siirto in siirrot[::-1]:
                if siirto in varatut_siirrot:
                    continue
                varatut_siirrot.add(siirto)

                # lisää tutkittavia siirtoja seuraavaa minimax kutsua varten
                uudet_siirrot, uudet_siirroissa_olevat_ruudut = self.etsi_siirrot(
                    siirto, vapaat_ruudut, siirroissa_olevat_ruudut, siirrot)
                
                pelilauta[siirto[1]][siirto[0]] = self.maksimoiva_merkki
                vapaat_ruudut.remove(siirto)

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
                    siirto)[0]

                arvo = max(arvo, arviointi)
                if arviointi == arvo:
                    paras_siirto = siirto
                pelilauta[siirto[1]][siirto[0]] = None

                varatut_siirrot.remove(siirto)
                vapaat_ruudut.add(siirto)
                alfa = max(alfa, arvo)
                if arvo > beeta:
                    break
            return arvo, paras_siirto

        else:
            arvo = float("infinity")
            for siirto in siirrot[::-1]:
                if siirto in varatut_siirrot:
                    continue
                varatut_siirrot.add(siirto)
                uudet_siirrot, uudet_siirroissa_olevat_ruudut = self.etsi_siirrot(
                    siirto, vapaat_ruudut, siirroissa_olevat_ruudut, siirrot)
                pelilauta[siirto[1]][siirto[0]] = self.minimoiva_merkki
                vapaat_ruudut.remove(siirto)

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
                    siirto)[0]

                arvo = min(arvo, arviointi)
                pelilauta[siirto[1]][siirto[0]] = None
                varatut_siirrot.remove(siirto)
                vapaat_ruudut.add(siirto)

                beeta = min(beeta, arvo)
                if arvo < alfa:
                    break

            return arvo, None

    @staticmethod
    def etsi_siirrot(
            edellinen_siirto: tuple,
            vapaat_ruudut: set,
            siirroissa_olevat_ruudut: set,
            siirrot: list):
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


    def heurestinen_funktio(self, pelilauta: list, syvyys: int) -> float:
        """arvioi kaikki vaaka, pysty, ja molemmat vinot rivit, joidenka pituus on 5 tai yli

        Args:
            pelilauta (list): 
            syvyys (int): minimax algoritmin syvyys, kun se kutsuu tätä metodia

        Returns:
            float: heurestinen arvo
        """
        pysty = HeurestisenArvonLaskija(
            self.maksimoiva_merkki,
            self.minimoiva_merkki,
            syvyys,
            self.maksimi_syvyys)
        vaaka = HeurestisenArvonLaskija(
            self.maksimoiva_merkki,
            self.minimoiva_merkki,
            syvyys,
            self.maksimi_syvyys)
        vino_oikea = HeurestisenArvonLaskija(
            self.maksimoiva_merkki,
            self.minimoiva_merkki,
            syvyys,
            self.maksimi_syvyys)
        vino_vasen = HeurestisenArvonLaskija(
            self.maksimoiva_merkki,
            self.minimoiva_merkki,
            syvyys,
            self.maksimi_syvyys)

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
                    vino_oikea_merkki, edeltava_ruutu=(x_akseli1 + 1, y_akseli1 - 1))
                vino_vasen.laske_arvo(
                    vino_vasen_merkki, edeltava_ruutu=(x_akseli2 - 1, y_akseli2 - 1))
            vino_oikea.viimeisen_ruudun_tarkistus()
            vino_vasen.viimeisen_ruudun_tarkistus()
        HeurestisenArvonLaskija.yksi_perakkain.clear()
        return pysty.heurestinen_arvo + vaaka.heurestinen_arvo + \
            vino_oikea.heurestinen_arvo + vino_vasen.heurestinen_arvo
