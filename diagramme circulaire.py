import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("qualite_industrielle.csv")


y = df["Resultat"].value_counts()
label = ["Conforme", "Non conforme"]
plt.pie(y, labels=y.index, autopct="%1.1f%%")

plt.title("Répartition des résultats de contrôle")
plt.show()