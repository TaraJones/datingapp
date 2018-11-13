import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Create df here:
df = pd.read_csv("profiles.csv")

print(df.body_type.value_counts())

drink_mapping = {"not at all": 0, "rarely": 1, "socially": 2, "often": 3, "very often": 4, "desperately": 5}
all_data["drinks_code"] = all_data.drinks.map(drink_mapping)


#Plt age histogram:
plt.hist(df.age, bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xlim(16, 80)
plt.show()