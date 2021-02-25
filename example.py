
# Liste (sono come gli array). Sequenza di elementi ordinati ed enumerati partendo da 0
# possono esserci dati eterogenei (numeri, stringhe, float, booleani, ecc.) e una lista
# può contenere anche un'altra lista al suo interno
print("\n\nLezione sulle liste\n\n")
MyFirstList = [3, 45, 56, 732]
#copiare le liste
CopyList1 = MyFirstList.copy()
CopyList2 = MyFirstList[:] 
print(MyFirstList)
print(CopyList1, CopyList2)
print (type(MyFirstList))
MySecondList = [3, "Hello", True, 7.32]
print(MySecondList)
MyThirdList = ["Ciao", 100, MySecondList]
print(MyThirdList)
# In Python 3 range è un iteratore e anche un generatore. L'equivalente di xrange() in Python 2
# creerà un oggetto che ha un riferimento ai 15 interi ma senza metterli in memoria
L4 = list(range(15)) #creiamo una lista con una sequenza di numeri da 0 a 14
print(L4)
L5 = list(range(1,10)) #creiamo una lista con una sequenza di numeri da 1 a 9
print(L5)
L6 = list(range(1,11,2)) #creiamo una lista con una sequenza di numeri da 1 a 10 (saltando di 2)
print(L6)

#lista con i cubi presi dal range
cubi = []
for i in range(1,21):
    cubi.append(i**3)
print(cubi)

#abbreviata
#list comprehension
cubi2= [ i**3 for i in range(1,21)]
print(cubi2)

#con tuple
cubi3= [ (i, i**3) for i in range(1,21)]
print(cubi3)

#cubi dei soli numeri pari
cubiEven = [ (i, i**3) for i in range(1,21) if (i%2 == 0)] 
print(cubiEven)

#moltiplicazione di liste
lista1 = [2,4,6,89,9]
lista2 = [3,5,6,89,6]
listMult = [ (i*j) for i in lista1 for j in lista2]
print (listMult)

#LETTURA LISTE 
#le liste sono indicizzate a partire da 0
w = ['a', 'b', 'c', 'd', 'e']
print(w[2]) #c
print(len(w)) #5
#Possiamo utilizzare in Python anche indici negativi; in questo caso partono da -1
#(ed è il valore più a dx) fino a -5 (il valore più a sx)
print(w[-1], w[-5])
w[1] = 250 #assegnamento
print(w)

#slicing (affettare) una lista in Python

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#prende tutta la lista
print(letters[:])
#parte dal terzo elemento (indice 2) e prende tutta la lista da qui alla fine
print(letters[2:])
#parte dall'inizio della lista e arriva fino al settimo elemento (quello di indice 6)
print(letters[:7])
#prende gli elementi da quello di indice 2 a quello di indice 6 (esclude quello di posizione 7)
print(letters[2:7])
#prende gli elementi da quello di indice -8 a quello di indice 6 (esclude quello di posizione 7)
print(letters[-8:7])
#prende gli elementi da quello di indice -8 a quello di indice -3 (usando gli indici in  negativo)
print(letters[-8:-3])
#prende le lettere dalla lettera di indice 2 a quella di indice 8, con uno step di 2
print(letters[2:9:2])
#prende le lettere dalla lettera di indice 0 a quella di indice 9, con uno step di 3
print(letters[::3])
#prende le lettere dalla lettera di indice -1 (l'ultima) a quella di indice -10, con uno step di 2
print(letters[::-2])
#stampa la lista in ordine inverso
print(letters[::-1])
#tuple (sono liste immutabili, non possiamo modificare, ma possiamo accedere agli elementi)
#non utilizzata in data analysis. Può servire per passare dati ad una funzione e vogliamo essere certi
#che questi dati non vengano cambiati.
tuples=(1, 'a', 2, 'b')
print(tuples)
print(tuples[0])
print(type(tuples))
