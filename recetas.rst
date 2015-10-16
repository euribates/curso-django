Recetas Habituales en Django (Que siempre se me olvidan)
=======================================================================

¿Cómo probar las páginas de errores (404, etc...) en desarrollo?
-----------------------------------------------------------------------

Para ver esas páginas de error, hay que desactivar la opción ``DEBUG``
de la configuración. Pero si lo hacemos, los contenidos estáticos dejan de
servirse, así que no podemos estar seguros de como se verán las páginas
finales, a no ser que instalemos nuestro propio servidor de contenidos 
estáticos.

O, por otro lado, podemos usar el flag ``insecure`` al llamar a ``runserver``::

    manage.py runserver --insecure

Esto obliga al servidor de desarrollo a servir los ficheros a partir
de los directorios ``static`` de las aplicaciones, aunque la variable
``settings.DEBUG`` sea ``False``. 

De ninguna manera debemos usar este truco para poner en explotación un
servidor de desarrollo de Django. Citando la documentación oficial:

    [...] By using this you
    acknowledge the fact that it’s grossly inefficient and probably insecure.
    This is only intended for local development, should never be used in
    production [...]

¿Cómo analizar las consultas SQL que está realizando Django?
------------------------------------------------------------------------

Normalmente el primer paso para poder optimizar Django consiste en analizar
el número de consultas, así como los tiempos de ejecución de las mismas. Para
ello hay una extensión muy recomendable: **Django-debug-toolbar**.

    pip install django-debug-toolbar

    http://django-debug-toolbar.readthedocs.org/en/1.4/
    https://pypi.python.org/pypi/django-debug-toolbar

    The Django Debug Toolbar is a configurable set of panels that display
    various debug information about the current request/response and when
    clicked, display more details about the panel’s content.

Lo ideal es poner esta app en desarrollo, y no en el despliegue final. Véase
la siguiente entrada

¿Cómo tener diferentes entornos de desarrollo/explotación/pruebas?
-------------------------------------------------------------------------

Mi solución actual, adaptada del muy recomendable 
libro `Two Scoops of Django`_, consiste en tener un ``settings.py``
que será el que se use en despliegue y luego un fichero 
``development.py``, que simplemente importa todo el contenido
del ``settings.py`` y realiza las modificaciones que crea oportunas.

Por ejemplo::

    from main.settings import *

    DEVELOPMENT = True

    INSTALLED_APPS += (
        'debug_toolbar',
        )

Para arrancar en desarrollo uso::

    manage.py runserver --settings=main.development

¿Como hago para que mi método booleano se vea bonito en el admin?
------------------------------------------------------------------------

Esta documentado, pero a menudo resulta complicado de encontrar. Si escribimos
un método de un modelo que devuelve solo ``True`` o ``False``, y lo consultamos
en el admin, este nos muestra texto. Sin embargo, para campos definidos como
booleanos (``BooleanField``) nos muestra un icono. Podemos hacer que utilice
esos mismos iconos si añadimos un atributo ``boolean`` al método.

por ejemplo::

    def nacio_en_bisiesto(self):
        year = self.birthday.year    
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    nacio_en_bisiesto.boolean = True

¿Como hago para mostrar mi propio contenido html en el admin?
-------------------------------------------------------------------------

Para que el admin interprete cualquier texto producido por un método 
como Html, sin escaparlo, debemos asignarle al método en cuestión
el atributo ``allow_tag`` a ``True``. Es recomendable que nos escudemos
de posibles fallos de seguridad usando la función ``format_html()`` siempre
que incluyamos en la salida texto generado por el usuario final.


Por ejemplo::

    def colored_name(self):
        return format_html('<span style="color: #{};">{} {}</span>',
                        self.color_code,
                        self.first_name,
                        self.last_name)

    colored_name.allow_tags = True

.. _Two Scoops of Django: http://twoscoopspress.org/products/two-scoops-of-django-1-8
