# Enhanced Annotations #

*	Authors: George Kerscher, Noelia Ruiz Martínez
* [download stable version][1] (compatible with NVDA 2023.1 and beyond)

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
* NVDA+alt+shift+d: moves the cursor to the original element, for example,
  an image with furter details like a long description. If NVDA+alt+d has
  been pressed several times to move to related annotations, it'll be
  possible to go back to each origin.

As ordes anteriores pódense modificar dende o menú de NVDA, submenú
Preferencias, diálogo de Xestos de entrada, categoría Modo exploración.

## Changes for 2.0 ##

* Added ability to move back through multiple annotation origins.
* Requires NVDA 2023.1 or later.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
