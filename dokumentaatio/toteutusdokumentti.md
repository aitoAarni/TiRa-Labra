# Toteutusdokumentti

## Yleisrakenne

Pelissä on valikko, josta voi risteille ja nollille joko ihmis- tai tekoälypelaajan, sekä pelilaudan ruutujen määrän. Pelin tekoäly käyttää minimax algoritmia (pienellä muunnelmalla), joka on raa'an voiman algoritmi. Minimax on tehostettu alfa-beeta karsinnalla. Tekoäly pelaajalla on aikaraja, ja se kutsuu minimax algoritmia syvyyksillä 2, 3, ..., maksimi_syvyys (iteratiivinen syveneminen). Jokaisen syvyyden jälkeen ruudut joista minimax etsii maksimoijan ensimmäistä siirtoa järjestetään sen syvyyden arvojen mukaan seuraavaa syvyyttä varten, jotta alfa-beeta karsinta toimisi tehokkaammin. Tekoälyn vuorolla on aikaraja, jos se loppuu kesken, niin edellisen syvyyden paras siirto palautetaan.

### minimax

Minimax algoritmin muunnelma on sen heuristisen arvion kanssa. Heuristista arvoa ei arvioida vain syvyydellä 0 tai kun jompi kumpi pelaaja on voittanut, niin kuin normaalissa minimax algoritmissa, vaan jokaisen siirron jälkeen.
Aluksi ennen miminax algoritmin kutsua arvioidaan `heuristinen_funktio` metodilla, joka arvioi koko pelilaudan "normaaliin tapaan" ja palauttaa arvion pelitilanteesta. Tämä arvio `heuristinen_arvo` annetaan minimaxille parametriksi. Jokaisen siirron jälkeen `for siirto in siirrot[::-1]:` arvioidaan siirron vaikutus ennen uutta minimax kutsua laudalla koomennolla: 
```
uusi_heuristinen_arvo = heuristinen_arvo + self.heurstisen_arvon_delta(pelilauta, syvyys, siirto)
```
ja `uusi_heuristinen_arvo` annetaan minimax metodille parametriin `heuristinen_arvo`. Miksi näin tehdään eikä vain arvioida pelitilannetta syvyydellä 0 tai kun jompi kumpi pelaajista on saanut yli 4 peräkkäin? Tähän on kaksi syytä

- Arvioitaessa pelitilannetta voidaan arvioon liittää aina kerroin, joka riippuu syvyydestä, sillä tiedetään helpisti millä syvyydellä aina mikäkin liike on tehty ja sen vaikutus arviointiin. Tämä on hyödyllistä sillä jos minimaxin maksimi syvyys on pariton, niin maksimioija saa aina yhden siirron enemmän, jolloinka se saisi yhtä monta merkkiä peräkkäin vaikka lähtötilanteessa minimoijalla olisi yksi merkki enemmän peräkkäin. </br>
- Tämä on oikeastaan nopeampaa, sillä arvioidaan vähemmän ruutuja, sillä normaalisti arvioitaisiin kaikki rivit tai minimissään pitäisi arvoida suuri osa riveistä. Seuraava kappale selittää miten `heurstisen_arvon_delta` toimii karkeasti ottaen.

metodi `heurstisen_arvon_delta` arvioi vain vaaka pysty ja molemmat vinot rivit jotka kulkevat juuri äskeisen siirron ruudun kautta (eli 4 riviä). Metodi ensin arvioi edellämainitut 4 riviä ilman äskeistä siirtoa laittamalla sirron ruutuun tyhjän ruudun ja sen jälkeen siirron kanssa, jolloin ruutuun ollaan laitettu äskeisen siirron merkki (eli 4 riviä 2 kertaa arvioitu). Metodi ottaa molemmista pelitilanteista arvion ja palauttaa `jälkimmäinen arvio - ensimmäinen arvio` ja kertoo tämän viellä kertoimella, joka vähänee mitä syvemmällä ollaan menty minimax algoritmissa, eli syvemmällä tehdyt liikkeet vaikuttavat minimaxin heuristiseen arvoon vähemmän.

