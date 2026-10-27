import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("qualite_industrielle.csv")


defauts = df.groupby("Ligne_Production")["Nb_Defauts"].sum()

defauts.plot(kind="bar")

plt.title("Nombre de défauts par ligne de production")
plt.xlabel("Ligne de production")
plt.ylabel("Nombre total de défauts")


plt.xticks(rotation=0)
plt.tight_layout()

plt.show()