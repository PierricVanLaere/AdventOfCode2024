# Ma version
import pandas as pd
data = pd.read_csv('j1-2.csv')

l1 = []
l2 = []
result = 0

for i in range(0, data.shape[0]):
    n1,n2 = data.iloc[i][0].split()
    l1.append(n1)
    l2.append(n2)
    
l2_occ = {}

for i in range(0,len(l2)):
    if l2[i] not in l2_occ:
        l2_occ[l2[i]] = 1
    else:
        l2_occ[l2[i]] += 1

for i in range(0,len(l1)):
    if l1[i] in l2_occ:
        result += (int(l1[i])*l2_occ[l1[i]])

print(result)

#-----------------------------------------------------------------------------------------------------------

#Ma version améliorée par chat GPT
import pandas as pd
from collections import Counter

# Chargement des données
data = pd.read_csv('j1-2.csv')

l1 = []
l2 = []

# Extraction des colonnes et remplissage des listes
for _, row in data.iterrows():
    n1, n2 = row[0].split()
    l1.append(int(n1))
    l2.append(int(n2))

# Comptage des occurrences dans l2
l2_occ = Counter(l2)

# Calcul du résultat
result = sum(num * l2_occ[num] for num in l1 if num in l2_occ)

print(result)