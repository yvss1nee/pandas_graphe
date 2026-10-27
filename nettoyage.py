import pandas as pd



df = pd.read_csv("qualite_industrielle.csv")

#affichage des informations du fichier
print(df.info())

#3 afficher le nombre des element nulls ou dupliques
print(df.isnull().sum())
print(df.duplicated().sum())

#4 les donnees principales du ficher
#Nb_Defauts
#Taux_Defauts_pct
#Dimension_mm
#Poids_g
#Temperature_C
#Nb_Non_Conformites
#Temps_Controle_min
#Cout_Non_Qualite_DH
#Resultat





#6 enregistrer le fichier
df.to_csv("qualite_industrielle_nettoyee.csv", index=False)








