Plantillas
===============================================================================

Las plantillas en Django juegan, en parte, el rol de las V en el modelo MVC (Si, es un poco confuso). [Repetir ejemplo del hola mundo pero con plantillas]

Herencia de plantillas
-----------------------------------------------------------------------

Una de las partes más potentes de las plantillas es que mantiene un sistema
de herencia, equivalente al que podemos encontrar en cualquier sistema
orienta a objetos. Al igual que en estos sistemas, se parte de un concepto
general, que se va particularizando mediante herencias.

En los sistemas de plantillas que no tiene herencia, lo normal es que 
tengan la posibilidad de incluir otros ficheros. La herencia de
plantillas es similar, pero con un pequeño giro conceptual que lo hace
a la vez más sencillo y más potente, una vez se entiende su funcionamieno. 

En un sistema que trabaja con inclusión de ficheros, normalmente tenemos un
fichero de cabecera y un fichero de pie, que van respectivamente al principio y
al final de cada página. El código se limita a incluir la cabecera, hacer su
trabajo y a continuación incluir el pie. Con este sistema, lo que hacemos es
definir en los ficheros a incluir **las partes que son iguales para todas lás
páginas**.

Imaginemos que en el pie de cada página está nuestro teléfono de asistencia, y
que dicho número ha cambiado. Queremos que el cambio se refleje en todas las
páginas que hayamos hecho hasta ahora. Como hemos tenido la precaución de
separar el contenido del pie en un único fichero, el cambio es fácil.

Sin embargo, otros cambios no son tan fáciles. Imaginemos que nos piden ahora
otro cambio aparentemente trivial: que en el *title* de cada página vaya,
añadido al final, la dirección acortada de nuestra web. Es decir, que una
página titulada  "Acerca de", deberá titularse ahora como "Acerca de -
shield.com". Esto implica que la página de cabecera, que antes era *igual* para
cada página, ahora es *distinta* para cada página.


Ventajas de las plantillas
-------------------------------------------------------------------------------

El uso de un buen sistema de plantillas presenta muchas ventajas:

 * Las plantillas pueden ser editadas  y modificadas por especialistas en
   diseño o en ergonomía sin necesidad de tener conocimientos de 
   programación. Al fin y al cabo, son como cualquier otra pagina web, 
   solo que con algunas marcas especiales más. 

 * El sistema de herencias y la inclusión de plantillas es realmente potente,
   y permite realizar modificaciones globales en la aplicación tocando un solo
   fichero. 

 * El sistema deja que algunos problemas se puedan resolver usando etiquetas
   y filtros, y permite incluir un poco de lógica en las vistas, pero
   el sistema está diseñado expresamente para que estas etiquetas
   y filtros sean, desde el punto de vista de uin programador, pobres. 

   Aunque puede parecer extraño diseñar una parte del sistema para
   que sea débil, existe una filosofía detras. La idea es que las tareas
   realmente complejas se realizen en la vista, donde disponemos de toda
   la potencia del lenguaje Python, y que lo hagan los programadores. La
   lógica de la vista está pensanda para ayudar a los los diseñadores, no
   para crear un segundo lenguaje de programación.

Ejemplo

    * Mostrar una lista de elementos y que sean de color rojo si es par y verde si es impar

    * Mostrar una lista de superheroes, pero que se vean los nombres de color
    rojo si su nivel es de 5 o superior y verde si es 4 o inferior.





