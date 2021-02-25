#Dictionary: come una lista, non è ordinato perché ci sono delle chiavi
dict1 = {'key1':'val1', 'key2':'val2', 'key3':'val3'}

#all'elemento si accede con la chiave
print(dict1['key2'])

#Un dizionario può avere valori eterogenei
dict2 = {'Germany':'I have been here', 'France':2, 'Spain':True}

#Non importa l'ordine nel dizionario, noi ci accediamo con le chiavi 
#agli elementi e quindi Python lo memorizza nel modo ottimale possibile.
print(dict2)
print(dict2['Spain'])