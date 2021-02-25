import numpy as np

r1 = list([1,2,3])
r2 = list([4,5,6])
r3 = list([7,8,9])

#matrice generata da tre liste
matrix1 = np.array([r1, r2, r3])
print("\nMatrix1:\n", matrix1)

#matrice generata da un array di un range 0...13
mydata = np.arange(0,14)
matrix2 = mydata.reshape((2, 7))
print("\nMatrix2:\n", matrix2)

#matrice ottenuta da mydata facendo il reshape
#7 righe, 2 colonne, ordinamento in verticale (Fortran like)
matrix3 = np.reshape(mydata, (7,2), 'F')
print("\nMatrix3:\n", matrix3)

#matrice ottenuta da mydata facendo il reshape
#2 righe, 7 colonne, ordinamento in orizzontale (C-like)
matrix4 = np.reshape(mydata, (2,7), 'C')
print("\nMatrix4: \n",matrix4)