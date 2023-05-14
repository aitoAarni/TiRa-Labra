# Käyttöohje

## Sovelluksen asentaminen ja komennot

Projektin asentamine omalle koneelle on mahdollista komennolla (jos git on asennettu):
```
git clone git@github.com:aitoAarni/TiRa-Labra.git
```

Sovelluksen riippuvuudet voidaan asentaa komennolla: 
```
poetry install
```

Ennen sovelluksen suoritusta .env sekä mahdollisesti konfiguraatio pitää alustaa komennolla:
```
poetry run invoke build
```

projektin komennot ovat juurihakemiston `tasks.py` tiedostossa
komennoista tärkeimmät ovat:
aloittamista varten
```
poetry run invoke start
```
windowsilla suosittelen aloittamaan ohjelman komennolla:
```
poetry run python src\index.py
```
sillä silloin näkyy komentorivin statistiikat

testejä varten:
```
peotry run invoke test
```

## Pelin ohjeet

Pelin voittamiseen vaaditaan viisi ristiä tai nollaa peräkkäin.
Valikosta voi vaihtaa muutamia pelin asetuksia.
Pelissä on useita asetuksia joita voi vaihtaa [konfiguraatio tiedostosta](https://github.com/aitoAarni/TiRa-Labra/blob/main/konfiguraatio/tuotanto_konfiguraatio.json) mm. tekoälyn maksimi syvyys, vuoron maksimi kesto tekoälylle ja resoluutio.

komentorivi näyttää pelin tekoälyn progression vuoron aikana.

Pelin pikanäppäimet: `r` on uudestaan pelaamista varten ja `esc` on poistumista varten
