from peli.peli_logiikka import Peli


def peli_silmukka(peli: Peli) -> str:
    """Pelin silmukka"""
    peli.lauta_ui.piirra_lauta()
    loppu = False
    vuoro = 0
    while True:
        while True:
            tapahtuma = peli.tapahtumat.palauta_nappaimiston_komento()
            if tapahtuma:
                return tapahtuma

            siirto = peli.pelaa_vuoro(vuoro)
            if siirto:
                loppu, loppu_arvo = peli.tarkista_onko_peli_paattynyt(
                    siirto, peli.pelaajat[vuoro].merkki, peli.lauta
                )

                break
        if loppu:
            break
        vuoro = peli.vaihda_vuoroa(vuoro)
        peli.lauta_ui.piirra_lauta()
    peli.lauta_ui.tee_voittoteksti(loppu_arvo)
    while True:
        peli.lauta_ui.piirra_lauta()
        tapahtumat = peli.tapahtumat.get_tapahtumat()
        if tapahtumat["lopeta"]:
            return "lopeta"
        elif tapahtumat["takaisin"]:
            return "takaisin"
        elif tapahtumat["pelaa_uudelleen"]:
            return "pelaa_uudelleen"