### Pelitilanteen arvioinnin heuristiikka

Pelilaudan rivejä (vaaka, pysty tai vino) arvioidaan aina kerrallaan. Arvioinnissa aloitetaan aina rivin alusta ja mennään yksi ruutu eteenpäin kerrallaan. Jos samoja merkkejä on enemmän kuin yksi peräkkäin, niin heristista arvoa lisätään. Arvioon vaikutta peräkkäisten merkkien päädyissä olevat ruudut, onko ne tyhjiä vai onko niissä toisen pelaajan merkkejä. Jos molemmilla puolilla on toisen pelaajan merkki, niin jonolle samoja merkkejä ei anneta arvoa, ellei merkkien pituus ole 5 tai yli. Kun toinen puoli jonosta peräkkäisiä merkkejä on blokattu vastustajan merkillä, niin jonolle annetaan pienempi arvo seuraavan koodin mukaan (5 tai yli peräkkäin on arvoltaan 10<sup>11</sup>-10<sup>maksimi_syvyys-nykyinen_syvyys</sup>)

```
arvot = {2: 10, 3: 100, 4: 1500}
if molemmilla_puolilla_tyhja:
    arvot = {2: 100, 3: 1500, 4: 100_000}
```
Arvioinnissa käytetään myös heuristiikkaa, joka ottaa huomioon yhden tyhjän rivin kahden samanmerkkisen jonon välissä. Esim. rivillä kohta `"xx-xx"` ("-" esittää tyhjää ruutua) arvioitaisiin, että siinä olisi neljä peräkkäin, mutta sen saama arvo neljä peräkkäin kerrottaisiin vakiolla 0.85, sillä se voidaan katkaista keskeltä, joten sen arvo ei ole välttämättä sama kuin 4 peräkkäin ilman tyhjää ruutua välissä. Koodi on myös optimoitu ottamaan huomioon tilanteet, jossa on monta katkonaista saman merkkistä jonoa `"-x-x-xx-xx-"`. Tässä arvioitasiin ensin kaksi yhden pituista yhteen (uusi pituus 2) ja kaksi kahden pituista yhteen (uusi pituus 4), sillä se tuottaisi suurimman arvon. Heuristiikka ei arvioi enempää kuin 2 katkonaista jonoa yhteen, edellisessä tapauksessa saataisiin 6 merkkiä peräkkäin muuten.

## Aika ja tilavaativuudet

- minimax algoritmin aikavaativuus on tällä hetkellä O(n<sup>a</sup>), missä a on sen syvyys ja n on syötteen, eli ristien ja nollien määrä.
- heuristiikka arvioidaan kahdella metodilla, mutta molempien aikavaativuus on O(1), mutta nopeampaa tapaa käytetään minimax algoritmissa, joten se nopeuttaa ohjelemaa huomattavasti vakiokertoimien takia.

## Työn mahdolliset puutteet ja parannusehdotukset

- Koodin sisäistä rakennetta voisi parantaa jonkin verran
- Testausta voisi aina olla enemmän
- Minimax algoritmia voisi nopeuttaa, sillä se voi hyvällä tuurilla vain laskea kohtuullisessa ajassa syvyydellä 4
    - Siirtoja jotka eivät vaikuta hyviltä voisi karsia pois laskennasta
    - transpositiotaulun implementointi olisi ollu mahdollisesti viisasta, mutta se ei välttämätt ole ihan yksi yhteen tämän projektin minimaxin kanssa, sillä pelitilanteen arviointi riippu siirtojen syvyydestä, mutta pieni muutos arviointii mahdollistaisi sen.
- heuristista arviointia voisi parantaa, jolloloinka pienempi syvyys ei ole yhtä merkittävää


## Työn kaikki lähteet

[kurssin minimax moniste](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)
