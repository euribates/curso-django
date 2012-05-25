Introducción a Python
---------------------------

Estructuras de datos
===========================

Tipos de datos básicos:

 * números (int, long, float, complex)
 * logicos (bool)
 * texto, string y unicode

Tipos de datos compuestos:

 * Listas
 * Diccionarios
 * Tuplas
 * Conjuntos

Estructuras de control
=============================

if

for

while

Funciones, clases y modulos
=============================

Funciones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una función no es más que un fragmento de programa que queremos
reutilizar. Para ello le damos un nombre. también definimos unos nombres
para las variables que les vamos a pasar, si es que se le
pasa alguna. En este caso, estas variables que sirven para pasar
información hacia o desde la función se llaman **parámetros**. También
podemos especificar, si lo queremos, uno
o varios valores de retorno (Para los que hayan levantado una ceja
cuando han visto lo de "varios valores de retorno", esplicaremos
esto en la última sección de este capítulo, "Para programadores
con experiencia en otros lenguajes").

Veamos con un ejemplo una función, la que nos da el perímetro
de una circuferencia pasándole el radio de la misma::

    def perimetro_circunferencia(radio):
        import math
        perimetro = 2 * math.pi * radio
        return perimetro

la palabra resevada ``def`` nos permite definir funciones. Después del
``def`` viene el nombre que le queremos dar a la función, y luego, entre 
paréntesis, va el parámetro o parámetros de entrada de la función, separados
por comas. Si no hubiera ningún paŕametro, aún así hemos de incluir los
paréntesis. Finalmente, viene el signo de dos puntos. Todo el código
que aparezca a continuación indentado a un nivel mayor que la palabra ``def``
forma parte del cuerpo de la función. Ahora podemos "llamar" o "invocar" a
esta función desde cualquier parte de nuestro programa, simplemente usando
su nombre, por ejemplo, el siguiente codigo imprime el resultado de
calcular el perímetro de una circunferencia de radio 7::

    # suponemos definida antes la func. perimetro_circunferencia

    radio = 6
    print 'El perímetro de una circunferencia de radio'
    print radio 
    print 'es'
    print perimetro_circunferencia(radio)

Para el que esté interesado, el paso de variables en Python siempre es
por referencia, no por valor.

El paso de parámetros también es interesante, y ofrece posibilidades
en python que no todos los lenguajes soportan. 

La forma habitual de paso de parámetro es por posición, es decir, cuando
llamemos a una funcion definida con varios parámetros, el primer
dato que pongamos tras los paréntesis ocupará el lugar del primer parámetro, el
segundo valor ocupará el segundo parámetro y así sucesivamente. En estos casos,
hay que pasar tantos valores como parámetros se hayan definido en la función.

Python soporta también el paso de parámetros por nombre y los parámetros
por omisión. Veamos estos dos casos, que están muy relacionados, con un ejemplo.

Supongamos que necesitamos escribir una funcion que determine el área de un triángulo. ¿que
parámetros necesita? Sabiendo que el área de un triángulo puede calcularse
con la fórmula *base* por *altura* partido por dos, parece lógico suponer
que necesitaremos dos parámetros, base y altura del triángulo. la función
podría ser algo así::

    def area_triangulo(base, altura):
        return (base * altura) / 2.0

A la hora de llamar a la función

Con python podemos tener valores opcionales y paso de parámetros con nombre










en la lista de 


Librerías incluidas
=============================

Para programadores con experiencia en otros lenguajes
=======================================================

Python, como cualquier otro lenguaje, tiene sus formas particulares
de realizar algunas tareas, algunas de ellas pueden ser más
sorprendentes para programadores que provengan de otros lenguajes
que para una persona que empieze de cero. [Escena del titanic]

Vamos a ver rápidamente algunas de estos modismos o costumbres
que pueden sorprender a los más experimentados.

Para definir bloques de código se usa el sangrado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es decir, no hay marcas de principio y fin de bloque, como en Pascal, Delphi
(BEGIN, END) o C, Java, C# (Llaves de apertura y cierre { y }). La indentación
del código marca el principio del bloque (cuando aumenta) y el fin del bloque
(cuando desminuye). Esto parecerá extraño a la mayoría de los programadores,
que están acostumbrados a que los espacios no sean significativos.

Sin embargo, tiene muchas ventajas:

 * La mayoría de los desarrolladores ya indentan el código de todas maneras.
 Usar el indentado para marcar los límites de los bloques de código simplifica
 la escritura y, sobre todo, la lectura del mismo. Presentele un trozo de
 código java relativamente complejo y sin ninguna indentación a un programador
 y lo primero que hará este, en un 99% de los casos [#n1]_, es indentar el código
 a su gusto mientras lo lee para entender como funciona.
   
 * En otros lenguajes, el indentado solo tiene una función decorativa, es una
 forma de simplificar la lectura del mismo, pero no tiene ningún significado
 real; la estructura será la que indiquen los marcadores de principio y fin de
 código. Muchos programadores se han dejdo las pestañas intentando encontrar un
 error en el flujo del programa porque ha indentado mal (o ha indentado bien
 pero se le han escapado un par de llaves, por ejemplo). Si el indentado y las
 marcas no concuerdan, puede ser un problema, porque es mucho más fácil leer el
 indentado que las marcas, sobre todo si el código es extenso.

 * No hay distintas formas de indentar código. En C y sus derivados hay tantas
 formas que incluso se agrupan por familias, según su semejanza. Casi podriamos
 decir que hay tantos estilos de indentación como desarrolladores. En Python
 solo hay que limitarse a decidir entre espacios y tabuladores --lo recomendado
 son espacios-- y en su caso, cuantos espacios usar para cada nivel de
 indentación --lo recomendado son 4 espacios--.

 * Además, nos ahorramos dos caracteres o palabras reservadas, que se pueden
 usar en otras partes.

No hay métodos ni propiedades privadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En lenguajes orientados a objetos como C++, java o C# a veces es posible
proteger determinados métodos o propiedades de nuestras clases, de
forma que sea imposible usarlas y/o modificarlas. En Python no se puede [#n2]_,
todos los métodos y atributos son públicos. No existe nada que sea "privado" en
el sentido de Java o C++. 

Eso si, no es un fallo en el lenguaje, es una decisión tomada conscientemente y
forma parte del diseño del lenguaje. La documentación de Python lo explica de
la siguiente manera: "Aquí somos todos adultos y conocemos las reglas del
juego". Algunos consideramos que la misma idea de ocultar o esconder parte del
código es "poco pythonico". Así, ninguna clase ni ningún objeto puede mantener
sus mecanismos internos ajenos al resto de los desarrolladores. Esto hace que
la introspección sea, no solo posible, sino además, sencilla y potente. 

La filosofía es que Python confía en ti y en tus habilidades. Viene a ser algo
así: "Si consideras necesario meterte por los recovecos y usar métodos que no
están diseñados para el usuario final, adelante, pensaremos que tienes una
buena razón para hacerlo, pero no digas luego que la culpa es nuestra. Aquí
somos todos adultos y todos conocemos las reglas del juego".

Perl tiene una filosofía similar que expresa de la siguiente forma: "[Los
modulos] de Perl prefieren que te mantengas fuera de su sala de estar, pero que
lo hagas no porque tengas una escopeta de cañones recortados, sino porque no
estás invitado."

Estructuras de datos integradas en el lenguaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En otros lenguajes, hay estructuras de datos como
pilas, colas, mapas (hash), tuplas, etc... que, por su gran utilidad,
están implementadas como librerías. Python da un paso más alla, y estas
estructuras de datos, entre otras, forman parte nativa del lenguaje. Esto
permite que el lenguaje interactue con estas estructuras de forma
mucho más fluida.

El bucle ``for``, por ejemplo, está diseñado nativamente para que
itere sobre aquellas estructuras de datos que sean "iterables". Veamos
lo que significa esto con un ejemplo: Para imprimir una lista de 
nombres guardados en la variable ``lista``, en C, haríamos::

    include <stdio.h>

    void main(int argc, char *argv[]) {
        char * lista[] = {"hola", "mundo", "cruel"};
        int i, n = sizeof(l)/sizeof(char *);
        for (i=0; i<n; i++) {
            puts(l[i]);
            }
        }

en Python, sería::

    lista = ("hola", "mundo", "cruel")
    for s in lista:
        print s

El resultado es el mismo en los dos casos, pero la legibilidad es mucho
mayor en el segundo. No hay ni cálculo de tamaño, ni comprobaciones
para no superar el límite, ni incremento de variables auxiliares ni, ya
puestos, variables auxiliares. La magia no existe, la operaciones siguen
siendo necesarias, pero se hacen internamente, con más rápidez y menos 
posibilidad de error [#n3]_. 

Las Funciones pueden devolver más de resultado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En otros lenguajes, las funciones solo pueden devolver un único resultado. En
python, las funciones pueden devolver más de una variable. Esto es posible
gracias a que la variables de tipo tupla son una estructura integrada (véase
punto anterior), y gracias a una técnica conocida con el simpático nombre de
*empaquetado y desempaquetado automático de tuplas*. La mejor manera de
entenderlo es con un ejemplo::

    def division_y_resto(dividendo, divisor):
        return dividendo // divisor, dividendo % divisor

    cociente, resto = division_y_resto(47, 9)
    print 'cociente:', cociente
    print 'resto:', resto

Este pequeño programa nos informa de que 47 dividido por 49 da cinco, con resto dos, o dicho
de otra manera, que (9 * 5) + 2 = 47

Las asignaciones pueden encadenarse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gracias a la magia de las tuplas y al empaquetado y desempaquetado automatico de
las mismas, junto con algún que otro truco, las expresiones siguientes son
posibles::

    a = b = c = d = 0

Y significan lo que uno podría esperarse, las variables ``a``, ``b``, ``c`` y
``d`` se inicializan a cero.

También podemos intercambiar los valores de dos variables sin necesidad de 
recurrir a variables intermedias::

    a,b = b,a

Las comparaciones también pueden escribirse de forma más legigle que en otros
lenguajes, por ejemplo, para comprobar que la variable ``a`` está entre cero y
cien, podemos expresarlo así::

    if a > 0 and a < 100:
        print 'OK'

o, más legible::

    if 0 < a < 100:
        print 'OK'


Las funciones son objetos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las funciones son objetos en si mismo, es decir, que podemos hacer con ellas
cosas que en otros lenguajes serían imposibles. Por ejemplo, podemos tener un
array de funciones, o podemos pasar una función --ojo, no el resultado de una
función, sino la función en si-- como parámetro de otra función. Esto no
sorprenderá en absoluto a aquellos que hayan tenido experiencia con lenguajes
funcionales, pero si a aquellos que sólo estén acostumbrados a lenguajes
imperativos.


.. rubric:: Footnotes

.. [#n1] Si perteneces al 99% te extrañará que exista siquiera ese 1%. Hay gente
   para todo.

.. [#n2] En realidad si se puede, porque en Python se puede hacer casi todo, pero
   es poco pythonico, la sintaxis es confusa y las razones de uso casi siempre
   inexistentes.

.. [#n3] En C uno de los errores más frecuentes era acceder con un puntero a
   direcciones de memoria posteriores a las que ocupaba una variable,
   provocando todo tipo de fallos. Eran tantos los errores de este tipo que
   incluso recibieron un nombre: *buffer overrun* o desbordamiento de buffer.

