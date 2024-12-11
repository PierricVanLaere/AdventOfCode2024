# Ma version
import pandas as pd
data = pd.read_csv('j2-1.csv')

unsafe = 0

for i in range(0,data.shape[0]):
    rapport = list((map(int, data.iloc[i][0].split())))
    if ( (rapport == sorted(rapport)) or (rapport == sorted(rapport, reverse=True)) ): #croissant ou decroissant
        isSafe = True
        for j in range(0,len(rapport)-1):
            if isSafe:
                result = abs((rapport[j])-rapport[j+1])
                if result > 3 or result < 1 : # Mauvais écart
                    unsafe+=1
                    isSafe = False
    else:
        unsafe += 1
    
print(data.shape[0]-unsafe)
            
#-----------------------------------------------------------------------------------------------------------

#Ma version améliorée par chat GPT
import pandas as pd

# Chargement des données
data = pd.read_csv('j2-1.csv')

unsafe_count = 0  # Compteur pour les cas non sécurisés

# Parcours de chaque ligne
for i in range(data.shape[0]):
    rapport = list(map(int, data.iloc[i][0].split()))
    
    # Vérifie si le rapport est croissant ou décroissant
    if rapport == sorted(rapport) or rapport == sorted(rapport, reverse=True):
        # Vérifie les écarts entre les éléments
        if any(abs(rapport[j] - rapport[j + 1]) > 3 or abs(rapport[j] - rapport[j + 1]) < 1 for j in range(len(rapport) - 1)):
            unsafe_count += 1
    else:
        unsafe_count += 1

# Nombre de lignes sécurisées
safe_count = data.shape[0] - unsafe_count
print(safe_count)
