with open(".env", "w") as tiedosto:
    tiedosto.write("KONFIGURAATIO=tuotanto_konfiguraatio.json")

from konfiguraatio import rakenna_konfiguraatio

rakenna_konfiguraatio()


print("Alustus tehty")
