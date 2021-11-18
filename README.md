# Alg2_maadiazmu
Algoritmos unal
Calculo de complejidad teorica Taller_grupal_1.ipynb

Funciones: 
'comp'------------------------------------------
def comp(a, b):					O(1)
    for i in range(len(a)):				O(n)
        if a[i] != b[i]: 				O(1)
	return False					O(1)
    return True					O(1)
TOTAL-------------------------------------------O(n)

'sbf'-------------------------------------------
def sbf(txt, trg):				O(1)
    len_trg = len(trg)					O(1)
    matches = []					O(1)
    for i in range(len(txt)-(len_trg-1)):		O(n)
        fin = i+len_trg						O(1)
        if comp(txt[i:fin], trg):				O(n)
            matches.append((i,fin-1))					O(1)
    if not matches:					O(1)
        matches.append(-1)					O(1)
    return matches					O(1)
TOTAL-------------------------------------------O(n) * O(n) = O(n^2)

Main:
------------------------------------------------
from google.colab import drive			O(1)
drive.mount('/content/drive')			O(1)
with open('/***/sequence.fasta') as f:		O(1)
    lines = f.readlines()			O(n)
print(lines)					O(1)
------------------------------------------------
secuence=''					O(1)
for l in lines[1:len(lines)-1]:			O(n)
  secuence+=l[:len(l)-1]			O(1)
print(secuence)					O(1)
------------------------------------------------
target = 'TAATAGCTTCTTAGGAGAATGACAAAA'		O(1)
a=sbf(secuence, target)				O(n^2)

if a[0] == -1:					O(1) 
        print('********')			O(1)
else:
    print(****)					O(1)
    for i in a:					O(1)
        print(****)				O(1)
TOTAL-------------------------------------------O(n)+O(n)+O(n^2) = O(n^2)
