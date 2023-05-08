kattavuusraportti yksikkötesteistä: [![codecov](https://codecov.io/gh/aitoAarni/TiRa-Labra/branch/main/graph/badge.svg?token=G521CJR0IT)](https://codecov.io/gh/aitoAarni/TiRa-Labra)

![Kattavuusraportti](https://user-images.githubusercontent.com/13611438/236777503-54125732-02f6-4ad0-a7b7-9048ae893fb7.png)


Projektia on testattu yksikkötesteillä. Yksikkötestit toteutettin automaattisella ohjelmalla. Testauksen syötteet katsovat osittain myös ääritapauksia ja niitä on lisätty viikosta 5 eteenpäin. 

Yksikkötesteillä testataan kaikkea muuta ohjelmasta paitsi konfiguraatio koodia sekä käyttöliittymää. Ohjelmassa on pääsääntöisesti koitettu testeata jokaisen luokan jokaista metodia yhdellä tai useammalla syötteellä. Ohjelman melkein jokainen "branchi" on koitettu testata ainakin yhdellä syötteellä. Heuristista arviontia ollaan jokseenkin testattu, mutta minimax algoritmin oikeellisuutta ei olla oikein testatttu monimutkaisiisa tapauksissa. Testauksessa on mukana testaus konfiguraatio tiedosto, joka eroaa tuotanto konfiguraatio tiedostosta, joten muutos toiseen ei sotke konfiguraatiota toisessa.
