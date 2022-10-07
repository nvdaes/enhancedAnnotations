# Laajennetut selitteet #

* Tekijät: George Kerscher ja Noelia Ruiz Martínez
* [Lataa vakaa versio][1] (yhteensopiva NVDA 2022.1:n ja sitä uudempien
  kanssa)

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
* NVDA+Alt+Vaihto+D: siirtää kohdistimen alkuperäiseen elementtiin,
  esimerkiksi kuvaan, jossa on tarkempia tietoja, kuten pitkä kuvaus.

Yllä olevia komentoja voidaan muokata kohdasta NVDA-valikko ->
Asetukset-alivalikko -> Näppäinkomennot-valintaikkuna ->
Selaustila-kategoria.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
