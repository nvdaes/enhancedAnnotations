# Anotaciones mejoradas #

*	Authors: George Kerscher, Noelia Ruiz Martínez
* [download stable version][1] (compatible with NVDA 2023.1 and beyond)

En el consorcio DAISY, se desarrollan buenas prácticas para que los
publicadores y autores proporcionen descripciones extendidas (largas).

Las buenas prácticas usan el elemento details de HTML que sigue a la imagen,
o un enlace a otro archivo que contenga la descripción extendida.

En ambos casos, el usuario tendría que desplazarse a los detalles o al
enlace y activarlo.

Tener un atajo que sitúe el foco en el enlace o los detalles es ideal.

Nuestras buenas prácticas recomiendan que tanto el enlace como los detalles
vayan inmediatamente después de la imagen, y si se sigue el enlace, se debe
proporcionar un enlace de vuelta a la ubicación exacta. Esto garantiza que
el usuario no se perderá.

Sin embargo, es probable que los autores sitúen la descripción extendida
(larga) casi en cualquier parte. En estos casos, el usuario querría volver a
la imagen, de ahí la necesidad de una forma de regresar a la imagen
original.

Este complemento proporciona ambas características, como apoyo a esta
[incidencia abierta en el repositorio de NVDA][2].

## Órdenes ##

* NVDA+alt+d: mueve el cursor al elemento identificado con aria-details.
* NVDA+alt+shift+d: moves the cursor to the original element, for example,
  an image with furter details like a long description. If NVDA+alt+d has
  been pressed several times to move to related annotations, it'll be
  possible to go back to each origin.

Las órdenes anteriores pueden modificarse desde el menú NVDA, submenú
Preferencias, diálogo Gestos de entrada, categoría Modo exploración.

## Changes for 2.0 ##

* Added ability to move back through multiple annotation origins.
* Requires NVDA 2023.1 or later.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
