# Ma version
import pandas as pd
data = pd.read_csv('j1-1.csv')

l1 = []
l2 = []
result = 0

for i in range(0, data.shape[0]):
    n1,n2 = data.iloc[i][0].split()
    l1.append(n1)
    l2.append(n2)
    
l1.sort()
l2.sort()


for i in range(0,len(l1)):
    result +=  abs(int(l1[i])-int(l2[i]))

print(result)

#-----------------------------------------------------------------------------------------------------------

#Ma version améliorée par chat GPT
import pandas as pd

# Lecture des données
data = pd.read_csv('j1-1.csv')

# Initialisation des listes et du résultat
list_1 = []
list_2 = []
total_difference = 0

# Traitement des lignes du fichier pour extraire les paires de nombres
for row in data.iloc[:, 0]:  # Parcourt uniquement la première colonne
    num1, num2 = map(int, row.split())  # Sépare et convertit les nombres en entiers
    list_1.append(num1)
    list_2.append(num2)

# Tri des listes
list_1.sort()
list_2.sort()

# Calcul de la somme des différences absolues
total_difference = sum(abs(a - b) for a, b in zip(list_1, list_2))

print(total_difference)
