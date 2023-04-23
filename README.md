# TiRa-Labra

Ristinolla tekoälyllä varustettuna olisi tavoite.

![Github Actions](https://github.com/aitoAarni/TiRa-Labra/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/aitoAarni/TiRa-Labra/branch/main/graph/badge.svg?token=G521CJR0IT)](https://codecov.io/gh/aitoAarni/TiRa-Labra)




## Dokumentit

[Määrittelydokumentti](https://github.com/aitoAarni/TiRa-Labra/blob/main/dokumentaatio/m%C3%A4%C3%A4rittelydokumentti.md)

[Testausdokumentti](https://github.com/aitoAarni/TiRa-Labra/blob/main/dokumentaatio/Testausdokumentti.md)

[Toteutusdokumentti](https://github.com/aitoAarni/TiRa-Labra/blob/main/dokumentaatio/toteutusdokumentti.md)

### viikkoraportit

[viikkoraportti 1](https://github.com/aitoAarni/TiRa-Labra/blob/main/dokumentaatio/viikkoraportti1.md)

[viikkoraportti 2](https://github.com/aitoAarni/TiRa-Labra/blob/main/dokumentaatio/viikkoraportti2.md)

[viikkoraportti 3](https://github.com/aitoAarni/TiRa-Labra/blob/main/dokumentaatio/viikkoraportti3.md)

[viikkoraportti 4](https://github.com/aitoAarni/TiRa-Labra/blob/main/dokumentaatio/viikkoraportti4.md)

## pikaiset ohjeet vertaisarviointia varten


Lataa projekti git clone - kommennolla ja asenna projekti seuraavilla komennoilla:

```
poetry install
```

aloita ohjelma komennolla

```
poetry run invoke start 
```
Tällä hetkellä pelissä heurestinen arviointi on vielä vähän heikko, joten paras minimax syvyys jolla peli toimii on 2. Pelissä ei ole vielä valikkoa, joten joitakin parametrejä voi vaihdella [materiaalit/tuotanto_konfiguraatio.json](https://github.com/aitoAarni/TiRa-Labra/blob/main/materiaalit/tuotanto_konfiguraatio.json) tiedostosta.
