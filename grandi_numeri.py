import numpy
from numpy.random import randn

#variabile che contiene il numero di tentativi
N = 500000
#counter dei numeri inclusi tra -1 e 1
cnt = 0
#generazione N valori casuali 
randN = randn(N)
for i in randN:
    if  (i > -1 and i < 1):
        cnt = cnt + 1
answer = cnt/N
print("answer = ", answer)

