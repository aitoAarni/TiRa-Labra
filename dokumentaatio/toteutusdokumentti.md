# Toteutusdokumentti

## Yleisrakenne

Pelissä on valikko, josta voi risteille ja nollille joko ihmis- tai tekoälypelaajan, sekä pelilaudan ruutujen määrän. Pelin tekoäly käyttää minimax algoritmia (pienellä muunnelmalla), joka on raa'an voiman algoritmi.

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

### Pelitilanteen arvioinnin heurestiikka

Pelilaudan rivejä (vaaka, pysty tai vino) arvioidaan aina kerrallaan. Arvioinnissa aloitetaan aina rivin alusta ja mennään yksi ruutu eteenpäin kerrallaan. Jos samoja merkkejä on enemmän kuin kaksi peräkkäin, niin niille annetaan arvo. Arvioon vaikutta peräkkäisten merkkien päädyissä olevat ruudut, onko ne tyhjiä vai onko niissä toisen pelaajan merkkejä. Jos molemmilla puolilla on toisen pelaajan merkki, niin jonolle samoja merkkejä ei anneta arvoa, ellei merkkien pituus ole 5 tai yli. Kun toinen puoli jonosta peräkkäisiä merkkejä on blokattu vastustajan merkillä, niin jonolle annetaan pienempi arvo seuraavan koodin mukaan (5 tai yli peräkkäin on arvoltaan 10<sup>11</sup>-10<sup>(maksimi_syvyys-nykyinen_syvyys)</sup>)

```
arvot = {2: 10, 3: 100, 4: 1500}
if molemmilla_puolilla_tyhja:
    arvot = {2: 100, 3: 1500, 4: 100_000}
```
Arvioinnissa käytetään myös heurestiikkaa, joka ottaa huomioon yhden tyhjän rivin kahden samanmerkkisen jonon välissä. Esim. rivillä kohta "xx-xx" ("-" esittää tyhjää ruutua) arvioitaisiin, että siinä olisi neljä peräkkäin, mutta sen saama arvo neljä peräkkäin kerrottaisiin vakiolla 0.85, sillä se voidaan katkaista keskeltä, joten sen arvo ei ole välttämättä sama kuin 4 peräkkäin ilman tyhjää riviä välissä. Koodi on myös optimoitu ottamaan huomioon tilanteet, jossa on monta katkonaista saman merkkistä jono "-x-x-xx-xx-". Tässä arvioitasiin ensin kaksi yhden pituista yhteen (uusi pituus 2) ja kaksi kahden pituista yhteen (uusi pituus 4), sillä se tuottaisi suurimman arvon.

## Aika ja tilavaativuudet

- minimax algoritmin aikavaativuus on tällä hetkellä O(n<sup>3</sup>), sillä sen syvyys on 3 ja n on syötteen, eli ristien ja nollien määrä.
- Heurestisen funktion aikavaativuus tällä hetkellä on O(1), sillä se käy läpi vain viimeisimmän valitun merkin ruudusta lähtien vakaa, pysty sekä vinot rivit (sama myös pätee voiton tarkistus funktiolle).

## Työn mahdolliset puutteet ja parannusehdotukset




lähteet: [minimax.pdf](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)
