# Enhanced Annotations #

* Authors: George Kerscher, Noelia Ruiz Martínez

No DAISY Consortium, as boas prácticas desenvólvense para publicadores e
autores para proporcionar descricións extendidas (longas).

As boas prácticas utilizan o elemento HTML details que siga a imaxe, ou unha
ligazón a outro arquivo que conteña a descrición extendida.

En ambas opcións, o usuario tería que moverse ós detalles ou a ligazón e
activala.

Ter un atallo de teclas que poña o foco nos detalles ou na ligazón sería
ideal.

As nosas boas prácticas recomendan que os detalles ou a ligazón sigan
inmediatamente á imaxe, e se se segue a ligazón, débese proporcionar un
botón atrás exactamente á mesma ubicación. Isto asegura que o usuario non se
perderá.

Porén, é probable que os autores, na práctica, coloquen a descrición
extendida (longa) case en calquera lugar. Neses casos, o usuario querería
volver á imaxe, e de aí a necesidade dunha maneira de volver á imaxe
orixinal.

Este complemento proporciona ambas características, en soporte [desta
incidencia aberta no repositorio de NVDA][2].

## Ordes ##

* NVDA+alt+D: move o cursor ó elemento identificado con aria-details.
* NVDA+alt+shift+D: move o cursor ó elemento orixinal, por exemplo, unha
  imaxe con máis detalles como unha descrición longa. Se se premeu
  NVDA+alt+d varias veces para moverse a anotacións realizadas, é posible
  volver a cada unha delas.

As ordes anteriores pódense modificar dende o menú de NVDA, submenú
Preferencias, diálogo de Xestos de entrada, categoría Modo exploración.

## Cambios para 2.0 ##

* Engadida a posibilidade de moverse rapidamente entre varias orixes de
  anotacións.
* Require NVDA 2023.1 ou posterior.

[[!tag dev stable]]

[2]: https://github.com/nvaccess/nvda/issues/13940
