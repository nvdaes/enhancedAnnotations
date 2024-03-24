# Laajennetut merkinnät #

* Tekijät: George Kerscher ja Noelia Ruiz Martínez

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
  esimerkiksi kuvaan, jossa on tarkempia tietoja, kuten pitkä kuvaus. Jos
  NVDA+Alt+D:tä on painettu useita kertoja liittyviin merkintöihin
  siirtymiseksi, kuhunkin alkuperään on mahdollista palata takaisin.

Yllä olevia komentoja voidaan muokata kohdasta NVDA-valikko ->
Asetukset-alivalikko -> Näppäinkomennot-valintaikkuna ->
Selaustila-kategoria.

## Muutokset versiossa 2.0 ##

* Lisätty mahdollisuus siirtyä useita merkintöjen alkuperiä taaksepäin.
* Edellyttää NVDA 2023.1:tä tai uudempaa.

[[!tag dev stable]]

[2]: https://github.com/nvaccess/nvda/issues/13940
