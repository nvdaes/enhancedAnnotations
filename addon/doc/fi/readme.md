# Laajennetut merkinnät #

*	Authors: George Kerscher, Noelia Ruiz Martínez
* [download stable version][1] (compatible with NVDA 2023.1 and beyond)

DAISY-konsortiossa kehitetään parhaita käytäntöjä julkaisijoille ja
tekijöille laajennettujen (pitkien) kuvausten antamiseen.

Parhaissa käytännöissä käytetään HTML:n tietoelementtiä (details), joka
seuraa kuvaa tai linkkiä toiseen tiedostoon, joka sisältää laajennetun
kuvauksen.

Molemmissa vaihtoehdoissa käyttäjän on siirryttävä tietoihin tai linkkiin ja
aktivoitava se.

Ihanteellista on,  että kohdistus siirtyy tietoihin tai linkkiin tiettyä
näppäinkomentoa painamalla.

Parhaat käytännöt suosittelevat, että tiedot tai linkki seuraa välittömästi
kuvaa, ja jos linkkiä seurataan, tulee käytettävissä olla tarkasti
edelliseen kohtaan siirtävä linkki. Tämä varmistaa, ettei käyttäjä eksy.

On kuitenkin todennäköistä, että tekijät sijoittavat laajennetun (pitkän)
kuvauksen melkein minne tahansa. Näissä tapauksissa käyttäjä haluaa palata
kuvaan, ja siksi tarvitaan tapa palata alkuperäiseen kuvaan.

Tämä lisäosa tarjoaa molemmat ominaisuudet, jotka tukevat tätä [NVDA:n
lähdekoodivarastossa avattua ongelmaa][2].

## Komennot ##

* NVDA+Alt+D: siirtää kohdistimen aria-details-attribuutilla merkittyyn
  elementtiin.
* NVDA+alt+shift+d: moves the cursor to the original element, for example,
  an image with furter details like a long description. If NVDA+alt+d has
  been pressed several times to move to related annotations, it'll be
  possible to go back to each origin.

Yllä olevia komentoja voidaan muokata kohdasta NVDA-valikko ->
Asetukset-alivalikko -> Näppäinkomennot-valintaikkuna ->
Selaustila-kategoria.

## Changes for 2.0 ##

* Added ability to move back through multiple annotation origins.
* Requires NVDA 2023.1 or later.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
