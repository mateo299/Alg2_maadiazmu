Punto 1: Este problema plantea la solucion a una multiplicacion usando el metodo Rossen 
Para esto, y durante toda la ejecucion del algoritmo solo es necesario el uso de un solo ciclo, 
todo lo demas se podria despreciar al ser tiempos de ejecucion constantes. 
El tiempo de ejecucion de este ciclo se define por el valor de una de las entradas (n), 
y este valor se ve modificado en cada ciclo al ser dividido por 2, 
asi el tiempo es O(n/2) el cual es el mas significativo de todo el algoritmo.
*******************
Punto 2: Este problema plantea generar una cadena de texto usando dos "diccionarios" diferentes, 
uno con 10 carácteres y otro con 26. 
Al evaluar la complejidad de este algoritmo, podremos notar que la complejidad de la primera 
parte del problema depende del tamaño del primer diccionario (n) y del segundo (m), 
dando una complejidad de **O(n^3*m^3)**