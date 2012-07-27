Vistas
=======================================================================

Una vista es una función o una clase de python normal, pero que debe cumplir
los siguientes requisitos:

 * Admite como parámetro una variable de tipo ``HttpRequest``. La función puede
   aceptar más de un parámetro, pero la variable de tipo ``HttpRequest`` ha
   de ser el primero de ellos.

 * Devuelve una instancia del tipo ``HttpResponse``.



