import pymongo
from pymongo import MongoClient

#connessione con mongodb
client = MongoClient("localhost", 27017)

#crea (o accede a ) un database testdb, con autenticazione
db = client.testdb
db.authenticate("testuser", "password123")

#crea una collection su questo db
personeCollection = db.persone

'''
crea indici per velocizzare l'accesso ai dati 
(è possibile creare indici multipli, con ordine ascending o descending)

'''
personeCollection.create_index([("nome", pymongo.ASCENDING)])
personeCollection.create_index([("cognome", pymongo.ASCENDING)])
personeCollection.create_index([("computer", pymongo.ASCENDING)])

#creo un documento
doc1 = {"nome":"Mario", "cognome":"Rossi", "eta":30, "computer":["asus", "apple"]}
doc2 = {"nome":"Giuseppe", "cognome":"Verdi", "eta":35, "computer":["asus"]}

personeCollection.insert_one(doc1)
personeCollection.insert_one(doc2)

