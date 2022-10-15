# Verbesserte Annotations #

* Autoren: George Kerscher, Noelia Ruiz Martínez
* [Stabile Version herunterladen][1] (kompatibel mit NVDA 2022.1 und neuer)

Im DAISY-Konsortium werden Best Practices für Verlage und Autoren
entwickelt, um erweiterte (lange) Beschreibungen bereitzustellen.

Am besten verwenden Sie das HTML-Details-Element, das auf das Bild folgt,
oder einen Link zu einer anderen Datei, die die erweiterte Beschreibung
enthält.

Bei beiden Optionen müsste der Nutzer zu den Details oder dem Link gehen und
ihn aktivieren.

Ein Tastendruck, um den Fokus auf die Details oder den Link zu legen, ist
ideal.

Unsere Best Practices empfehlen, dass die Details oder der Link unmittelbar
auf das Bild folgen, und wenn dem Link gefolgt wird, muss ein Backlink zum
genauen Standort angegeben werden. So wird sichergestellt, dass der Nutzer
sich nicht verliert.

Es ist jedoch wahrscheinlich, dass viele Autoren die erweiterte (lange)
Beschreibung fast überall platzieren. In diesen Fällen würde der Benutzer zu
dem Bild zurückkehren wollen, und daher ist eine Möglichkeit erforderlich,
zum Originalbild zurückzukehren.

Diese Erweiterung bietet beide Funktionen, um dies zu unterstützen [Problem
eingereicht im NVDA-Repository][2].

## Befehle ##

* NVDA+Alt+D: Zieht den Cursor auf das mit "aria-details" gekennzeichnete
  Element.
* NVDA+Alt+Umschalt+D: Zieht den Cursor auf das ursprüngliche Element,
  z. B. ein Bild mit weiteren Details wie einer langen Beschreibung.

Die oben genannten Tastenbefehle können über die Einstellungen im NVDA-Menü
im Dialogfeld für die Tastenbefehle und dort in der Kategorie "Lesemodus"
geändert werden.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
