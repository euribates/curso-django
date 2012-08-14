Qué es Django [95%]
===============================================================================

Django es un framework de desarrollo web. Un framework nos proporciona una
infraestructura sobre la que podemos construir nuestras propios desarrollos.
Tal y como  reza su lema, Django es *The Web Framewok for perfectionists with
deadlines*, es decir, el framework Django para perfeccionistas con fechas de
entrega. Es una meta ambiciosa, desde luego. El objetivo es poder crear
rápidamente aplicaciones web elegantes, potentes y de alto rendiento.

En el diseño de Django se tomaron desde el principio en cuenta ciertos
principios básicos, que determinan gran parte del porqué y el cómo se hacen
las cosas en Django. Una de estas reglas es conocida por sus iniciales en
inglés DRY_ (*Don't Repeat Yourself*). DRY presupone que toda duplicción del
código, ya sea por descuido o a propósito, conduce a pesadillas durante el
mantenimiento, dificulta las mejoras e incluye contradicciones lógicas. Un
ejemplo claro fue el llamado `problema del año 2000`_; en la mayoría de los
casos  el código responsable de trabajar con fechas no estaba unificado, sino
copiado y distribuido  a lo largo de todo el código, lo que dificultaba
enormente arreglar el problema.

Django nació como una aplicación interna, desarrollada para un periódico de
Kansas, el `Lawrence Journal World`_. El equipo de desarrollo de la versión
web del periódico, encabezados por Adrian Holovaty y Simon Willison, empezaron
a migrar el código de PHP a Python, y fueron añadiendo y agrupando diversas
funcionalidades que aparecían repetidas en diferentes proyectos, conformando
así poco a poco un pequeño framework, siguiendo la idea ya comentada de no
repetir código. 

Poco después Jacob Kaplan-Moss se incorporó al equipo y más o menos un año más
tarde convencieron a los dueños del periódico de las bondades que traería
publicar el framework como software libre. Según Willison, los dueños se
convencieron por dos factores principalmente, primero, el hecho de que se
hubiera liberado recientemente el código de `Ruby on Rails`_, un framework
similar escrito en Ruby_ y desarrollado por la gente de 37signals_, que lo
usaron para su producto estrella, Basecamp_. En segundo lugar, por la cantidad
de beneficios que durante muchos años había aportado el software libre a la
empresa, y el desea de esta de poder compensar y retornar algo a la comunidad.
Adrian decidió bautizar el framework como Django en honor de su guitarrista
favorito, `Django Reinhardt`_.

Conocimientos previos [05%]
-------------------------------------------------------------------------------

Se presupone en el lectos conocimiento, aun superficial, de las distintas
tecnologías que inciden a día de hoy en el desarrollo web.

Python, Html, CSS, http, javascript, sql

Estructura (e infraestructura) de la Web [05%]
-------------------------------------------------------------------------------

Esquema de como funciona una peticion web muy sencilla.

Esquema de como funciona una peticion web dinámica, con base 
de datos incluida

Esquema super complicado: Balanceo de carga, distribuidores, sistemas
 de cahces, bases de datos distibuidas, etc...

listado de responsabilidades:

    Http

    Html

    CSS

    javascript

    SQL

Cliente, servidor, peticion, respuesta, cabecera, tipos mime, contenido
estáticos frente a contenidos dinámicos. Bases de datos. Memorias caché.

Django está pensado para trabajar bien en cualquiera de estos escenarios, pero
especialmente en el escenario B, que, afortunadamente, es el más habitual.
Podríamos usar Django para un entorno muy sencillo, de pocas páginas estáticas,
pero sería el equivalente a matar moscas a cañonazos. En el entorno C, bastante
complejo y con necesidades y requerimientos muy grandes, puede quedarse corto.
No es que no se puedan hacer, per seguramente habrá que realizar una labor de
adaptación para conseguir el rendimiento deseado.

.. _DRY: http://c2.com/cgi/wiki?DontRepeatYourself

.. _Lawrence Journal World: http://www2.ljworld.com/

.. _Ruby: http://www.ruby-lang.org/es/
 
.. _Ruby on Rails: http://rubyonrails.org/

.. _37signals: http://37signals.com/

.. _Basecamp: http://basecamp.com/

.. _Django Reinhardt: http://es.wikipedia.org/wiki/Django_Reinhardt
