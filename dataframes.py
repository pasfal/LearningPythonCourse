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