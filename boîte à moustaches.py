import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("qualite_industrielle.csv")

df.boxplot(column="Nb_Defauts", by="Ligne_Production")


plt.title("Distribution des défauts par ligne de production")
plt.suptitle("")
plt.xlabel("Ligne de production")
plt.ylabel("Nombre de défauts")
plt.tight_layout()
plt.show()

"""

explication : 
• Le minimum : la plus petite valeur de la série (hors valeurs aberrantes).
• Le premier quartile (Q₁) : la valeur en dessous de laquelle se situent 25 % des données.
• La médiane (Q₂) : la valeur du milieu (50 % des données sont en dessous, 50 % au-dessus), représentée par une ligne à l'intérieur de la boîte.
• Le troisième quartile (Q₃) : la valeur en dessous de laquelle se situent 75 % des données.
• Le maximum : la plus grande valeur de la série (hors valeurs aberrantes)
• Les valeurs aberrantes (outliers) : les points situés au-delà des moustaches (des lignes qui partent de la boîte 
                                                                             et s'étendent généralement jusqu'à 1,5 × IQR 
                                                                             pour capturer les valeurs normales)

IQR = Q₃ - Q₁ : l'écart interquartile

"""