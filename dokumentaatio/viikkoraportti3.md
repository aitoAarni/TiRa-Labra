# Viikkoraportti

## Mitä olen tehnyt tällä viikolla?

Tällä viikolla ohjelman peli tuli valmiiksi, yksikkötestaaminen aloitettu sekä yksikkötestiraportit näkyvät codecovissa.

## Miten ohjelma on edistynyt?

Muuten sujuvasti, mutta yksikköstestien kanssa oli iso vääntäminen saada importit toimimaan. Sain ne kuitenkin monen tunnin jälkeen toimimaan.

## Mitä opin tällä viikolla / tänään?

lähinnä opin uudestaan unohdettuja tai täysin uusia asioita pygameiin liittyen.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

Tässä juuri nuo yksikkötestit pytest kirjasto ja unittestien kanssa jäi vähän auiki. Koodi toimii normaalissa käytössä esim importilla from peli.main import Peli, 
mutta kun haluaa samaa koodia testata, niin pitää importtaa from src.peli.main import Peli. Lisäsin alkuun sys.path.append("./src") niin testit toimivat, 
mutta en oikein ymmärrä mistä tämä johtuu sillä testien working directory on kuitenkin sama.

## Mitä teen seuraavaksi?

Seuraavaksi aloitan minimax algoritmin toteuttamisen peliä varten.
