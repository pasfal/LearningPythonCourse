import pandas as pd
import os
#Metodo 1: leggere csv da path assoluto
stats = pd.read_csv('C:\\MyProjects\\PythonWorkspace\\LearningPython\\csv\\DemographicData.csv')

#Metodo 2: Cambiamo la working directory
print("Current Working Directory = ", os.getcwd())
#Cambio working directory
os.chdir("C:\\MyProjects\\PythonWorkspace\\LearningPython\\csv")
stats2 = pd.read_csv('DemographicData.csv')

#Visualizzazione CSV letti
print(stats)
print(stats2)