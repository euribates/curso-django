Tipos de campos disponibles
-----------------------------------------------------------------------

Django viene con un conjunto de tipos de campos bastante extenso, veremos
con más detalle cada uno de ellos. Los agruparemos según el tipo de datos
que usará la base de datos subyacente para almacenarlos:

Campos numéricos (Enteros o en coma flotante)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 + AutoField

 + BigIntegerField

 + DecimalField

 + IntegerField

 + FloatField

 + PositiveIntegerField

 + PositiveSmallIntegerField

 + SmallIntegerField
    
Campos lógicos (booleanos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 + BooleanField

 + NullBooleanField

Fechas y tiempos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 + DateField

 + DateTimeField

 + TimeField

Texto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 + CharField

 + CommaSeparatedIntegerField
    
 + EmailField

 + IPAddressField

 + GenericIPAddressField

 + SlugField

 + TextField

 + URLField

Ficheros
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los ficheros, en realidad, se almacenan en la base de datos en un campo
de texto variable, pero tiene unas cuantas particularidades que aconsejan
explicarlos aparte

 + FileField
        
 + FilePathField
    
 + ImageField

Cuando usamos un campo de tipo ``FileField`` o ``ImageField``, el archivo 
que subimos es almacenado por el servidor en el sistema de ficheros, y lo
que se guarda en la base de datos es una ruta parcial al mismo, en un 
campo de texto variable. La ruta absoluta en el sistema de 
ficheros (accesible mediante el atributo ``path`` del campo) se compone 
a partir de varios elementos:

 * En primer lugar, el valor que se haya almacenado en
   la variable ``MEDIA_ROOT``, definida en el fichero 
   ``settings.py``. Si no se ha modificado, el valor por
   defecto de esta variable es una cadena de texto vacía, que
   viene a significar el directorio de trabajo actual.

 * En segundo lugar, la ruta que se obtiene de evaluar 
   el parámetro ``upload_to`` con el que se definió el
   campo. Podemos usar códigos de formateo como los que 
   usamos en ``strftime()``; por ejemplo, usando ``%Y``
   conseguimos que en la ruta se sustituya ese código por
   el año del día es que se ha realizado la carga

 * En tercer lugar, el nombre original del fichero

 Por ejemplo, si la variable ``MEDIA_ROOT`` se definió
 como ``/var/media``, el campo de tipo ``FileField`` 
 o ``ImageField`` se definió con el parámetro ``upload_to`` igual a ``fotos/%Y/%m/%d``  y el nombre del fichero original era ``mifoto.jpg``, la ruta final (Si se hubiera subido el 27 de julio de 2013) sería::

 	 /var/media/fotos/2013/07/27/mifoto.jpg

Definir tu propio tipo de campo de datos
-----------------------------------------------------------------------

Si estos tipos de campos no son suficientes, podemos definir nuestros
propios tipos. Los detalles son un poco más complicados, pero en 
esencia lo único realmente importante es decirle a django dos cosas: Como
se almacena nuestro tipo de dato en la base de datos (normalmente en
un ``VARCHAR``), y a la inversa, como recuperar, a partir de lo almacenado,
el dato original.