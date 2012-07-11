Plantillas
===============================================================================

Las plantillas en Django juegan, en parte, el rol de las V en el modelo MVC (Si, es un poco confuso). Repetir ejemplo del hola mundo pero con plantillas

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





