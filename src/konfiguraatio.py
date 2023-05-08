import json
from dotenv import load_dotenv
import os

tiedoston_nimi = os.path.dirname(__file__)

try:
    load_dotenv()
except FileNotFoundError:
    pass


konfiguraatiotiedoston_nimi = os.getenv("KONFIGURAATIO")
if konfiguraatiotiedoston_nimi == None:
    konfiguraatiotiedoston_nimi = "tuotanto_konfiguraatio.json"
konfiguraatiotiedoston_polku = os.path.join(
    "konfiguraatio", konfiguraatiotiedoston_nimi
)


class KonfiguraatioArvot:
    def __init__(self) -> None:
        pass

    def paivita_atribuutit(self, sanakrija):
        self.__dict__ = sanakrija

    def palauta_sanakirja_atribuuteista(self):
        return vars(self)


konfiguraatio = KonfiguraatioArvot()


def rakenna_konfiguraatio():
    konfiguraatio = {
        "tekoalyn_syvyys": 3,
        "ruutujen_maara": 25,
        "laudan_vari": (0, 0, 0),
        "laudan_viivojen_vari": (255, 255, 255),
        "korkeus": 1000,
        "leveys": 1000,
        "nappuloiden_vari": (0, 0, 255),
        "peli_ohi_vari": (192, 192, 192),
        "voitto_tekstin_vari": (105, 105, 105),
        "fontti": 60,
        "nappien_vari": (0, 0, 220),
    }
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        tiedosto.write(json.dumps(konfiguraatio))
    testaus_konfiguraatio_polku = os.path.join(
        tiedoston_nimi, "..", "konfiguraatio", "testaus_konfiguraatio.json"
    )
    with open(testaus_konfiguraatio_polku, "w") as tiedosto:
        tiedosto.write(json.dumps(konfiguraatio))


def set_konfiguraatio(konfiguraatio_objekti: KonfiguraatioArvot):
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        tiedosto.write(
            json.dumps(konfiguraatio_objekti.palauta_sanakirja_atribuuteista())
        )


def paivita_konfiguraatio():
    with open(konfiguraatiotiedoston_polku, "r") as tiedosto:
        try:
            uusi_konfiguraatio = json.load(tiedosto)
        except json.decoder.JSONDecodeError:
            return
    konfiguraatio.paivita_atribuutit(uusi_konfiguraatio)


paivita_konfiguraatio()


def get_konfiguraatio():
    return konfiguraatio
