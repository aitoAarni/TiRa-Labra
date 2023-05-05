import json
from dotenv import load_dotenv
import os

tiedoston_nimi = os.path.dirname(__file__)

try:
    load_dotenv()
except FileNotFoundError:
    pass


try:
    konfiguraatiotiedoston_nimi = os.getenv("KONFIGURAATIO")
    konfiguraatiotiedoston_polku = os.path.join(
        "materiaalit",
        konfiguraatiotiedoston_nimi)

except TypeError:
    konfiguraatiotiedoston_polku = os.path.join(
        tiedoston_nimi,
        "..",
        "materiaalit",
        "testaus_konfiguraatio.json")


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
        "ruutujen_maara": 25,
        "laudan_vari": (0, 0, 0),
        "laudan_viivojen_vari": (255, 255, 255), 
        "korkeus": 1000, 
        "leveys": 1200, 
        "nappuloiden_vari": (0, 0, 255), 
        "peli_ohi_vari": (192, 192, 192),
        "voitto_tekstin_vari": (105, 105, 105),
        "fontti": 60, 
        "nappien_vari": (0, 0, 220)}
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        json.dump(konfiguraatio, tiedosto)


def set_konfiguraatio(konfiguraatio_objekti: KonfiguraatioArvot):
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        tiedosto.write(json.dumps(konfiguraatio_objekti.palauta_sanakirja_atribuuteista()))


def paivita_konfiguraatio():
    with open(konfiguraatiotiedoston_polku, "r") as tiedosto:
        uusi_konfiguraatio = json.load(tiedosto)
    konfiguraatio.paivita_atribuutit(uusi_konfiguraatio)


paivita_konfiguraatio()


def get_konfiguraatio():
    return konfiguraatio
