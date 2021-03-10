import pandas as pd
import os

#Metodo 1: leggere csv da path assoluto
stats = pd.read_csv('C:\\MyProjects\\GithubRepo\\LearningPythonCourse\\csv\\DemographicData.csv')

#Metodo 2: Cambiamo la working directory
print("Current Working Directory = ", os.getcwd())
#Cambio working directory
os.chdir("C:\\MyProjects\\GithubRepo\\LearningPythonCourse\\csv")
stats2 = pd.read_csv('DemographicData.csv')

#Visualizzazione CSV letti (bisogna sempre verificare il numero di righe, per una questione di tracciabilità)
#In questo modo capiamo se il numero di righe importate equivale al numero di righe nel file
print(stats)
print(stats2)

#--- Lezione 2: Esplorare i dati

#Numeri di righe
print("Numero di righe di stats = ", len(stats))

#Numeri di colonne del dataset
#Molto spesso ci sono tante colonne ed è utile avere il numero di colonne in modo leggibile
print("Colonne importate = ", stats.columns)
print("Numero di colonne = ", len(stats.columns))

#top and tail rows (Utile per verifiche)
#Le prime 5 righe più in alto
print("Top Rows = ", stats.head())
#Le prime 7 righe più in alto
print("Top Rows = ", stats.head(7))
#Le prime 5 righe più in basso
print("Bottom Rows = ", stats.tail())
#Le prime 7 righe più in basso
print("Bottom Rows = ", stats.tail(7))

#Info sulla tabella (colonne, tipo di ogni colonna, valori nulli o no, numero di righe)
print(stats.info())

#Statistiche sulle colonne numeriche
print(stats.describe())

#Statistiche sulle colonne numeriche (trasposta su righe)
print(stats.describe().transpose())

#Rinominare le colonne
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

print(stats)

#--- Lezione 3: Subset from Data Frames

# 1 - Rows Subsets
print("\n******* Rows Subsets ******")
print("\nRighe dalla 21ma alla 25ma:\n")
print(stats[21: 26])

print("\nRighe dalla 1ma alla 25ma:\n")
print(stats[0: 26])

print("\nRighe dalla 1ma alla 9a (partono da 0):\n")
print(stats[0: 10]) #equivale a stats.head(10)

print("\nRighe dalla 185ma fino alla fine:\n")
print(stats[185 :])

print("\nRighe dall'inizio alla fine, invertite:\n")
print(stats[: : -1])

print("\nUna riga ogni 10, dall'inizio alla fine del data frame:\n")
print(stats[: : 10])

# 2 - Columns Subset
print("****** Columns Subsets ******\n")
print("\nVisualizzazione colonna dei nomi delle nazioni:\n")
print(stats["CountryName"])

print("\nVisualizzazione della parte superiore della colonna (primi 5 valori) dei nomi delle nazioni:\n")
print(stats["CountryName"].head())

print("\nVisualizzazione dei primi 5 valori dei nomi delle nazioni e dei rispettivi Birth Rates:\n")
#Ricordare le doppie quadre! L'ordine delle colonne è quello dato da noi
print(stats[["CountryName", "BirthRate"]].head()) 
print("\nQuick Access:\n")
print(stats.BirthRate) #ecco perché è importante cambiare il nome alle colonne!

# 3 - Combine Rows and Columns
print("****** Combine Rows and Columns ******\n")
#Prendo la porzione della tabella dalla riga 3 alla 7 
#e come colonne il nome della Nazione, il tasso di natalità e l'Income Group
print(stats[3:8][['CountryName', 'BirthRate', 'IncomeGroup']])