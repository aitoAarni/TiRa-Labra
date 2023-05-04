import json
from dotenv import load_dotenv
import os

tiedoston_nimi = os.path.dirname(__file__)
konfiguraatio = None

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



def rakenna_konfiguraatio():
    konfiguraatio = {
        "ruutujen_määrä": 15,
        "laudan_väri": (0, 0, 0),
        "laudan_viivojen_väri": (255, 255, 255),
        "korkeus": 500,
        "leveys": 500,
        "nappuloiden_väri": (0, 0, 255),
        "peli_ohi_väri": (192, 192, 192),
        "voitto_tekstin_väri": (0, 0, 0),
        "fontti": 30,
        "nappien_väri": (0, 0, 220)
    }
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        json.dump(konfiguraatio, tiedosto)



def set_konfiguraatio(konfiguraatio_tietokirja):
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        tiedosto.write(json.dumps(konfiguraatio_tietokirja))

def paivita_konfiguraatio():
    global konfiguraatio
    with open(konfiguraatiotiedoston_polku, "r") as tiedosto:
        uusi_konfiguraatio = json.load(tiedosto)
    konfiguraatio = uusi_konfiguraatio

paivita_konfiguraatio()


def get_konfiguraatio():
    return konfiguraatio


class Testi:
    def __init__(self) -> None:
        self.testi_attribuutti = 1

t = Testi()

def get_testi():
    print("konfiguraatiossa id(t):", id(t))
    return t

def paivita_testi():
    t.testi_attribuutti += 1


def main():
    rakenna_konfiguraatio()
