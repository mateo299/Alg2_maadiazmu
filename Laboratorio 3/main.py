#obtenemos valores del usuario
import time

xi = float(input("ingrese la cota inferior: "))
xs = float(input("ingrese la cota superior: "))

#def otras variables
errorPermitido = 0.001
error = 1
i=0
def poli(x): return -(x**4) + 30*(x**3) + 15*(x**2) + 34*x + 540
#Formato
print(f"  X  | Cota superior      | Cota inferior      | Reemplazo          | Error")
tiempo = time.time()
#Algoritmo
while abs(error) > errorPermitido: #Este ciclo no termina hasta que el error sea menor al deseado
    xa = (xi + xs)/2 #La mitad
    if poli(xi) * poli(xa) < 0: #Definir reemplazo
        xs = xa
    else:
        xi = xa
    error=abs(poli(xa))
    i=i+1
    print(f"{i:^5.0f}|{xs:20}|{xi:20}|{xa:20}|{error:20}")
print(f"La raiz es: {xa} con un error del {error}, completado en {i} iteraciones\nEl tiempo de ejecucion es{time.time() - tiempo: .10f}")