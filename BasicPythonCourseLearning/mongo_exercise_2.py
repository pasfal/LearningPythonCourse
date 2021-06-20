from pymongo import MongoClient

#connessione con mongodb
client = MongoClient("localhost", 27017)

#crea (o accede a ) un database testdb, con autenticazione
db = client.testdb
db.authenticate("testuser", "password123")

#crea una collection su questo db
personeCollection = db.persone

print("\nQuery 1: trovare e visualizzare la prima persona nella collection:")

primaPersona = personeCollection.find_one()
print(primaPersona)

print("\nQuery 2: trovare le persone con computer 'asus':")

persone = personeCollection.find({"computer": "asus"})
for persona in persone:
    print(persona)

print("\nQuery 3: Modificare l'età di Giuseppe Verdi:")

'''
il secondo parametro è un'operazione di set e dice che bisogna settare l'età a 45 di Giuseppe Verdi
(il secondo parametro è un dizionario che ha come valore un dizionario al suo interno)
Le operazioni hanno il $ come prefisso
'''
persone = personeCollection.update_one({"nome": "Giuseppe", "cognome":"Verdi"}, {"$set": {"eta": 45}})
personaModificata = personeCollection.find_one({"nome": "Giuseppe", "cognome":"Verdi"})
print(personaModificata)

print("\nQuery 4: Troviamo tutte le persone il cui cognome in ordine afabetico viene dopo 'Rossi':")
'''
Al metodo find abbiamo passato una query e questa query dice a mongo
di restituire tutti quei documenti (persone) il cui cognome, in ordine alfabetico,
viene dopo il cognome 'Rossi'
'''
persone = personeCollection.find({"cognome":{"$gt":"Rossi"}})
for persona in persone:
    print(persona)