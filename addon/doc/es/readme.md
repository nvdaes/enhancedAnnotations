# Anotaciones mejoradas #

* Autores: George Kerscher, Noelia Ruiz Martínez

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

This add-on provides both features, in support of this [issue opened in
NVDA's repository][1].

## Órdenes ##

* NVDA+alt+d: mueve el cursor al elemento identificado con aria-details.
* NVDA+alt+shift+d: mueve el cursor al elemento original. Por ejemplo, una
  imagen con más detalles, como una descripción larga. Si se ha pulsado
  NVDA+alt+d varias veces para desplazarse a anotaciones relacionadas, será
  posible regresar a cada origen.

Las órdenes anteriores pueden modificarse desde el menú NVDA, submenú
Preferencias, diálogo Gestos de entrada, categoría Modo exploración.

## Cambios para 2.0 ##

* Se ha añadido la posibilidad de retroceder por varios orígenes de
  anotaciones.
* Se requiere NVDA 2023.1 o posterior.

[[!tag dev stable]]

[1]: https://github.com/nvaccess/nvda/issues/13940
